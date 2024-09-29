import os
import logging
from dotenv import load_dotenv
from biblio.convert_to_md import convert_to_md

load_dotenv()

def main():
    array = ["11061.pdf", "11065.pdf",
            "11143.pdf", "11144.pdf"]
    references_output_path = 'results/converted_file.md'

    openai_api_key = os.getenv('OPENAI_API_KEY')
    semantic_scholar_api_key = os.getenv('SEMANTIC_SCHOLARE_API_KEY')

    if not openai_api_key:
        raise EnvironmentError("OPENAI_API_KEY environment variable not set.")
    if not semantic_scholar_api_key:
        raise EnvironmentError("SEMANTIC_SCHOLARE_API_KEY environment variable not set.")

    logging.debug("Starting PDF processing...")

    for elem in array:
        pdf_path = "test/thayer/"+elem
        references_output_path = 'results/'+elem.split(".")[0]+".md"
        convert_to_md(pdf_path, references_output_path, openai_api_key)

    logging.debug("Processing completed.")

if __name__ == "__main__":
    main()
