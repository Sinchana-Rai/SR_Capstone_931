from src.tools.webscraper import fetch_website_text


url = "https://www.target.com"

website_text = fetch_website_text(url)

print("\nExtracted data from the website\n")

print(website_text)
print(f"Characters extracted: {len(website_text)}")