import logging
import PyPDF2
import openai
import requests
import json
import os
from dotenv import load_dotenv

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')
semantic_scholar_api_key = os.getenv('SEMANTIC_SCHOLARE_API_KEY')

if not semantic_scholar_api_key:
    raise EnvironmentError("S2_API_KEY environment variable not set.")

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        str: Extracted text from the PDF.
    """
    logging.debug("Starting text extraction from PDF...")
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    logging.debug("Text extracted from PDF.")
    return text

def split_text(text, max_tokens=3000):
    """
    Splits the text into chunks of a specified maximum size.

    Args:
        text (str): Text to split.
        max_tokens (int): Maximum size of each chunk.

    Returns:
        list: List of text chunks.
    """
    logging.debug("Starting text splitting into chunks...")
    words = text.split()
    chunks = []
    current_chunk = []
    current_length = 0

    for word in words:
        word_length = len(word)
        if current_length + word_length + 1 > max_tokens:
            chunks.append(' '.join(current_chunk))
            current_chunk = []
            current_length = 0
        current_chunk.append(word)
        current_length += word_length + 1

    if current_chunk:
        chunks.append(' '.join(current_chunk))

    logging.debug(f"Text split into {len(chunks)} chunks.")
    return chunks

def extract_references(text, model="gpt-4"):
    """
    Extracts references from the text using the OpenAI API.

    Args:
        text (str): Text from which to extract references.

    Returns:
        str: Extracted references.
    """
    logging.debug("Starting extraction of references from text...")
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant that extracts references from text."},
            {"role": "user", "content": f"Extract all references from the following text and format them in a consistent manner:\n\n{text}\n\nFormat each reference as:\n1. \"Title\" - [Reference Number]\n2. \"Title\" - [Reference Number]\n..."}
        ],
        max_tokens=4096,
        n=1,
        stop=None,
        temperature=0.0,
    )
    references = response.choices[0].message.content.strip()
    logging.debug("References extracted from text.")
    return references

def save_references(references, output_path):
    """
    Saves the references to a file.

    Args:
        references (str): References to save.
        output_path (str): Path to the output file.
    """
    logging.debug("Starting to save the references to a file...")
    with open(output_path, 'w') as file:
        file.write(references)
    logging.debug(f"References saved to {output_path}")

def check_reference_in_semantic_scholar(reference):
    """
    Checks if a reference is present in the Semantic Scholar database.

    Args:
        reference (str): The reference to check.

    Returns:
        dict: The response data from the Semantic Scholar API.
    """
    headers = {
        "x-api-key": semantic_scholar_api_key
    }

    title = reference.split('-')[0].strip()

    response = requests.post(
        'https://api.semanticscholar.org/graph/v1/paper/batch',
        headers=headers,
        json={
            "ids": [title],
            "fields": "referenceCount,citationCount,title"
        }
    )

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Error: {response.status_code}", "response": response.json()}

def main():
    """
    Main function that processes a PDF, extracts text, and saves the references.
    """
    pdf_path = 'test/558779153.pdf'
    references_output_path = 'references.md'

    logging.debug("Starting PDF processing...")

    pdf_text = extract_text_from_pdf(pdf_path)

    references = extract_references(pdf_text)

    # Save the references to a Markdown file
    with open(references_output_path, 'w') as file:
        file.write(f"# References\n\n{references}")

    logging.debug(f"References saved to {references_output_path}")
    logging.debug("Processing completed.")

if __name__ == "__main__":
    main()
