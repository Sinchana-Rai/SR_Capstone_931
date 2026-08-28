from io import BytesIO

from reportlab.pdfgen import canvas

from src.tools.document_parser import (extract_product_document_text)


sample_lines = [
    "Product: Salesforce CRM",
    "",
    "Salesforce CRM helps organizations manage customer relationships,",
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


# Create a PDF file in memory
buffer = BytesIO()

pdf = canvas.Canvas(buffer)

y_position = 800

for line in sample_lines:
    pdf.drawString(50, y_position, line)

    y_position -= 20

pdf.save()

file_bytes = buffer.getvalue()


# Test the document parser
result = extract_product_document_text(
    file_bytes=file_bytes,
    file_name="salesforce_product.pdf"
)


print("\nExtracted PDF Product Document\n")
print("-" * 40)

print(result)

print("\nCharacters extracted:")
print(len(result))