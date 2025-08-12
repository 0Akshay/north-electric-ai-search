from azure.search.documents import SearchClient
from azure.search.documents.indexes import SearchIndexClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv
import os


# To load env variables;
load_dotenv()

# Set these environment variables or replace with your values
endpoint = os.getenv("ENDPOINT")  # e.g. https://<service-name>.search.windows.net
index_name = os.getenv("INDEX_NAME")  # e.g. north-electric-index
api_key = os.getenv("ADMIN_KEY")   # admin or query key with delete rights

search_client = SearchClient(endpoint=endpoint, index_name=index_name, credential=AzureKeyCredential(api_key))

def delete_all_documents():
    batch_size = 1000
    while True:
        results = search_client.search(search_text="*", select=["id"], top=batch_size)
        docs_to_delete = [{"@search.action": "delete", "id": doc["id"]} for doc in results]

        if not docs_to_delete:
            print("No more documents to delete.")
            break

        result = search_client.upload_documents(documents=docs_to_delete)
        print(f"Deleted {len(docs_to_delete)} documents in batch.")

if __name__ == "__main__":
    delete_all_documents()
