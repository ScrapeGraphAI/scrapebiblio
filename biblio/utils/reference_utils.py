import logging
import requests
import os
from scrapegraphai.graphs import SearchGraph

def save_references(references:str, output_path:str):
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

def check_reference(reference:str, semantic_scholar_api_key:str, use_semantic_scholar=True):
    """
    Checks if a reference is present in the Semantic Scholar database or using ScrapeGraph.

    Args:
        reference (str): The reference to check.
        semantic_scholar_api_key (str): The API key for Semantic Scholar.
        use_semantic_scholar (bool): Whether to use Semantic Scholar or ScrapeGraph.

    Returns:
        dict: The response data from the Semantic Scholar API or ScrapeGraph.
    """
    title = reference.split('-')[0].strip()

    if use_semantic_scholar:
        if semantic_scholar_api_key is None:
            raise ValueError('Semantic scholar api not provided')

        headers = {
            "x-api-key": semantic_scholar_api_key
        }

        response = requests.post(
            'https://api.semanticscholar.org/graph/v1/paper/batch',
            headers=headers,
            json={
                "ids": [title],
                "fields": "referenceCount,citationCount,title"
            }
        )

        if response.status_code == 200:
            return response.json()
        else:
            logging.debug(f"Reference not found in Semantic Scholar: {title}")
            return check_reference_with_scrapegraph(title)
    else:
        return check_reference_with_scrapegraph(title)

def check_reference_with_scrapegraph(title:str)->dict:
    """
    Checks if a reference is present using ScrapeGraph.

    Args:
        title (str): The title of the reference to check.

    Returns:
        dict: The response data from ScrapeGraph.
    """
    logging.debug(f"Checking reference with ScrapeGraph: {title}")

    openai_key = os.getenv("OPENAI_API_KEY")

    graph_config = {
        "llm": {
            "api_key": openai_key,
            "model": "openai/gpt-4",
        },
        "max_results": 2,
        "verbose": True,
    }

    search_graph = SearchGraph(
        prompt=f"Find information about the paper titled: {title}",
        config=graph_config
    )

    result = search_graph.run()
    return result
