import os
import logging
from dotenv import load_dotenv
from biblio.convert_to_md import convert_to_md
from biblio.utils.read import openai_to_speech

load_dotenv()

def main():
    pdf_path = 'test/558779153.pdf'
    references_output_path = 'results/converted_file.md'

    openai_api_key = os.getenv('OPENAI_API_KEY')
    semantic_scholar_api_key = os.getenv('SEMANTIC_SCHOLARE_API_KEY')

    if not openai_api_key:
        raise EnvironmentError("OPENAI_API_KEY environment variable not set.")
    if not semantic_scholar_api_key:
        raise EnvironmentError("SEMANTIC_SCHOLARE_API_KEY environment variable not set.")

    logging.debug("Starting PDF processing...")

    convert_to_md(pdf_path, references_output_path, openai_api_key)

    logging.debug("Processing completed.")

    file = open(references_output_path, "r").read()

    openai_to_speech(openai_api_key, file, "results/res.mp3")

if __name__ == "__main__":
    main()