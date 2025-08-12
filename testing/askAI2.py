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

async def main():
    question = "I need help, no electrity is there"
    context = '''{
    'content': 'Q1: How do I apply for a new residential connection? A: Complete the online application on our portal or visit the nearest customer service center with proof of identity, proof of ownership/occupancy, a site plan, and the required fees. Typical lead time is 7–14 business days depending on site inspection.\\n\\nQ2: How are bills calculated? A: Bills are calculated based on meter reading (kWh) multiplied by applicable tariff slabs, fixed monthly charge, and taxes/levies. Late payment fees apply after the due date.\\n\\nQ3: How do I report a power outage? A: Use the mobile app, call 1800-NE-HELP (example), or report via the outage reporting form on the website. Provide location, nearest landmark, and any observed cause.\\n\\nQ4: How do I request meter replacement? A: Fill an online meter replacement form or book service; an authorized technician will inspect and, if needed, replace the meter within the SLA.\\n\\nQ5: What documents do I need for commercial connections? A: Business registration certificate, PAN, proof of premises, authorized signatory ID and financial guarantee if required.', 
    'fileURL': 'http://0akshay.github.io/help.html'
    'source': 'InternalKnowledgeBase', 
    'title': 'North Electric - Customer FAQs', 
    'id': 'doc-001', 
    'category': 'FAQ', 
    'tags': ['faq', 'billing', 'connections', 'outage', 'service'], 
    'last_updated': '2025-08-12', 
    '@search.score': 2.6178992, 
    '@search.reranker_score': None, 
    '@search.highlights': None, 
    '@search.captions': None
}'''
    
    prompt = "You are a context aware chatbot of North Electric which is a power utility company. You are provided with a user question and context. Answer the question STRICTLY based on context and nothing else. You may paraphrase the answer. If the context is not sufficient say, \"Sorry, I don't have enough information on that.\". The context you would be provided will have a 'fileURL' parameter, at the end of your answer give this 'fileURL' as source. Here is the question and the context: "+f"[QUESTION START] {question} [QUESTION END] "+f"[CONTEXT START] {context} [CONTEXT END]"

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
