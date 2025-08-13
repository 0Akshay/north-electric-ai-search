from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from dotenv import load_dotenv
import os
import httpx
import asyncio

# Load environment variables from .env file
load_dotenv()

# Azure Search config from environment
endpoint = os.getenv("ENDPOINT")
index_name = os.getenv("INDEX_NAME")
admin_key = os.getenv("ADMIN_KEY")

if not all([endpoint, index_name, admin_key]):
    raise EnvironmentError("Azure Search environment variables are not set properly")

# Create Azure SearchClient
search_client = SearchClient(endpoint=endpoint, index_name=index_name, credential=AzureKeyCredential(admin_key))

# Azure OpenAI config from environment
AZURE_OPENAI_BASE = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_VERSION = os.getenv("AZURE_OPENAI_VERSION")
AZURE_OPENAI_MODEL = os.getenv("AZURE_OPENAI_MODEL")
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")

if not all([AZURE_OPENAI_BASE, AZURE_OPENAI_VERSION, AZURE_OPENAI_MODEL, AZURE_OPENAI_KEY]):
    raise EnvironmentError("Azure OpenAI environment variables are not set properly")

router = APIRouter()

# Pydantic model for request body
class AskAIRequest(BaseModel):
    question: str

# Pydantic model for response
class AskAIResponse(BaseModel):
    answer: str

@router.post("/askai", response_model=AskAIResponse)
async def ask_ai(request: AskAIRequest):
    query = request.question

    # Perform Azure Search with the query
    results = search_client.search(search_text=query)

    # Compile top 4 documents' 'content' fields (up to 400 chars each)
    compiled_docs = ""
    for i, result in enumerate(results):
        if i >= 4:
            break
        content = result.get("content") or ""
        compiled_docs += " " + content[:500]

    # Prepare prompt with context
    prompt = (
        "You are a context aware chatbot of North Electric which is a power utility company. "
        "You are provided with a user question and context. Answer the question based on context and nothing else. "
        "Keep your tone helpful"
        "Only if the user greets you, you greet the user and tell them that you are an intelligent bot of North Electric and ask them how should you help them."
        "You may paraphrase the answer. Keep your answers concise. If the context is not sufficient say, \"Sorry, I don't have enough information on that.\". "
        "The context is an array of string which is the context. "
        "Here is the question and the context: "
        f"[QUESTION START] {query} [QUESTION END] [CONTEXT START] {compiled_docs} [CONTEXT END]"
    )

    # print("QUERY")
    # print(query)
    # print("COMPILED QUERY")
    # print()
    # print("COMPILED DOCS")
    # print(compiled_docs)
    # print("END COMPILED DOCS")
    
    # Azure OpenAI endpoint
    endpoint = f"{AZURE_OPENAI_BASE}/openai/deployments/{AZURE_OPENAI_MODEL}/chat/completions?api-version={AZURE_OPENAI_VERSION}"

    payload = {
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 100,
    }

    headers = {
        "Content-Type": "application/json",
        "api-key": AZURE_OPENAI_KEY,
    }

    # Async HTTP call to Azure OpenAI
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(endpoint, headers=headers, json=payload)
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=response.status_code, detail=f"OpenAI API error: {e}")

        data = response.json()
        assistant_msg = data["choices"][0]["message"]["content"]

    return AskAIResponse(answer=assistant_msg)
