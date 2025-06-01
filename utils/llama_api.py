import requests

TOGETHER_API_KEY = "0e16e6e8e818ff0cfa315f301ed1b68a6ea11e3d7fe3efb3e97971906a9b6035"
MODEL = "meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8"

def query_llama(prompt):
    url = "https://api.together.xyz/inference"
    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "max_tokens": 512,
        "temperature": 0.7,
        "top_p": 0.9
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()['output']['choices'][0]['text'].strip()
    else:
        return f"API Error: {response.text}"
