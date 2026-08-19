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
    Discover and prioritize useful internal corporate links.

    Args:
        base_url (str): Corporate/company website.
        max_links (int): Maximum number of useful links returned.

    Returns:
        list: Relevant internal URLs ranked by research value.
    """

    keyword_weights = {
        "leadership": 14,
        "executive": 10,
        "investor": 9,
        "news": 9,
        "press": 9,
        "technology": 8,
        "innovation": 8,
        "strategy": 12,
        "about": 5,
        "company": 5,
    }

    try:
        response = requests.get(base_url, timeout=10,
            headers={"User-Agent": "Mozilla/5.0"})

        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        base_domain = urlparse(base_url).netloc

        scored_links = []

        for link in soup.find_all("a", href=True):

            href = link.get("href")

            full_url = urljoin(base_url, href)

            # Ignore links outside the same domain
            if urlparse(full_url).netloc != base_domain:
                continue

            link_text = link.get_text(separator=" ", strip=True).lower()

            searchable_text = (full_url.lower() + " " + link_text)

            score = 0

            for keyword, weight in keyword_weights.items():
                if keyword in searchable_text:
                    score += weight

            if score > 0:
                scored_links.append((full_url, score))

        # Remove duplicate URLs
        unique_links = {}

        for url, score in scored_links:
            if (url not in unique_links
                or score > unique_links[url]):
                unique_links[url] = score

        # Sort highest score first
        sorted_links = sorted(unique_links.items(), key=lambda item: item[1], reverse=True)

        # Return only URLs
        return [url
            for url, score in sorted_links[:max_links]]

    except requests.RequestException as error:
        print(f"Error discovering links: {error}")
        return []


def build_company_research_data(corporate_url, max_links=4, max_char_per_page=4000, max_total_characters=12500):
    """
    Discover useful corporate pages and collect their text.

    Args:
        corporate_url (str): Corporate website URL.
        max_links (int): Maximum pages to research.
        max_char_per_page (int): Maximum characters from each page.

    Returns:
        str: Combined research source data.
    """

    links = discover_research_links(corporate_url, max_links=max_links)

    # Always include the corporate homepage
    urls = [corporate_url]

    for link in links:
        if link not in urls:
            urls.append(link)

    print(f"Researching {len(urls)} corporate pages...")

    source_data = fetch_multiple_websites(urls, max_char_per_page=max_char_per_page)

    # Prevent very large prompts from being sent to Groq
    source_data = source_data[:max_total_characters]
    return source_data