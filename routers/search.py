from fastapi import APIRouter
from pydantic import BaseModel
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from dotenv import load_dotenv
import os
import httpx

load_dotenv()

# Azure Search
endpoint = os.getenv("ENDPOINT")
index_name = os.getenv("INDEX_NAME")
admin_key = os.getenv("ADMIN_KEY")
search_client = SearchClient(endpoint=endpoint, index_name=index_name,
                             credential=AzureKeyCredential(admin_key))

# Azure OpenAI
AZURE_OPENAI_BASE = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_VERSION = os.getenv("AZURE_OPENAI_VERSION")
AZURE_OPENAI_MODEL = os.getenv("AZURE_OPENAI_MODEL")
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")

router = APIRouter()

# Request body model
class SearchRequest(BaseModel):
    query: str

async def get_relevant_urls(question: str):
    # Step 1: Query Azure Cognitive Search
    results = search_client.search(search_text=question)
    # print(results)
    # print("RESULTEND\n")
    compiledDocs = []
    for i, result in enumerate(results):
        # print(result)
        if i >= 3:
            break
        compiledDocs.append({
            'category': result['category'],
            'fileURL': result['fileURL']
        })
    
    print()
    print(compiledDocs)
    return compiledDocs

    # Step 2: Prepare prompt for Azure OpenAI
    # prompt = (
    #     "You are a context aware chatbot of North Electric which is a power utility company. "
    #     "You have to give only 'fileURL' of the 3 or less most relevant objects. "
    #     "Give these 'fileURL's as an array strings"
    #     f"[QUESTION START] {question} [QUESTION END] "
    #     f"[CONTEXT START] {compiledDocs} [CONTEXT END]"
    # )

    # endpoint_url = f"{AZURE_OPENAI_BASE}/openai/deployments/{AZURE_OPENAI_MODEL}/chat/completions?api-version={AZURE_OPENAI_VERSION}"
    # payload = {"messages": [{"role": "user", "content": prompt}], "max_tokens": 100}
    # headers = {"Content-Type": "application/json", "api-key": AZURE_OPENAI_KEY}

    # async with httpx.AsyncClient(timeout=60) as client:
    #     response = await client.post(endpoint_url, headers=headers, json=payload)
    #     response.raise_for_status()
    #     data = response.json()
    #     return data["choices"][0]["message"]["content"].strip()

# Step 3: POST endpoint
@router.post("/search")
async def search_endpoint(body: SearchRequest):
    try:
        urls = await get_relevant_urls(body.query)
        return urls
    except Exception as e:
        return {"error": str(e)}
