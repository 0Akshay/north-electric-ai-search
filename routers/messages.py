from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
import httpx
import os
from dotenv import load_dotenv

# To load env variables;
load_dotenv()

router = APIRouter()

AZURE_OPENAI_BASE = os.getenv("AZURE_OPENAI_ENDPOINT")  # e.g. "https://<your-resource>.openai.azure.com"
AZURE_OPENAI_VERSION = os.getenv("AZURE_OPENAI_VERSION")  # e.g. "2024-06-01"
AZURE_OPENAI_MODEL = os.getenv("AZURE_OPENAI_MODEL")  # e.g. "gpt-4o-mini"
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")

@router.post("/ask-ai")
async def ask_ai(request: Request):
    try:
        body = await request.json()
        user_prompt = body.get("prompt", "Hello")

        system_message = "You are an AI assistant specialized in index search."

        context = [
            {"role": "user", "content": "What is index search?"},
            {"role": "assistant", "content": "Index search is ..."}
        ]

        messages = [
            {"role": "system", "content": system_message},
            *context,
            {"role": "user", "content": user_prompt}
        ]

        if not all([AZURE_OPENAI_BASE, AZURE_OPENAI_VERSION, AZURE_OPENAI_MODEL, AZURE_OPENAI_KEY]):
            return JSONResponse({"error": "Azure OpenAI environment variables not fully configured"}, status_code=500)

        endpoint = f"{AZURE_OPENAI_BASE}/openai/deployments/{AZURE_OPENAI_MODEL}/chat/completions?api-version={AZURE_OPENAI_VERSION}"

        payload = {
            "messages": messages,
            "max_tokens": 300
        }

        headers = {
            "Content-Type": "application/json",
            "api-key": AZURE_OPENAI_KEY
        }

        async with httpx.AsyncClient(timeout=15) as client:
            response = await client.post(endpoint, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()

    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)
