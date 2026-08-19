from src.agents.strategy_leadership_agent import (
    run_strategy_leadership_agent
)

from src.tools.webscraper import fetch_multiple_websites


urls = [
    "https://www.target.com",
    "https://corporate.target.com",
]


print("\nFetching strategy and leadership sources...\n")


source_data = fetch_multiple_websites(urls)


print(f"\nSource data collected: "
    f"{len(source_data)} characters")


print("\nRunning Strategy & Leadership Agent...\n")


result = run_strategy_leadership_agent(
    product_name="Snowflake Data Cloud",
    product_category="Cloud Data Platform",
    target_customer="Chief Data Officer",
    company_url="https://www.target.com",
    source_data=source_data,
)


print("\n Output\n")

print(result)