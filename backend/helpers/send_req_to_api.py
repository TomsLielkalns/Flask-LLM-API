import os
import requests


def send_to_hf(input_text):
    URL = os.getenv("HF_API_URL")
    API_KEY = os.getenv("HF_API_KEY")

    if not URL or not API_KEY:
        raise ValueError("API URL and API Key must be set in environment variables.")

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "inputs": input_text
    }
    response = requests.post(URL, json=payload, headers=headers)
    print(response)
    if response.status_code != 200:
        raise requests.exceptions.HTTPError(f"Error from huggingface API: {response.text}")
    return response.json()
