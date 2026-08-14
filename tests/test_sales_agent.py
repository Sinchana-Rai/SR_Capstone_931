from src.agents.sales_agent import run_sales_agent


result = run_sales_agent(
    product_name="Snowflake Data Cloud",
    company_url="https://www.target.com",
    product_category="Cloud Data Platform",
    competitors="Databricks, Google BigQuery",
    value_proposition=("Helps organizations store, analyze, and share data "
        "using a scalable cloud platform."),
    target_customer="Chief Data Officer",
)


print("\nOutput\n")
print(result)