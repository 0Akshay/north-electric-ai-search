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
    "id": "doc-001",
    "title": "North Electric - Customer FAQs",
    "category": "FAQ",
    "source": "InternalKnowledgeBase",
    "last_updated": "2025-08-12",
    "tags": ["faq","billing","connections","outage","service"],
    "content": "Q1: How do I apply for a new residential connection? A: Complete the online application on our portal or visit the nearest customer service center with proof of identity, proof of ownership/occupancy, a site plan, and the required fees. Typical lead time is 7–14 business days depending on site inspection.\\n\\nQ2: How are bills calculated? A: Bills are calculated based on meter reading (kWh) multiplied by applicable tariff slabs, fixed monthly charge, and taxes/levies. Late payment fees apply after the due date.\\n\\nQ3: How do I report a power outage? A: Use the mobile app, call 1800-NE-HELP (example), or report via the outage reporting form on the website. Provide location, nearest landmark, and any observed cause.\\n\\nQ4: How do I request meter replacement? A: Fill an online meter replacement form or book service; an authorized technician will inspect and, if needed, replace the meter within the SLA.\\n\\nQ5: What documents do I need for commercial connections? A: Business registration certificate, PAN, proof of premises, authorized signatory ID and financial guarantee if required.",
    "fileURL": "http://localhost:8000/faqs"
  },
  {
    "id": "doc-002",
    "title": "Current Retail Tariff — Sample (Update Required)",
    "category": "CurrentPrices",
    "source": "RegulatoryAndBilling",
    "last_updated": "2025-08-12",
    "tags": ["tariff","prices","billing","residential","commercial"],
    "content": "NOTE: Replace these sample numbers with official approved tariffs before publishing.\\n\\nResidential (single-phase):\\n- 0–100 kWh: ₹3.50 per kWh\\n- 101–300 kWh: ₹5.20 per kWh\\n- >300 kWh: ₹7.00 per kWh\\nFixed charge: ₹50/month\\nCommercial (three-phase):\\n- All consumption: ₹9.50 per kWh\\nDemand charge: ₹200/kVA/month\\nTaxes: As per central & state statutes (electricity duty & GST where applicable).\\nConcessions: Lifeline slab and agricultural subsidies to be applied per customer category.",
    "fileURL": "http://localhost:8000/rates"
  },
  {
    "id": "doc-003",
    "title": "Power Outage — Response SOP",
    "category": "PowerOutage",
    "source": "Operations",
    "last_updated": "2025-08-12",
    "tags": ["outage","sop","restoration","safety","operations"],
    "content": "Purpose: Rapid, safe restoration of supply and transparent customer communication.\\n\\n1. Detection: Automated SCADA/AMR alerts or customer reports via hotline/app.\\n2. Triage: Control center logs incident, classifies outage (local/feeder/HT/transformer).\\n3. Safety: If downed lines are reported, dispatch safety patrol and mark hazard zone. Public warnings issued on social channels.\\n4. Dispatch: Closest crew assigned; estimated time to repair (ETR) sent to affected customers.\\n5. Repair: Isolate faulted section, replace damaged equipment, perform earthing/insulation tests.\\n6. Restoration: Re-energize after safety checks.\\n7. Post-incident: Root cause analysis, preventive action plan, update asset maintenance schedule.\\nSLA: Major feeder faults — restore within 6 hours; localized faults — restore within 4 hours where feasible.",
    "fileURL": "http://localhost:8000/news"
  },
  {
    "id": "doc-004",
    "title": "Billing — Customer Support SOP",
    "category": "Billing",
    "source": "CustomerService",
    "last_updated": "2025-08-12",
    "tags": ["billing", "payment", "support", "policy", "helpline"],
    "content": "Purpose: Ensure transparent billing practices, timely communication, and effective resolution of billing concerns.\\n\\n1. Billing Cycle: Bills are generated monthly on the 1st and due by the 15th. Cycle dates vary slightly by region.\\n2. Bill Breakdown: Each bill includes energy usage (kWh), fixed charges, taxes, previous balance, and late fees if any. A sample bill with section-wise explanation is available on our website.\\n3. Payment Options: Customers can pay via mobile app, online portal, authorized retail centers, bank auto-debit, or UPI.\\n4. Late Payment Policy: A 2% penalty is applied on overdue amounts after the due date. Services may be suspended after 30 days of non-payment.\\n5. Dispute Resolution: Customers can raise disputes within 7 days of bill generation. Disputes are resolved within 3 working days.\\n6. Helpline Support: A dedicated billing support line is available at 1800-XXX-XXXX (8AM–8PM, Mon–Sat) or via live chat in the app.\\n7. Alerts & Reminders: SMS/email alerts are sent for bill generation, due reminders, and overdue warnings.\\nSLA: Billing complaints to be acknowledged within 24 hours and resolved within 72 hours wherever possible.",
    "fileURL": "http://localhost:8000/billing"
  }
]


# Upload
result = search_client.upload_documents(documents=documents)
print("Upload result:", result)
