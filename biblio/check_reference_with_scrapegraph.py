""""
check_reference_with_scrapegraph module
"""
import logging
from scrapegraphai.graphs import SearchGraph


def check_reference_with_scrapegraph(title:str, openai_key:str):
    """
    Checks if a reference is present using ScrapeGraph.

    Args:
        title (str): The title of the reference to check.
        openai_key (str): The api key

    Returns:
        dict: The response data from ScrapeGraph.
    """
    logging.debug(f"Checking reference with ScrapeGraph: {title}")

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
