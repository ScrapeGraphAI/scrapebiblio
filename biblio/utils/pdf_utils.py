import logging
import PyPDF2

def extract_text_from_pdf(pdf_path:str)->str:
    """
    Extracts text from a PDF file.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        str: Extracted text from the PDF.
    """
    logging.debug("Starting text extraction from PDF...")
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    logging.debug("Text extracted from PDF.")
    return text
