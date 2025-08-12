from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from dotenv import load_dotenv
import asyncio
import httpx
import os

# To load env variables;
load_dotenv()

# Azure Search details
endpoint = os.getenv("ENDPOINT")
index_name = os.getenv("INDEX_NAME")
admin_key = os.getenv("ADMIN_KEY")

# Create SearchClient
search_client = SearchClient(endpoint=endpoint,
                             index_name=index_name,
                             credential=AzureKeyCredential(admin_key))

# Example search
query = "power outage"  # try changing this to "new connection", "tariff", etc.
# query = "I missed something"  # try changing this to "new connection", "tariff", etc.
results = search_client.search(search_text=query)

# print(f"Results for query: '{query}'\n")
# for result in results:
#     print(f"ID: {result['id']}")
#     if 'title' in result:
#         print(f"Title: {result['title']}")
#     print(f"Category: {result.get('category', 'N/A')}")
#     print(f"Content snippet: {result['content'][:150]}...")
#     print("-" * 60)
compiledDocs = []
i = 1
for result in results:
    if (i > 4):
        break
    r = { 'content': result['content'][:400], 'fileURL': result['fileURL'] }
    print(r)
    compiledDocs.append(r)
    print(i)
    i=i+1
    print()
    
print(compiledDocs)
print()
print()


AZURE_OPENAI_BASE = os.getenv("AZURE_OPENAI_ENDPOINT")  # e.g. "https://<your-resource>.openai.azure.com"
AZURE_OPENAI_VERSION = os.getenv("AZURE_OPENAI_VERSION")  # e.g. "2024-06-01"
AZURE_OPENAI_MODEL = os.getenv("AZURE_OPENAI_MODEL")  # e.g. "gpt-4o-mini"
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")

async def main():
    question = query
    context = compiledDocs
    
    prompt = "You are a context aware chatbot of North Electric which is a power utility company. You are provided with a user question and context. Answer the question STRICTLY based on context and nothing else. You may paraphrase the answer. If the context is not sufficient say, \"Sorry, I don't have enough information on that.\". The context is an array of objects which have 'content' and 'fileURL' keys. At the end of your answer give the 'fileURL' of the object which has most relevant 'content' as per the question. Here is the question and the context: "+f"[QUESTION START] {question} [QUESTION END] "+f"[CONTEXT START] {context} [CONTEXT END]"

    endpoint = f"{AZURE_OPENAI_BASE}/openai/deployments/{AZURE_OPENAI_MODEL}/chat/completions?api-version={AZURE_OPENAI_VERSION}"

    payload = {
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 100
    }

    headers = {
        "Content-Type": "application/json",
        "api-key": AZURE_OPENAI_KEY
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(endpoint, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        # Extract assistant message content
        assistant_msg = data["choices"][0]["message"]["content"]
        print("Assistant:", assistant_msg)

if __name__ == "__main__":
    asyncio.run(main())
    print("end")
