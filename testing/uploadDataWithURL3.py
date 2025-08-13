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

# Create search client
search_client = SearchClient(endpoint=endpoint,
                             index_name=index_name,
                             credential=AzureKeyCredential(admin_key))

# Example data
documents = [
  {
    "id": "doc-010",
    "title": "High Electricity Bill — Customer Support SOP",
    "category": "High Bill Management",
    "source": "North Electric CustomerService",
    "last_updated": "2025-08-12",
    "tags": ["high bill", "billing", "energy saving", "appliances", "support", "conservation", "tips"],
    "content": "Purpose: Help North Electric customers understand causes of high electricity bills and provide guidance on managing costs and using energy-efficient appliances to reduce bills.\n\n1. Understanding High Bills: Customers should review usage patterns and billing details to identify reasons for unusually high bills such as increased consumption, meter errors, or appliance inefficiency.\n\n2. Audit and Check Meter Readings: Verify the meter readings match bills and conduct energy audits to identify hidden power drains or malfunctioning devices causing high energy use.\n\n3. Energy-Saving Appliances: Recommend use of ENERGY STAR certified and energy-efficient appliances like LED lighting, induction cooktops, inverter ACs, and efficient refrigerators to reduce electricity consumption.\n\n4. Usage Tips to Manage High Bills: Encourage customers to turn off unused devices, unplug electronics on standby, schedule high-energy tasks during off-peak hours, and optimize thermostat and water heater settings.\n\n5. Smart Technology: Use smart plugs and home energy monitoring devices available via North Electric to control and track electricity use effectively.\n\n6. Contact Support: Customers with persistent or unexplained high bills can contact North Electric support through the helpline at 1800-XXX-XXXX or live chat for assistance and dispute resolution.\n\n7. Preventive Measures: Promote behavioral changes such as reducing peak hour usage, taking shorter showers to reduce water heating costs, and regular maintenance of appliances to avoid excess energy consumption.\n\nSLA: High bill inquiries acknowledged within 4 hours and resolved or clarified within 5 business days where possible.",
    "fileURL": "http://localhost:8000/billing"
  }
]


# Upload
result = search_client.upload_documents(documents=documents)
print("Upload result:", result)
