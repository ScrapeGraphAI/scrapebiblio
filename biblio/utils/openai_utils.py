import logging
import openai
from .text_utils import tokenize_text

def extract_references(text:str, model:str="gpt-4", api_key:str=None)->str:
    """
    Extracts references from the text using the OpenAI API.

    Args:
        text (str): Text from which to extract references.
        model (str): The model to use for the API call.
        api_key (str): The API key for OpenAI.

    Returns:
        str: Extracted references.
    """
    logging.debug("Starting extraction of references from text...")
    client = openai.OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant that extracts references from text."},
            {"role": "user", "content": f"""Extract all references from the following
                                            text and format them in a consistent manner: \n{text}\n.
                                            Format each reference as:\n
                                                1. \"Title\" by Authors - [Reference Number]\n
                                                2. \"Title\" by Authors - [Reference Number]\n
                                            ..."""}
        ],
        max_tokens=4096,
        n=1,
        stop=None,
        temperature=0.0,
    )
    references = response.choices[0].message.content.strip()
    logging.debug("References extracted from text.")
    return references

def convert_text_to_markdown(text:str, temp_output_path:str, api_key:str=None)->str:
    """
    Converts the entire text to Markdown using the OpenAI API.

    Args:
        text (str): The entire text to be converted.
        temp_output_path (str): Path to the temporary output file.
        api_key (str): The API key for OpenAI.

    Returns:
        str: Text in Markdown format.
    """
    markdown_text = ''

    tokenized_chunks = tokenize_text(text)
    total_chunks = len(tokenized_chunks)

    for i, chunk_text in enumerate(tokenized_chunks):
        logging.debug(f"Starting conversion of chunk {i + 1}/{total_chunks} to Markdown...")
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", 
                 "content": "You are a helpful assistant that converts text to Markdown."},
                {"role": "user", 
                 "content": f"Convert the following text to Markdown:\n\n{chunk_text}"}
            ],
            max_tokens=4096,
            n=1,
            stop=None,
            temperature=0.5,
            api_key=api_key
        )
        markdown_text += response.choices[0].message.content.strip() + '\n\n'
        logging.debug(f"Chunk {i + 1}/{total_chunks} converted to Markdown.")

        with open(temp_output_path, 'w') as file:
            file.write(markdown_text)
        logging.debug(f"Temporary Markdown saved to {temp_output_path} after chunk {i + 1}/{total_chunks}.")

    return markdown_text
