import logging
from openai import OpenAI

def extract_references(text:str, model:str="gpt-4o", api_key:str=None)->str:
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
    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": """You are a helpful
                                            assistant that extracts references from text."""},
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
