import logging
from .utils.pdf_utils import extract_text_from_pdf
from .utils.text_utils import split_text, tokenize_text
from .utils.openai_utils import extract_references, convert_text_to_markdown
from .utils.reference_utils import save_references, check_reference

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def process_pdf(pdf_path, references_output_path, openai_api_key, semantic_scholar_api_key):
    """
    Processes a PDF, extracts text, and saves the references.

    Args:
        pdf_path (str): Path to the PDF file.
        references_output_path (str): Path to the output file for references.
        openai_api_key (str): The API key for OpenAI.
        semantic_scholar_api_key (str): The API key for Semantic Scholar.
    """
    logging.debug("Starting PDF processing...")

    pdf_text = extract_text_from_pdf(pdf_path)

    references = extract_references(pdf_text, api_key=openai_api_key)

    with open(references_output_path, 'w') as file:
        file.write(f"# References\n\n{references}")

    logging.debug(f"References saved to {references_output_path}")

    for reference in references.split('\n'):
        if reference.strip():
            result = check_reference(reference, semantic_scholar_api_key, use_semantic_scholar=False)
            logging.debug(f"Reference check result: {result}")

    logging.debug("Processing completed.")
