import dotenv
import os
dotenv.load_dotenv()

YOUDOTCOM_API_KEY = os.getenv("YOUDOTCOM_API_KEY")

import requests

def get_ai_snippets_for_query(query):
    headers = {"X-API-Key": YOUDOTCOM_API_KEY}
    params = {"query": query}
    return requests.get(
        f"https://api.ydc-index.io/search?query={query}",
        params=params,
        headers=headers,
    ).json()
    
results = get_ai_snippets_for_query("reasons to smile")
print(results)
