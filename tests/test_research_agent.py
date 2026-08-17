from src.agents.research_agent import run_research_agent
from src.tools.webscraper import fetch_website_text


company_url = "https://www.target.com"


print("\nFetching company website...")

website_text = fetch_website_text(company_url)

print(f"Website text extracted: {len(website_text)} characters")


print("\nRunning Research Agent...")


result = run_research_agent(
    product_name="Snowflake Data Cloud",
    product_category="Cloud Data Platform",
    company_url=company_url,
    website_text=website_text,
)


print("\nOutput\n")

print(result)