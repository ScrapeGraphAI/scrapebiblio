"""
read module
"""
import os
import openai
from gtts import gTTS

def read_text_from_api(api_key: str, input_text: str, model: str = "gpt-4"):
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
    openai.api_key = api_key
    response = openai.Completion.create(
        engine=model,
        prompt=input_text,
        max_tokens=100
    )
    return response.choices[0].text.strip()

def openai_to_speech(api_key:str, input_text:str, output_path:str, 
                     model:str="gpt-4", lang:str="eng"):
    """
    This function sends a text input to OpenAI, gets the response, and converts it to speech.

    :param api_key: Your OpenAI API key
    :type api_key: str
    :param input_text: The text input for the API request
    :type input_text: str
    :param output_path: The file path where the audio file will be saved
    :type output_path: str
    :param model: The specific OpenAI model to use, defaults to "gpt-4"
    :type model: str
    :return: The filename of the saved audio file
    :rtype: str
    """
    generated_text = read_text_from_api(api_key, input_text, model)
    tts = gTTS(text=generated_text, lang=lang)
    tts.save(output_path)
    os.system(f"start {output_path}")
    return output_path
