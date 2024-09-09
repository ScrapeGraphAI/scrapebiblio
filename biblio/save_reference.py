"""
save_references module
"""
import logging
import logging

def save_references(references:str, output_path:str)->str:
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
