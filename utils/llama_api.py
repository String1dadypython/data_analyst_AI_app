import requests
import os

TOGETHER_API_KEY = os.getenv("0e16e6e8e818ff0cfa315f301ed1b68a6ea11e3d7fe3efb3e97971906a9b6035")  # Make sure this is set properly

def query_llama(prompt):
    url = "https://api.together.xyz/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, json=data)

    try:
        result = response.json()
        print("🧪 Full API Response:", result)  # Debug print
        return result['output']['choices'][0]['text'].strip()
    except KeyError:
        print("❌ Unexpected response format:", result)
        return "Sorry, something went wrong with the AI response."

