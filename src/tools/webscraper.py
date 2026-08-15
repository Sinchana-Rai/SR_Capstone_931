import re
import requests
from bs4 import BeautifulSoup

def clean_website_text(text):
    """
    Clean extracted website text by removing repeated
    whitespace and common unnecessary webpage text.
    """

    # remove repeated "Loading..." text
    text = re.sub(r"Loading\.\.\.", "", text, flags=re.IGNORECASE)

    
    # remove some common webpage navigation
    noise_txt = [
    "skip to main content",
    "skip to footer",
    "Sponsored",
    "pause",
    "Homepage",
    "Shop all",
    "Email address",
    "Sign up",
    "Privacy policy",
    "Terms",]

    for txt in noise_txt:
        text = re.sub(re.escape(txt), "", text, flags=re.IGNORECASE)

    # remove repeated whitespace
    text = re.sub(r"\s+", " ", text)

    # remove extra spaces
    text = text.strip()

    return text


def fetch_website_text(url, max_char= 15000):
    """
        Download a webpage and extract readable text.

    Args:
        url (str): Website URL to scrape.
        max_char (int): Maximum amount of text returned.

    Returns:
        str: Cleaned webpage text.
    """

    try:
        response = requests.get(url, timeout=10,
                                headers={"User-Agent": "Mozilla/5.0"})

        #this method automatically throws an exception if an HTTP request failed
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        #remove the content that doesnot help our analysis
        for elmt in soup(["script", "style", "nav", "footer", "header", "noscript"]):
            elmt.decompose()

        output_text = soup.get_text(separator=" ", strip = True)

        #clean extracted text and limit the amoont of text
        text = clean_website_text(output_text)
        text = text[:max_char]

        return text  

    except requests.RequestException as error:
        return f"Error retrieving website: {error}"

