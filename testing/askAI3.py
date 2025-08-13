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
search_client = SearchClient(endpoint=endpoint, index_name=index_name, credential=AzureKeyCredential(admin_key))

# Example search
query = "is there a number for emergency"
print(query)

results = search_client.search(search_text=query)

compiledDocs = ""
i = 1
for result in results:
    if (i > 4):
        break
    compiledDocs = compiledDocs + " " + result['content'][:400]
    i=i+1

AZURE_OPENAI_BASE = os.getenv("AZURE_OPENAI_ENDPOINT")  
AZURE_OPENAI_VERSION = os.getenv("AZURE_OPENAI_VERSION") 
AZURE_OPENAI_MODEL = os.getenv("AZURE_OPENAI_MODEL")
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")

async def main():
    question = query
    context = compiledDocs
    
    prompt = "You are a context aware chatbot of North Electric which is a power utility company. You are provided with a user question and context. Answer the question STRICTLY based on context and nothing else. You may paraphrase the answer. If the context is not sufficient say, \"Sorry, I don't have enough information on that.\". The context is an array of string which is the context. Here is the question and the context: "+f"[QUESTION START] {question} [QUESTION END] "+f" [CONTEXT START] {context} [CONTEXT END]"

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
