from src.agents.strategy_leadership_agent import (run_strategy_leadership_agent)

from src.tools.webscraper import build_company_research_data


corporate_url = "https://corporate.target.com"


print("\nBuilding company research data...\n")


source_data = build_company_research_data(corporate_url=corporate_url, max_links=4, max_char_per_page=4000)


print(f"\nSource data collected: "
    f"{len(source_data)} characters")


print("\nRunning Strategy & Leadership Agent...\n")


result = run_strategy_leadership_agent(
    product_name="Snowflake Data Cloud",
    product_category="Cloud Data Platform",
    target_customer="Chief Data Officer",
    company_url=corporate_url,
    source_data=source_data,
)


print("\n Output\n")

print(result)