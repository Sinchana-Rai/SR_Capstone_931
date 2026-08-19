import re
import requests
from bs4 import BeautifulSoup

from urllib.parse import urljoin, urlparse

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


def fetch_multiple_websites(urls, max_char_per_page=10000):
    """
    Fetch and combine text from multiple website URLs.

    Args:
        urls (list): List of website URLs.
        max_char_per_page (int): Maximum characters per page.

    Returns:
        str: Combined website text with source URLs.
    """

    combined_text = []

    for url in urls:

        print(f"Fetching: {url}")

        page_text = fetch_website_text(
            url,
            max_char=max_char_per_page
        )

        source_block = f"""
SOURCE URL:
{url}

SOURCE CONTENT:
{page_text}

----------------------------------------
"""

        combined_text.append(source_block)

    return "\n".join(combined_text)


def discover_research_links(base_url, max_links=10):
    """
    Discover useful internal corporate links from a website.

    Args:
        base_url (str): Corporate/company website.
        max_links (int): Maximum number of useful links returned.

    Returns:
        list: Relevant internal URLs.
    """

    keywords = [
        "leadership",
        "executive",
        "company",
        "about",
        "news",
        "press",
        "investor",
        "strategy",
        "technology",
        "innovation",
    ]

    try:
        response = requests.get(
            base_url,
            timeout=10,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        discovered_links = []

        base_domain = urlparse(base_url).netloc

        for link in soup.find_all("a", href=True):

            href = link.get("href")

            full_url = urljoin(base_url, href)

            link_text = link.get_text(separator=" ", strip=True).lower()

            full_url_lower = full_url.lower()

            # Only keep links from the same domain
            if urlparse(full_url).netloc != base_domain:
                continue

            # Check whether URL or link text contains one of our research keywords
            relevant = any(
                keyword in full_url_lower
                or keyword in link_text
                for keyword in keywords
            )

            if relevant and full_url not in discovered_links:
                discovered_links.append(full_url)

            if len(discovered_links) >= max_links:
                break

        return discovered_links

    except requests.RequestException as error:
        print(f"Error discovering links: {error}")
        return []