# ScrapeBiblio: PDF Reference Extraction and Verification Library

## Powered by Scrapegraphai
![Drag Racing](docs/scrapebiblio.png)
[![Downloads](https://static.pepy.tech/badge/scrapebiblio)](https://pepy.tech/project/scrapebiblio)

This library is designed to extract references from a PDF file, check them against the Semantic Scholar database, and save the results to a Markdown file.

## Overview

The library performs the following steps:

### First usage: extracting references from 
1. **Extract Text from PDF**: Reads the content of a PDF file and extracts the text.
2. **Split Text into Chunks**: Splits the extracted text into smaller chunks to manage large texts efficiently.
3. **Extract References**: Uses the OpenAI API to extract references from the text.
4. **Save References**: Saves the extracted references to a Markdown file.
5. **Check References in Semantic Scholar**: (Optional) Checks if the extracted references are present in the Semantic Scholar database.

## Installation and Setup

To install the required dependencies, you can use the following command:

```bash
pip install scrapebiblio
```

Ensure you have a `.env` file in the root directory of your project with the following content:

```plaintext
OPENAI_API_KEY="YOUR_OPENAI_KEY"
SEMANTIC_SCHOLARE_API_KEY="YOUR_SEMANTIC_SCHOLAR_KEY"
```

## Usage

To use the library, ensure you have the required environment variables set and run the script. The extracted references will be saved to a Markdown file named `references.md`.

### Example

Here is an example of how to use the library:

```python
import logging
import os
from dotenv import load_dotenv
from biblio.find_reference import process_pdf

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()

def main():
    """
    Main function that processes a PDF, extracts text, and saves the references.
    """
    pdf_path = 'test/558779153.pdf'
    references_output_path = 'references.md'

    openai_api_key = os.getenv('OPENAI_API_KEY')
    semantic_scholar_api_key = os.getenv('SEMANTIC_SCHOLARE_API_KEY')

    if not openai_api_key:
        raise EnvironmentError("OPENAI_API_KEY environment variable not set.")
    if not semantic_scholar_api_key:
        raise EnvironmentError("SEMANTIC_SCHOLARE_API_KEY environment variable not set.")

    logging.debug("Starting PDF processing...")

    process_pdf(pdf_path, references_output_path, openai_api_key, semantic_scholar_api_key)

    logging.debug("Processing completed.")

if __name__ == "__main__":
    main()
```

## Contributing

We welcome contributions to this project. If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes.
4. Submit a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.
