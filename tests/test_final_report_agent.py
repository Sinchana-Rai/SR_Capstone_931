from src.agents.final_report_agent import run_final_report_agent


sales_analysis = """
Product: Snowflake Data Cloud
Prospect: Target
Target Customer: Chief Data Officer
Competitors: Databricks, Google BigQuery
"""

research_analysis = """
Target is a large omnichannel retailer.
Its public website emphasizes seasonal promotions,
digital engagement, and broad retail operations.
"""

competitor_analysis = """
Databricks and Google BigQuery are the provided competitors.
No evidence was found that Target currently uses either platform.
"""

strategy_leadership_analysis = """
Target's strategic priorities include accelerating technology,
improving personalization, digital discovery, and guest experience.

Relevant executives identified include Prat Vemana,
Chief Information and Product Officer, and Sarah Travis,
Chief Digital and Revenue Officer.

Target also highlights AI investment and digital twin technology.

Sources:
https://corporate.target.com
https://corporate.target.com/about/leadership-team
"""

source_urls = [
    "https://www.target.com",
    "https://corporate.target.com",
    "https://corporate.target.com/about/leadership-team",
]

result = run_final_report_agent(
    product_name="Snowflake Data Cloud",
    company_url="https://www.target.com",
    sales_analysis=sales_analysis,
    research_analysis=research_analysis,
    competitor_analysis=competitor_analysis,
    strategy_leadership_analysis=strategy_leadership_analysis,
    source_urls=source_urls,
)


print("\n Sales Intelligence Report")
print("-" *40 + "\n")

print(result)