from io import BytesIO

from pypdf import PdfReader
from docx import Document


def extract_txt_text(file_bytes):
    """
    Extract text from a TXT file.
    """

    return file_bytes.decode("utf-8", errors="ignore").strip()


def extract_pdf_text(file_bytes):
    """
    Extract readable text from a PDF file.
    """

    reader = PdfReader(BytesIO(file_bytes))

    pages = []

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            pages.append(page_text)

    return "\n".join(pages).strip()


def extract_docx_text(file_bytes):
    """
    Extract text from a DOCX file.
    """

    document = Document(BytesIO(file_bytes))

    paragraphs = []

    for paragraph in document.paragraphs:

        text = paragraph.text.strip()

        if text:
            paragraphs.append(text)

    return "\n".join(paragraphs).strip()


def extract_product_document_text(
    file_bytes,
    file_name,
    max_characters=12000
):
    """
    Extract text from an uploaded TXT, PDF, or DOCX file.

    Args:
        file_bytes (bytes): Uploaded file contents.
        file_name (str): Original filename.
        max_characters (int): Maximum extracted text returned.

    Returns:
        str: Extracted document text.
    """

    if not file_bytes:
        return ""

    file_name_lower = file_name.lower()

    if file_name_lower.endswith(".txt"):

        text = extract_txt_text(file_bytes)

    elif file_name_lower.endswith(".pdf"):

        text = extract_pdf_text(file_bytes)

    elif file_name_lower.endswith(".docx"):

        text = extract_docx_text(file_bytes)

    else:

        raise ValueError(
            "Unsupported file type. "
            "Please upload a PDF, DOCX, or TXT file."
        )

    # Limit document size before sending to Groq
    return text[:max_characters]