from src.tools.webscraper import fetch_multiple_websites


urls = [
    "https://www.target.com",
    "https://corporate.target.com",
]


result = fetch_multiple_websites(urls)


print("\nMulti-page website data\n")

print(result[:5000])


print("\ntotal num of characters\n")

print(len(result))