from src.agents.competitor_agent import run_competitor_agent


sales_analysis = """
Product: Snowflake Data Cloud
Product Category: Cloud Data Platform
Prospect Company: Target
Target Customer: Chief Data Officer
Competitors: Databricks, Google BigQuery
"""


research_analysis = """
Target operates a large retail business with broad product categories.

The website shows digital commerce activity, seasonal promotions,
and customer engagement through digital channels.

No information was found regarding Target's current cloud data
platform or data infrastructure.
"""


result = run_competitor_agent(
    product_name="Snowflake Data Cloud",
    product_category="Cloud Data Platform",
    competitors="Databricks, Google BigQuery",
    sales_analysis=sales_analysis,
    research_analysis=research_analysis,
)


print("\nOutput\n")
print(result)