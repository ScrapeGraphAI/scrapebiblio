"""
split_text module
"""
import logging

def split_text(text:str, max_tokens:int=3000)->str:
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
