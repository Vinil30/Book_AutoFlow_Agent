import requests

def spin_content(markdown_text):
    payload = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "user", "content": f"Spin this chapter creatively: {markdown_text}"}
        ]
    }
    headers = {"Authorization": "Bearer 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"}
    response = requests.post("https://api.groq.com/openai/v1/chat/completions", json=payload, headers=headers)

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
    headers = {"Authorization": "Bearer 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"}
    response = requests.post("https://api.groq.com/openai/v1/chat/completions", json=payload, headers=headers)

    print(response.status_code)
    print(response.text)

    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]
