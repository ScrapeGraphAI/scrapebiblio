# PDF Reference Extraction and Verification Script

This script is designed to extract references from a PDF file, check them against the Semantic Scholar database, and save the results to a Markdown file.

## Overview

The script performs the following steps:

1. **Extract Text from PDF**: Reads the content of a PDF file and extracts the text.
2. **Split Text into Chunks**: Splits the extracted text into smaller chunks to manage large texts efficiently.
3. **Extract References**: Uses the OpenAI API to extract references from the text.
4. **Save References**: Saves the extracted references to a Markdown file.
5. **Check References in Semantic Scholar**: (Optional) Checks if the extracted references are present in the Semantic Scholar database.

## Dependencies

The script uses the following Python libraries:

- `logging`: For logging debug information.
- `PyPDF2`: For reading and extracting text from PDF files.
- `openai`: For interacting with the OpenAI API to extract references.
- `requests`: For making HTTP requests to the Semantic Scholar API.
- `json`: For handling JSON data.
- `os`: For accessing environment variables.
- `dotenv`: For loading environment variables from a `.env` file.

## Environment Variables

The script requires the following environment variables to be set:

- `OPENAI_API_KEY`: Your OpenAI API key.
- `SEMANTIC_SCHOLARE_API_KEY`: Your Semantic Scholar API key.

## Functions

### `extract_text_from_pdf(pdf_path)`

Extracts text from a PDF file.

- **Args**:
  - `pdf_path` (str): Path to the PDF file.
- **Returns**:
  - `str`: Extracted text from the PDF.

### `split_text(text, max_tokens=3000)`

Splits the text into chunks of a specified maximum size.

- **Args**:
  - `text` (str): Text to split.
  - `max_tokens` (int): Maximum size of each chunk.
- **Returns**:
  - `list`: List of text chunks.

### `extract_references(text, model="gpt-4")`

Extracts references from the text using the OpenAI API.

- **Args**:
  - `text` (str): Text from which to extract references.
- **Returns**:
  - `str`: Extracted references.

### `save_references(references, output_path)`

Saves the references to a file.

- **Args**:
  - `references` (str): References to save.
  - `output_path` (str): Path to the output file.

### `check_reference(reference)`

Checks if a reference is present in the Semantic Scholar database.

- **Args**:
  - `reference` (str): The reference to check.
- **Returns**:
  - `dict`: The response data from the Semantic Scholar API.

### `main()`

Main function that processes a PDF, extracts text, and saves the references.

## Usage

To use the script, ensure you have the required environment variables set and run the script. The extracted references will be saved to a Markdown file named `references.md`.