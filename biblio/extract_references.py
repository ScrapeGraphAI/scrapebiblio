"""
extract_references module
"""
import logging
import openai

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
            {"role": "user", "content": f"Extract all references from the following text and format them in a 
             consistent manner:\n\n{text}\n\nFormat each reference as:\n1. \"Title\" - [Reference Number]\n2. 
             \"Title\" - [Reference Number]\n..."}
        ],
        max_tokens=4096,
        n=1,
        stop=None,
        temperature=0.0,
    )
    references = response.choices[0].message.content.strip()
    logging.debug("References extracted from text.")
    return references