import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load from .env
API_KEY = os.getenv("API_KEY")

HEADERS = {
    "Authorization": f"Bearer {API_KEY}"
}

ENDPOINT = "https://api.groq.com/openai/v1/chat/completions"

def spin_content(markdown_text):
    payload = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "user", "content": f"Spin this chapter creatively: {markdown_text}"}
        ]
    }
    response = requests.post(ENDPOINT, json=payload, headers=HEADERS)

    print(response.status_code)
    print(response.text)

    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]


def review_content(spun_text):
    payload = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "user", "content": f"Review and refine this version:\n{spun_text}"}
        ]
    }
    response = requests.post(ENDPOINT, json=payload, headers=HEADERS)

    print(response.status_code)
    print(response.text)

    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]
