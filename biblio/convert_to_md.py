import logging 
from .utils.pdf_utils import extract_text_from_pdf 
from .utils.openai_utils import convert_text_to_markdown

def convert_to_md(pdf_path, references_output_path, openai_api_key):
    """
    Function to convert a PDF file to Markdown format with reference links extracted from the document.

    :param pdf_path: Str, path to the input PDF file
    :param references_output_path: Str, path to save the output Markdown file with the extracted references
    :param openai_api_key: Str, OpenAI API key for text summarization and conversion to markdown
    """
    logging.debug("Starting PDF processing...")

    pdf_text = extract_text_from_pdf(pdf_path)

    md_text = convert_text_to_markdown(pdf_text, openai_api_key)

    with open(references_output_path, 'w') as f:
        f.write(md_text)

    logging.info("PDF processed and converted to Markdown format successfully.")
