import os
import httpx
import asyncio
from dotenv import load_dotenv

# To load env variables;
load_dotenv()

AZURE_OPENAI_BASE = os.getenv("AZURE_OPENAI_ENDPOINT")  # e.g. "https://<your-resource>.openai.azure.com"
AZURE_OPENAI_VERSION = os.getenv("AZURE_OPENAI_VERSION")  # e.g. "2024-06-01"
AZURE_OPENAI_MODEL = os.getenv("AZURE_OPENAI_MODEL")  # e.g. "gpt-4o-mini"
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")

print(AZURE_OPENAI_BASE, AZURE_OPENAI_VERSION, AZURE_OPENAI_MODEL, AZURE_OPENAI_KEY)

async def main():
    if not all([AZURE_OPENAI_BASE, AZURE_OPENAI_VERSION, AZURE_OPENAI_MODEL, AZURE_OPENAI_KEY]):
        print("Please set all required environment variables.")
        return

    endpoint = f"{AZURE_OPENAI_BASE}/openai/deployments/{AZURE_OPENAI_MODEL}/chat/completions?api-version={AZURE_OPENAI_VERSION}"

    system_message = "You are an AI assistant specialized in index search."
    context = [
        {"role": "user", "content": "What is index search?"},
        {"role": "assistant", "content": "Index search is a method to quickly find information within documents."}
    ]
    user_prompt = "Explain the benefits of index search."

    messages = [
        {"role": "system", "content": system_message},
        *context,
        {"role": "user", "content": user_prompt}
    ]

    payload = {
        "messages": messages,
        "max_tokens": 300
    }

    headers = {
        "Content-Type": "application/json",
        "api-key": AZURE_OPENAI_KEY
    }

    async with httpx.AsyncClient(timeout=15) as client:
        try:
            response = await client.post(endpoint, headers=headers, json=payload)
            response.raise_for_status()
            data = response.json()
            print("Azure OpenAI Response:")
            print(data['choices'][0]['message']['content'])
        except httpx.HTTPError as e:
            print("Request failed:", e)

if __name__ == "__main__":
    asyncio.run(main())
