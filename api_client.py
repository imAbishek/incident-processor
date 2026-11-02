import requests

def fetch_remote_url(url):
    try:
        response = requests.get(url, timeout=1)
        response.raise_for_status()
        result = response.json()
        return result
    except requests.exceptions.HTTPError:
        print("HTTP request failed")
    except requests.exceptions.Timeout:
        print("Request timed out")
    except requests.exceptions.ConnectionError as error:
        print(f"Connection failed : {error}")
    return None

