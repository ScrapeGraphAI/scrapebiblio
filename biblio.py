import logging
import PyPDF2
import openai
from dotenv import load_dotenv
import os

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def extract_text_from_pdf(pdf_path):
    """
    Extrae el texto de un archivo PDF.

    Args:
        pdf_path (str): Ruta del archivo PDF.

    Returns:
        str: Texto extraído del PDF.
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
    Divide el texto en fragmentos de tamaño máximo especificado.

    Args:
        text (str): Texto a dividir.
        max_tokens (int): Tamaño máximo de cada fragmento.

    Returns:
        list: Lista de fragmentos de texto.
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

def convert_text_to_markdown(text_chunks, temp_output_path):
    """
    Convierte fragmentos de texto a Markdown utilizando la API de OpenAI.

    Args:
        text_chunks (list): Lista de fragmentos de texto.
        temp_output_path (str): Ruta del archivo temporal de salida.

    Returns:
        str: Texto en formato Markdown.
    """
    markdown_text = ''
    total_chunks = len(text_chunks)
    for i, chunk in enumerate(text_chunks):
        logging.debug(f"Starting conversion of chunk {i + 1}/{total_chunks} to Markdown...")
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that converts text to Markdown."},
                {"role": "user", "content": f"Convert the following text to Markdown:\n\n{chunk}"}
            ],
            max_tokens=4096,
            n=1,
            stop=None,
            temperature=0.5,
        )
        markdown_text += response.choices[0].message.content.strip() + '\n\n'
        logging.debug(f"Chunk {i + 1}/{total_chunks} converted to Markdown.")

        with open(temp_output_path, 'w') as file:
            file.write(markdown_text)
        logging.debug(f"Temporary Markdown saved to {temp_output_path} after chunk {i + 1}/{total_chunks}.")

    return markdown_text

def extract_references(text):
    """
    Extrae las referencias del texto utilizando la API de OpenAI.

    Args:
        text (str): Texto del cual extraer las referencias.

    Returns:
        str: Referencias extraídas.
    """
    logging.debug("Starting extraction of references from text...")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that extracts references from text."},
            {"role": "user", "content": f"Extract all references from the following text:\n\n{text}"}
        ],
        max_tokens=4096,
        n=1,
        stop=None,
        temperature=0.5,
    )
    references = response.choices[0].message.content.strip()
    logging.debug("References extracted from text.")
    return references

def save_references(references, output_path):
    """
    Guarda las referencias en un archivo.

    Args:
        references (str): Referencias a guardar.
        output_path (str): Ruta del archivo de salida.
    """
    logging.debug("Starting to save the references to a file...")
    with open(output_path, 'w') as file:
        file.write(references)
    logging.debug(f"References saved to {output_path}")

def save_markdown(markdown_text, output_path):
    """
    Guarda el texto en formato Markdown en un archivo.

    Args:
        markdown_text (str): Texto en formato Markdown.
        output_path (str): Ruta del archivo de salida.
    """
    logging.debug("Starting to save the Markdown to a file...")
    with open(output_path, 'w') as file:
        file.write(markdown_text)
    logging.debug(f"Markdown saved to {output_path}")

def main():
    """
    Función principal que procesa un PDF, extrae texto, lo convierte a Markdown y guarda las referencias.
    """
    pdf_path = 'test/558779153.pdf'
    output_path = 'output.md'
    temp_output_path = 'temp_output.md'
    references_output_path = 'references.md'

    logging.debug("Starting PDF processing...")

    pdf_text = extract_text_from_pdf(pdf_path)

    text_chunks = split_text(pdf_text)

    markdown_text = convert_text_to_markdown(text_chunks, temp_output_path)

    references = extract_references(pdf_text)

    save_markdown(markdown_text, output_path)

    save_references(references, references_output_path)

    logging.debug("Processing completed.")

if __name__ == "__main__":
    main()
