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
    "content": "Q1: How do I apply for a new residential connection? A: Complete the online application on our portal or visit the nearest customer service center with proof of identity, proof of ownership/occupancy, a site plan, and the required fees. Typical lead time is 7–14 business days depending on site inspection.\\n\\nQ2: How are bills calculated? A: Bills are calculated based on meter reading (kWh) multiplied by applicable tariff slabs, fixed monthly charge, and taxes/levies. Late payment fees apply after the due date.\\n\\nQ3: How do I report a power outage? A: Use the mobile app, call 1800-NE-HELP (example), or report via the outage reporting form on the website. Provide location, nearest landmark, and any observed cause.\\n\\nQ4: How do I request meter replacement? A: Fill an online meter replacement form or book service; an authorized technician will inspect and, if needed, replace the meter within the SLA.\\n\\nQ5: What documents do I need for commercial connections? A: Business registration certificate, PAN, proof of premises, authorized signatory ID and financial guarantee if required."
  },
  {
    "id": "doc-002",
    "title": "Current Retail Tariff — Sample (Update Required)",
    "category": "CurrentPrices",
    "source": "RegulatoryAndBilling",
    "last_updated": "2025-08-12",
    "tags": ["tariff","prices","billing","residential","commercial"],
    "content": "NOTE: Replace these sample numbers with official approved tariffs before publishing.\\n\\nResidential (single-phase):\\n- 0–100 kWh: ₹3.50 per kWh\\n- 101–300 kWh: ₹5.20 per kWh\\n- >300 kWh: ₹7.00 per kWh\\nFixed charge: ₹50/month\\nCommercial (three-phase):\\n- All consumption: ₹9.50 per kWh\\nDemand charge: ₹200/kVA/month\\nTaxes: As per central & state statutes (electricity duty & GST where applicable).\\nConcessions: Lifeline slab and agricultural subsidies to be applied per customer category."
  },
  {
    "id": "doc-003",
    "title": "Power Outage — Response SOP",
    "category": "PowerOutage",
    "source": "Operations",
    "last_updated": "2025-08-12",
    "tags": ["outage","sop","restoration","safety","operations"],
    "content": "Purpose: Rapid, safe restoration of supply and transparent customer communication.\\n\\n1. Detection: Automated SCADA/AMR alerts or customer reports via hotline/app.\\n2. Triage: Control center logs incident, classifies outage (local/feeder/HT/transformer).\\n3. Safety: If downed lines are reported, dispatch safety patrol and mark hazard zone. Public warnings issued on social channels.\\n4. Dispatch: Closest crew assigned; estimated time to repair (ETR) sent to affected customers.\\n5. Repair: Isolate faulted section, replace damaged equipment, perform earthing/insulation tests.\\n6. Restoration: Re-energize after safety checks.\\n7. Post-incident: Root cause analysis, preventive action plan, update asset maintenance schedule.\\nSLA: Major feeder faults — restore within 6 hours; localized faults — restore within 4 hours where feasible."
  },
  {
    "id": "doc-004",
    "title": "How to Apply for a New Connection (Step-by-step)",
    "category": "NewConnection",
    "source": "CustomerService",
    "last_updated": "2025-08-12",
    "tags": ["new-connection","application","documentation","metering"],
    "content": "1) Online application: Visit the North Electric portal → New Connection → fill customer info, select connection type (LT residential / LT commercial / HT), upload documents, pay application fee.\\n2) Document checklist: ID proof (Aadhaar/PAN/Passport), proof of address/ownership (tax receipt/lease), site sketch, NOC if required.\\n3) Site inspection: After payment, scheduling team arranges inspection within 3 working days.\\n4) Estimate & approval: Based on load assessment, service line work required and service charges are computed. Customer approves estimate and pays security deposit.\\n5) Work & meter installation: Civil and electrical crews install service line and meter. Commissioning and energizing once safety tests pass.\\n6) Handover: Final bill & customer welcome kit with tariff class and meter number."
  },
  {
    "id": "doc-005",
    "title": "Book a Repair or Maintenance Visit",
    "category": "BookService",
    "source": "CustomerService",
    "last_updated": "2025-08-12",
    "tags": ["book-service","maintenance","repair","appointment"],
    "content": "Customers can book repair/maintenance via: (a) Mobile app → Services → Book Technician, (b) Website → Book Service, (c) Call center. Required info: service type (meter/meter box/wiring complaint/low voltage), preferred date/time window, contact phone, and photos (optional).\\nPriority tiers: Emergency (no supply/danger) — same-day, High (major appliance failure) — next business day, Routine — within 3–5 business days.\\nOn-site protocol: Technician carries ID, service order, and PPE. Customer must ensure safe access. Post-work, customer signs service completion and receives work order number for records."
  },
  {
    "id": "doc-006",
    "title": "New Smart Meter Rollout - Process & Benefits",
    "category": "Metering",
    "source": "MeteringAndAMR",
    "last_updated": "2025-08-12",
    "tags": ["smart-meter","amr","meter-installation","benefits"],
    "content": "Overview: North Electric’s smart meter program replaces legacy meters with AMR/AMI-enabled meters to enable accurate billing, remote readings, outage detection and time-of-day tariffs.\\nProcess: Customer notification → eligibility check → schedule installation → technician installs smart meter, validates serial and communication link → commission and start remote telemetry.\\nBenefits: Eliminate estimated bills, enable pre-paid and time-of-day pricing, faster outage detection, remote disconnection/reconnection where policy allows.\\nCustomer responsibilities: Ensure meter accessibility; do not tamper with meter. Tampering leads to penalties per tariff order."
  },
  {
    "id": "doc-007",
    "title": "Report Billing Dispute — Procedure",
    "category": "Billing",
    "source": "BillingDept",
    "last_updated": "2025-08-12",
    "tags": ["billing-dispute","complaint","adjustment","meter-reading"],
    "content": "1. Submission: Customer raises dispute via portal or in writing at the customer center with bill number and reason.\\n2. Acknowledgement: A reference number is issued within 24 hours.\\n3. Investigation: Meter reading audit, consumption history review, and site inspection if required (within 7 business days).\\n4. Resolution: If error found, bill is corrected and adjustment applied to next bill; if no error, explanation provided with supporting data.\\n5. Escalation: If customer dissatisfied, escalate to Grievance Redressal Officer; final appeal to electricity ombudsman per regulations."
  },
  {
    "id": "doc-008",
    "title": "Electrical Safety Tips for Customers",
    "category": "Safety",
    "source": "SafetyDept",
    "last_updated": "2025-08-12",
    "tags": ["safety","public-safety","downed-lines","education"],
    "content": "1. Never touch a fallen power line — treat all downed wires as live and call the emergency number.\\n2. Keep children away from substations and transformer areas.\\n3. Use certified electricians for home wiring and get wiring inspected every 3–5 years.\\n4. Do not tamper with meter seals or fuse boxes — report to North Electric for authorized work.\\n5. During storms, unplug major appliances and avoid standing near electrical equipment when wet."
  },
  {
    "id": "doc-009",
    "title": "Transformer and Distribution Asset Maintenance Schedule",
    "category": "AssetManagement",
    "source": "DistributionOperations",
    "last_updated": "2025-08-12",
    "tags": ["maintenance","transformer","schedule","preventive"],
    "content": "Preventive maintenance schedule (typical):\\n- LT distribution transformers: Visual inspection & oil level check — quarterly; oil sampling & dielectric test — annually; bushings & earthing checks — annually.\\n- Feeder lines: Vegetation trimming — biannually; joint inspections — annually; pole integrity audit — every 3 years.\\n- Substations: Relay calibration & protection testing — annually; battery bank test — semi-annually.\\nMaintenance windows: Planned outages for major works will be communicated 48–72 hours in advance to affected customers through SMS and website postings."
  },
  {
    "id": "doc-010",
    "title": "Contact & Escalation Directory",
    "category": "Contact",
    "source": "CustomerService",
    "last_updated": "2025-08-12",
    "tags": ["contact","hotline","escalation","support"],
    "content": "Customer Support (24x7): 1800-NE-HELP (1800-632-4357)\\nEmergency/Downed Lines: 24x7 Outage Hotline: 1800-NE-OUTG (1800-632-6844)\\nEmail: support@north-electric.example.com\\nPayment & Billing: billing@north-electric.example.com\\nGrievance Redressal Officer: gro@north-electric.example.com (Response SLA: 7 business days)\\nOffice Address: Operations HQ, North Electric Ltd., Sector 12 Industrial Area, Cityname — Office hours: Mon–Fri 09:00–18:00.\\nSocial: Twitter/X: @NorthElectric, Facebook: NorthElectricOfficial"
  }
]


# Upload
result = search_client.upload_documents(documents=documents)
print("Upload result:", result)
