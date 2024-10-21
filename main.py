import asyncio
import logging
from src.core.pdf_processor import process_pdf
from src.models.api_config import APIConfig

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

async def main():
    api_config = APIConfig(
        openai_api_key="your_openai_api_key",
        semantic_scholar_api_key="your_semantic_scholar_api_key",
        core_api_key="your_core_api_key",
        base_api_key="your_base_api_key"
    )
    
    await process_pdf(
        pdf_path="path/to/your/pdf",
        references_output_path="path/to/save/references",
        markdown_output_path="path/to/save/markdown",
        api_config=api_config
    )

if __name__ == "__main__":
    asyncio.run(main())
