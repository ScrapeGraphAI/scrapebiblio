"""
reference module
"""
import os
import logging
import requests
from scrapegraphai.graphs import SearchGraph

def save_references(references: str, output_path: str):
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

def check_reference(reference: str, **kwargs):
    """
    Checks if a reference is present in various databases.

    Args:
        reference (str): The reference to check.
        kwargs: Additional API keys and configurations for other sources.

    Returns:
        dict: The response data from the APIs.
    """
    title = reference.split('-')[0].strip()
    return check_reference_with_other_sources(title, **kwargs)

def check_reference_with_other_sources(title: str, **kwargs):
    """
    Checks if a reference is present using other sources.

    Args:
        title (str): The title of the reference to check.
        kwargs: Additional API keys and configurations for other sources.

    Returns:
        dict: The response data from the other sources.
    """
    logging.debug(f"Checking reference with other sources: {title}")

    results = {}

    if 'semantic_scholar_api_key' in kwargs and kwargs.get('use_semantic_scholar', True):
        results['Semantic Scholar'] = check_reference_with_semantic_scholar(title,
                                                                            kwargs['semantic_scholar_api_key'])

    if 'core_api_key' in kwargs:
        results['CORE'] = check_reference_with_core(title, kwargs['core_api_key'])

    if 'base_api_key' in kwargs:
        results['BASE'] = check_reference_with_base(title, kwargs['base_api_key'])

    return results

def check_reference_with_semantic_scholar(title: str, api_key: str) -> dict:
    """
    Checks if a reference is present in the Semantic Scholar database.

    Args:
        title (str): The title of the reference to check.
        api_key (str): The API key for Semantic Scholar.

    Returns:
        dict: The response data from the Semantic Scholar API.
    """
    headers = {
        "x-api-key": api_key
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
        return None

def check_reference_with_core(title: str, api_key: str) -> dict:
    """
    Checks if a reference is present using CORE.

    Args:
        title (str): The title of the reference to check.
        api_key (str): The API key for CORE.

    Returns:
        dict: The response data from the CORE API.
    """
    response = requests.get(f'https://core.ac.uk/api-v2/articles/search/{title}?apiKey={api_key}')
    if response.status_code == 200:
        return response.json()
    else:
        return None

def check_reference_with_base(title: str, api_key: str) -> dict:
    """
    Checks if a reference is present using BASE.

    Args:
        title (str): The title of the reference to check.
        api_key (str): The API key for BASE.

    Returns:
        dict: The response data from the BASE API.
    """
    response = requests.get(f'https://api.base-search.net/cgi-bin/BaseHttpSearchInterface.fcgi?func=performSearch&query={title}&format=json&apiKey={api_key}')
    if response.status_code == 200:
        return response.json()
    else:
        return None

def check_reference_with_scrapegraph(title: str) -> dict:
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
