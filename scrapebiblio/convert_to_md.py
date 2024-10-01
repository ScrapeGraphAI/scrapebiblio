import logging
import os
from .utils.pdf_utils import extract_text_from_pdf
from .utils.openai_utils import convert_text_to_markdown

def convert_to_md(pdf_path, references_output_path, openai_api_key):
    logging.debug("Starting PDF processing...")

    pdf_text = extract_text_from_pdf(pdf_path)

    md_text = convert_text_to_markdown(pdf_text, openai_api_key)

    output_dir = os.path.dirname(references_output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    with open(references_output_path, 'w') as f:
        f.write(md_text)

    logging.info("PDF processed and converted to Markdown format successfully.")
