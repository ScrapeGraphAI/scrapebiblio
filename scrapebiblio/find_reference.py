"""
find_reference module
"""
import logging
from dataclasses import dataclass
from typing import List, Optional
import asyncio
from .utils.pdf_utils import extract_text_from_pdf
from .utils.openai_utils import extract_references
from .utils.reference_utils import check_reference, check_reference_with_scrapegraph

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

@dataclass
class APIConfig:
    openai_api_key: str
    semantic_scholar_api_key: str
    core_api_key: Optional[str] = None
    base_api_key: Optional[str] = None

@dataclass
class Reference:
    title: str
    authors: List[str]
    year: int

async def process_pdf(pdf_path: str, references_output_path: str, api_config: APIConfig) -> None:
    """
    Processes a PDF, extracts text, and saves the references.

    Args:
        pdf_path (str): Path to the PDF file.
        references_output_path (str): Path to the output file for references.
        api_config (APIConfig): Configuration object containing API keys.
    """
    logging.debug("Starting PDF processing...")

    pdf_text = await extract_text_from_pdf(pdf_path)
    references = await extract_references(pdf_text, api_key=api_config.openai_api_key)

    await save_references(references, references_output_path)

    tasks = [
        check_reference(ref, api_config) for ref in references
    ]
    results = await asyncio.gather(*tasks)

    for reference, result in zip(references, results):
        logging.debug(f"Reference check result for {reference.title}: {result}")

        scrapegraph_result = await check_reference_with_scrapegraph(reference.title)
        logging.debug(f"ScrapeGraph check result for {reference.title}: {scrapegraph_result}")

    logging.debug("Processing completed.")

async def save_references(references: List[Reference], output_path: str) -> None:
    with open(output_path, 'w') as file:
        file.write("# References\n\n")
        for ref in references:
            file.write(f"- {ref.title} by {', '.join(ref.authors)} ({ref.year})\n")
    logging.debug(f"References saved to {output_path}")
