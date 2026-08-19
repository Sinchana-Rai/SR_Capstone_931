from src.tools.webscraper import discover_research_links


corporate_url = "https://corporate.target.com"


print("\nDiscovering research links...\n")


links = discover_research_links(corporate_url, max_links=10)


print("Discovered links\n")


for number, link in enumerate(links, start=1):
    print(f"{number}. {link}")


print(
    f"\nTotal useful links discovered: "
    f"{len(links)}"
)