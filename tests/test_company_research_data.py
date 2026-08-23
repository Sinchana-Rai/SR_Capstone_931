from src.tools.webscraper import build_company_research_data


corporate_url = "https://corporate.target.com"


print("\nBuilding company research data...\n")


research_data = build_company_research_data(
    corporate_url=corporate_url,
    max_links=4,
    max_char_per_page=4000,
    max_total_characters=12500
)


print("\n Research Data\n")

print(research_data[:8000])


print("\nData Size\n")

print(f"Characters collected: "
    f"{len(research_data)}")