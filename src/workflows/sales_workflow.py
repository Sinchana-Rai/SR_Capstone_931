from src.agents.sales_agent import run_sales_agent
from src.agents.research_agent import run_research_agent
from src.tools.webscraper import fetch_website_text

def run_sales_workflow(
    product_name,
    company_url,
    product_category,
    competitors,
    value_proposition,
    target_customer
):
    """
    Coordinate the Sales Agent, website scraper and Research Agent.
    """

    print("Step 1: Running Sales Agent...")

    sales_analysis = run_sales_agent(
        product_name=product_name,
        company_url=company_url,
        product_category=product_category,
        competitors=competitors,
        value_proposition=value_proposition,
        target_customer=target_customer,
    )


    print("Step 2: Fetching company website...")

    website_text = fetch_website_text(
        company_url
    )


    print("Step 3: Running Research Agent...")

    research_analysis = run_research_agent(
        product_name=product_name,
        product_category=product_category,
        company_url=company_url,
        website_text=website_text,
    )


    return {
        "sales_analysis": sales_analysis,
        "research_analysis": research_analysis,
        "website_text": website_text,
    }