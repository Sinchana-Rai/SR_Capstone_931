from src.tools.document_parser import (extract_product_document_text)


sample_text = """
Product: Salesforce CRM

Salesforce CRM helps organizations manage
customer relationships, sales activities,
marketing interactions, and service operations.

Key Capabilities:
- Customer account management
- Sales pipeline tracking
- Marketing automation
- Reporting and analytics
- Customer service integration

Target Customers:
- Chief Sales Officer
- VP of Sales
- Chief Revenue Officer

Competitors:
- HubSpot
- Microsoft Dynamics
"""


file_bytes = sample_text.encode(
    "utf-8"
)


result = extract_product_document_text(
    file_bytes=file_bytes,
    file_name="salesforce_product.txt"
)


print("\nExtracted Product Document\n")
print("-" * 40)
print(result)

print("\nCharacters extracted:")
print(len(result))