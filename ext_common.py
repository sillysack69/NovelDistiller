import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    """Fetch HTML content from a URL."""
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    return response.text