import requests

API_URL = "https://api.thecatapi.com/v1/images/search"

def get_random_cat(full=False):
    response = requests.get(API_URL)
    if response.status_code != 200:
        return None
    data = response.json()
    if not full:
        return data[0]["url"]
    else:
        return data[0]

