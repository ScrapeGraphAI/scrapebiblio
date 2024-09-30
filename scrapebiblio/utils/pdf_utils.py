"""
pdf_utils module
"""
import logging
import fitz

def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extracts text from a PDF file, including handling special cases like PDF Packages.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        str: Extracted text from the PDF.
    """
    logging.debug("Starting text extraction from PDF...")

    extracted_text = ''

    # Open the PDF using PyMuPDF
    try:
        with fitz.open(pdf_path) as pdf:
            for page_num in range(pdf.page_count):
                logging.debug(f"Extracting text from page {page_num + 1}...")
                page = pdf[page_num]
                extracted_text += page.get_text("text") or ''
    except Exception as e:
        logging.error(f"Error during PDF text extraction: {e}")
        return "Error: Unable to extract text from the PDF."

    if not extracted_text.strip():
        logging.warning("The PDF might be a PDF Package or contain special formats.")
        extracted_text = """Unable to extract text from the PDF.
                            It may be a PDF Package or contain embedded files."""

    logging.debug("Text extraction completed.")
    return extracted_text
