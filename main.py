# simple_web_scraping_example.py

import requests

def fetch_website_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

if __name__ == "__main__":
    url = "http://example.com"
    content = fetch_website_content(url)
    if content:
        print("Fetched website content:")
        print(content[:500])  # Print only the first 500 characters
    else:
        print("Failed to fetch the website content.")
