import requests
from bs4 import BeautifulSoup

def fetch_website_text(url):
    """
        Download a webpage and extract readable text.

    Args:
        url (str): Website URL to scrape.

    Returns:
        str: Cleaned webpage text.
    """

    try:
        response = requests.get(url, timeout=20,
                                headers={"User-Agent": "Mozilla/5.0"})

        #this method automatically throws an exception if an HTTP request failed
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        #remove the content that doesnot help our analysis
        for elmt in soup(["script", "style", "nav", "footer", "header", "noscript"]):
            elmt.decompose()

        output_text = soup.get_text(separator=" ", strip = True)

        return output_text  

    except requests.RequestException as error:
        return f"Error retrieving website: {error}"

