import requests

def read_text_from_api(api_key:str, input_text:str, model:str="gpt-4o"):
    """
    This function sends a text input to the OpenAI API and returns the generated text response.

    :param api_key: Your OpenAI API key
    :type api_key: str
    :param input_text: The text input for the API request
    :type input_text: str
    :param model: The specific OpenAI model to use, defaults to "gpt-4"
    :type model: str
    :return: Generated text response from the API
    :rtype: str
    """
    url = "https://api.openai.com/v1/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "prompt": input_text,
        "max_tokens": 100
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()['choices'][0]['text'].strip()
    else:
        raise Exception(f"API Error: {response.status_code}, {response.reason}")