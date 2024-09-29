"""
text_utils module
"""
import logging
from typing import List
import tiktoken

def split_text(text:str, max_tokens:int=3000)->List:
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

def tokenize_text(text:str, chunk_size:str=2048)->List:
    """
    Tokenizes the text and splits it into chunks of a specified size.

    Args:
        text (str): Text to tokenize.
        chunk_size (int): Size of each chunk.

    Returns:
        list: List of tokenized text chunks.
    """

    logging.debug("Starting text tokenization...")
    tokenizer = tiktoken.get_encoding("cl100k_base")
    tokens = tokenizer.encode(text)
    token_chunks = [tokens[i:i + chunk_size] for i in range(0, len(tokens), chunk_size)]
    logging.debug(f"Text tokenized into {len(token_chunks)} chunks.")

    return [tokenizer.decode(chunk) for chunk in token_chunks]
