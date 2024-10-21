import logging
import asyncio
from ..models.api_config import APIConfig
from ..utils.pdf_utils import extract_text_from_pdf
from ..services.reference_service import extract_and_check_references
from ..services.markdown_service import convert_to_markdown

async def process_pdf(pdf_path: str, references_output_path: str, markdown_output_path: str, api_config: APIConfig) -> None:
    logging.debug("Starting PDF processing...")

    pdf_text = await extract_text_from_pdf(pdf_path)
    
    references = await extract_and_check_references(pdf_text, api_config)
    
    await save_references(references, references_output_path)
    
    markdown_text = await convert_to_markdown(pdf_text, api_config.openai_api_key)
    
    await save_markdown(markdown_text, markdown_output_path)

    logging.debug("PDF processing completed.")

async def save_references(references, output_path: str) -> None:
    with open(output_path, 'w') as file:
        file.write("# References\n\n")
        for ref in references:
            file.write(f"- {ref.title} by {', '.join(ref.authors)} ({ref.year})\n")
    logging.debug(f"References saved to {output_path}")

async def save_markdown(markdown_text: str, output_path: str) -> None:
    with open(output_path, 'w') as file:
        file.write(markdown_text)
    logging.debug(f"Markdown saved to {output_path}")

async def main(pdf_path: str, references_output_path: str, markdown_output_path: str, api_config: APIConfig) -> None:
    await process_pdf(pdf_path, references_output_path, markdown_output_path, api_config)
