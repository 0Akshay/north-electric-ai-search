from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from dotenv import load_dotenv
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
results = search_client.search(search_text=query)

print(f"Results for query: '{query}'\n")
for result in results:
    print(f"ID: {result['id']}")
    if 'title' in result:
        print(f"Title: {result['title']}")
    print(f"Category: {result.get('category', 'N/A')}")
    print(f"Content snippet: {result['content'][:150]}...")
    print("-" * 60)
