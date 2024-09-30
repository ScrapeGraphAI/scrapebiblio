import os
import logging
from dotenv import load_dotenv
from scrapebiblio.convert_to_md import convert_to_md

load_dotenv()

def main():
    pdf_path = 'test/558779153.pdf'
    references_output_path = 'results/converted_file.md'

    openai_api_key = os.getenv('OPENAI_API_KEY')
    semantic_scholar_api_key = os.getenv('SEMANTIC_SCHOLARE_API_KEY')

    logging.debug("Starting PDF processing...")

    convert_to_md(pdf_path, references_output_path, openai_api_key)

    logging.debug("Processing completed.")

if __name__ == "__main__":
    main()