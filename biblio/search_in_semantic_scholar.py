"""
search_in_semantic_scholar module
"""
import requests

def check_reference_in_semantic_scholar(reference:str, api_key:str)-> str:
    """
    Checks if a reference is present in the Semantic Scholar database.

    Args:
        reference (str): The reference to check.
        api_key (str): api_key

    Returns:
        dict: The response data from the Semantic Scholar API.
    """
    headers = {
        "x-api-key": api_key
    }

    title = reference.split('-')[0].strip()

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
        return {"error": f"Error: {response.status_code}", "response": response.json()}
