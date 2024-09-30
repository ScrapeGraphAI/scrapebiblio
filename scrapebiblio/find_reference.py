"""
find_reference module
"""
import logging
from .utils.pdf_utils import extract_text_from_pdf
from .utils.openai_utils import extract_references
from .utils.reference_utils import check_reference, check_reference_with_scrapegraph

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def process_pdf(pdf_path: str, references_output_path: str,
                openai_api_key: str, semantic_scholar_api_key: str,
                core_api_key: str = None, base_api_key: str = None):
    """
    Processes a PDF, extracts text, and saves the references.

    Args:
        pdf_path (str): Path to the PDF file.
        references_output_path (str): Path to the output file for references.
        openai_api_key (str): The API key for OpenAI.
        semantic_scholar_api_key (str): The API key for Semantic Scholar.
        core_api_key (str, optional): The API key for CORE. Defaults to None.
        base_api_key (str, optional): The API key for BASE. Defaults to None.
    """
    logging.debug("Starting PDF processing...")

    pdf_text = extract_text_from_pdf(pdf_path)

    references = extract_references(pdf_text, api_key=openai_api_key)

    with open(references_output_path, 'w') as file:
        file.write(f"# References\n\n{references}")

    logging.debug(f"References saved to {references_output_path}")

    for reference in references.split('\n'):
        if reference.strip():
            result = check_reference(reference,
                                     semantic_scholar_api_key=semantic_scholar_api_key,
                                     core_api_key=core_api_key,
                                     base_api_key=base_api_key,
                                     use_semantic_scholar=True)
            logging.debug(f"Reference check result: {result}")

            # Check reference with ScrapeGraph
            scrapegraph_result = check_reference_with_scrapegraph(reference)
            logging.debug(f"ScrapeGraph check result: {scrapegraph_result}")

    logging.debug("Processing completed.")
