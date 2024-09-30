import logging
import os
from dotenv import load_dotenv
from scrapebiblio.find_reference import process_pdf

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()

def main():
    """
    Main function that processes a PDF, extracts text, and saves the references.
    """
    pdf_path = 'test/558779153.pdf'
    references_output_path = 'references.md'

    openai_api_key = os.getenv('OPENAI_API_KEY')
    semantic_scholar_api_key = os.getenv('SEMANTIC_SCHOLAR_API_KEY')

    logging.debug("Starting PDF processing...")

    process_pdf(pdf_path, references_output_path, openai_api_key, semantic_scholar_api_key)

    logging.debug("Processing completed.")

if __name__ == "__main__":
    main()
