import requests
from docx import Document
import os

subscription_key = "YyDVYh4FfUho1uJOFz6YMMzSGry3xFigKcvJC7tRQ4IjsQkTWIvnJQQJ99AKACHYHv6XJ3w3AAAbACOG6y1u"
endpoint = "https://api.cognitive.microsofttranslator.com/"
location = "eastus2"
language_destination = "pt-br"

subscription_key = "YyDVYh4FfUho1uJOFz6YMMzSGry3xFigKcvJC7tRQ4IjsQkTWIvnJQQJ99AKACHYHv6XJ3w3AAAbACOG6y1u"
endpoint = "https://api.cognitive.microsofttranslator.com/"
location = "eastus2"
language_destination = "pt-br"

def translate_text(text, target_language):
    path = '/translate'
    constructed_url = endpoint + path
    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(os.urandom(16))
    }
    body = [{
        'text': text
    }]

    params = {
        'api-version': '3.0',
        'from': 'en',
        'to': target_language
    }

    request = requests.post(constructed_url, headers=headers, json=body, params=params)
    response = request.json()
    translated_text = response[0]['translations'][0]['text']
    return translated_text

