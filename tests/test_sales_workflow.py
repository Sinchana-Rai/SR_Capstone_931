from src.workflows.sales_workflow import run_sales_workflow


result = run_sales_workflow(
    product_name="Snowflake Data Cloud",
    company_url="https://www.target.com",
    product_category="Cloud Data Platform",
    competitors="Databricks, Google BigQuery",
    value_proposition=(
        "Helps organizations store, analyze, and share data "
        "using a scalable cloud platform."
    ),
    target_customer="Chief Data Officer",
)


print("Sales Agent result")
print("*" *40 + "\n")
print(result["sales_analysis"])

print("Research agent result")
print("*" *40 + "\n")
print(result["research_analysis"])

print("\nCompetitor agent result")
print("*" *40 + "\n")
print(result["competitor_analysis"])

print("\nStrategy & Leadership Agent result")
print("*" *40 + "\n")
print(result["strategy_leadership_analysis"])

print("\nFinal Sales Intelligence Report")
print("*" *40 + "\n")
print(result["final_report"])

print("Workflow Info")
print("*" *40 + "\n")

print(
    f"Website characters processed: "
    f"{len(result['website_text'])}"
)

print(
    f"Corporate research characters processed: "
    f"{len(result['corporate_source_data'])}"
)