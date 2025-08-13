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
    "id": "doc-005",
    "title": "Power Outage — Customer Support SOP",
    "category": "Power Outage",
    "source": "North Electric CustomerService",
    "last_updated": "2025-08-12",
    "tags": ["power outage", "troubleshooting", "support", "contact", "SOP"],
    "content": "Purpose: Provide clear guidance for North Electric customers during power outages and ensure timely resolution through proper troubleshooting and support contact procedures.\n\n1. Reporting Outage: Customers should report power outages via the North Electric mobile app, online portal, or helpline at 1800-XXX-XXXX (available 24/7).\n2. Initial Troubleshooting: Check main circuit breaker and home wiring for issues. Reset breakers if needed. Confirm if outage affects only your home or the neighborhood.\n3. Safety Precautions: Avoid touching downed power lines or damaged electrical equipment. Wait for professional assistance for hazardous conditions.\n4. Outage Updates: Real-time updates and estimated restoration times will be provided through SMS/email alerts and the North Electric app.\n5. Contact Support: Dedicated support available 24/7 through helpline and live chat on the app for outage-related concerns and emergency assistance.\n6. Escalation Process: Prolonged outages exceeding 4 hours are escalated to senior technical teams for faster resolution.\n7. Restoration & Post-Outage Checks: After power restoration, check appliances for damage and report functional issues immediately.\nSLA: Power outage reports acknowledged within 30 minutes and restoration status updated every hour until resolved.",
    "fileURL": "http://localhost:8000/news"
  },
  {
    "id": "doc-006",
    "title": "Electricity Rates — Customer Support SOP",
    "category": "Rates",
    "source": "North Electric CustomerService",
    "last_updated": "2025-08-12",
    "tags": ["rates", "billing", "tariff", "pricing", "support"],
    "content": "Purpose: To provide clear information and assistance regarding electricity rates and tariff structures for North Electric customers.\\n\\n1. Rate Plans: Details on residential, commercial, and industrial rate plans including peak and off-peak rates.\\n2. Tariff Updates: Customers will be informed of any tariff changes through SMS, email, and updates on the North Electric website and app.\\n3. Bill Calculation: Explanation of how bills are calculated based on usage, demand charges, taxes, and subsidies.\\n4. Rate Queries: Customers can contact support via helpline 1800-XXX-XXXX or mobile app chat for rate-related queries.\\n5. Rate Complaints: Any discrepancies or complaints about rates will be acknowledged within 24 hours and resolved within 7 days.\\n6. Educational Resources: Guides and FAQs on understanding electricity rates are available on the website and app.\\nSLA: Rate queries acknowledged within 1 hour and resolved within 48 hours where possible.",
    "fileURL": "http://localhost:8000/rates"
  },
  {
    "id": "doc-007",
    "title": "Customer News and Notifications SOP",
    "category": "News",
    "source": "North Electric CustomerService",
    "last_updated": "2025-08-12",
    "tags": ["news", "notifications", "updates", "customer communication", "support"],
    "content": "Purpose: Ensure timely and accurate communication of news, service updates, and emergency notifications to North Electric customers.\\n\\n1. Communication Channels: Use SMS, email, mobile app push notifications, and social media for customer news distribution.\\n2. Content Approval: All news content is reviewed and approved by the Communications team before release.\\n3. Types of News: Includes planned maintenance, outages, tariff changes, policy updates, and community initiatives.\\n4. Emergency Alerts: High priority alerts such as major outages or safety warnings are sent immediately through all available channels.\\n5. Feedback Mechanism: Customers can provide feedback or report issues related to news via the app or helpline.\\n6. Archival: Past news and announcements are archived on the North Electric website for reference.\\nSLA: Important news acknowledged within 1 hour and customer feedback responded to within 24 hours.",
    "fileURL": "http://localhost:8000/news"
  },
  {
    "id": "doc-009",
    "title": "Company Policies — Customer Support SOP",
    "category": "Policies",
    "source": "North Electric CustomerService",
    "last_updated": "2025-08-12",
    "tags": ["policies", "rules", "compliance", "support", "customer service"],
    "content": "Purpose: Communicate North Electric's customer-related policies clearly to ensure compliance and transparency.\\n\\n1. Service Policies: Guidelines on new connections, disconnections, and service modifications.\\n2. Billing Policies: Payment deadlines, dispute resolution, late fees, and refunds.\\n3. Safety Policies: Customer and employee safety procedures related to electrical services.\\n4. Privacy Policies: Protection of customer data and confidentiality commitments.\\n5. Complaint Handling: Procedures for filing, escalation, and resolution of customer complaints.\\n6. Policy Updates: Customers are notified of policy changes through official communications channels.\\nSLA: Policy inquiries acknowledged within 4 hours and resolved or clarified within 3 business days.",
    "fileURL": "http://localhost:8000/policies"
  }
]


# Upload
result = search_client.upload_documents(documents=documents)
print("Upload result:", result)
