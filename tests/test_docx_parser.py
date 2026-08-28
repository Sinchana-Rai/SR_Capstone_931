from io import BytesIO

from docx import Document

from src.tools.document_parser import (
    extract_product_document_text
)


sample_text = [
    "Product: Salesforce CRM",
    "",
    "Salesforce CRM helps organizations manage customer relationships, "
    "sales activities, marketing interactions, and service operations.",
    "",
    "Key Capabilities:",
    "- Customer account management",
    "- Sales pipeline tracking",
    "- Marketing automation",
    "- Reporting and analytics",
    "- Customer service integration",
    "",
    "Target Customers:",
    "- Chief Sales Officer",
    "- VP of Sales",
    "- Chief Revenue Officer",
    "",
    "Competitors:",
    "- HubSpot",
    "- Microsoft Dynamics",
]


# Create a DOCX file in memory
document = Document()

for line in sample_text:
    document.add_paragraph(line)

buffer = BytesIO()

document.save(buffer)

file_bytes = buffer.getvalue()


# Test the document parser
result = extract_product_document_text(
    file_bytes=file_bytes,
    file_name="salesforce_product.docx"
)


print("\nExtracted DOCX Product Document\n")
print("-" * 40)

print(result)

print("\nCharacters extracted:")
print(len(result))