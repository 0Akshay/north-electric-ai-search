from fastapi import APIRouter, Query
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

async def get_relevant_urls(question: str):
    results = search_client.search(search_text=question)
    compiledDocs = []
    for i, result in enumerate(results):
        if i >= 4:
            break
        compiledDocs.append({
            'content': result['content'][:400],
            'fileURL': result['fileURL']
        })

    prompt = (
        "You are a context aware chatbot of North Electric which is a power utility company. "
        "You have to give only 'fileURL' of the 3 or less most relevant objects. "
        f"[QUESTION START] {question} [QUESTION END] "
        f"[CONTEXT START] {compiledDocs} [CONTEXT END]"
    )

    endpoint_url = f"{AZURE_OPENAI_BASE}/openai/deployments/{AZURE_OPENAI_MODEL}/chat/completions?api-version={AZURE_OPENAI_VERSION}"
    payload = {"messages": [{"role": "user", "content": prompt}], "max_tokens": 100}
    headers = {"Content-Type": "application/json", "api-key": AZURE_OPENAI_KEY}

    async with httpx.AsyncClient(timeout=60) as client:
        response = await client.post(endpoint_url, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"].strip()

@router.get("/search")
async def search_endpoint(query: str = Query(..., description="Search query string")):
    try:
        urls = await get_relevant_urls(query)
        return {"query": query, "recommended_urls": urls}
    except Exception as e:
        return {"error": str(e)}
