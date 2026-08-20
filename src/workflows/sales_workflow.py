from src.agents.sales_agent import run_sales_agent
from src.agents.research_agent import run_research_agent
from src.agents.competitor_agent import run_competitor_agent

from src.agents.strategy_leadership_agent import (run_strategy_leadership_agent)
from src.tools.webscraper import (fetch_website_text, build_company_research_data)
from src.agents.final_report_agent import run_final_report_agent


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

    print("Step 4: Running Competitor Agent...")

    competitor_analysis = run_competitor_agent(
        product_name=product_name,
        product_category=product_category,
        competitors=competitors,
        sales_analysis=sales_analysis,
        research_analysis=research_analysis,
    )

    print("Step 5: Building corporate research data...")

    corporate_url = "https://corporate.target.com"

    corporate_source_data = build_company_research_data(
        corporate_url=corporate_url,
        max_links=4,
        max_char_per_page=4000,
        max_total_characters=12500,
    )

    print("Step 6: Running Strategy and Leadership Agent...")

    strategy_leadership_analysis = run_strategy_leadership_agent(
        product_name=product_name,
        product_category=product_category,
        target_customer=target_customer,
        company_url=corporate_url,
        source_data=corporate_source_data,
    )

    print("Step 7: Generating Final Sales Intelligence Report...")

    final_report = run_final_report_agent(
        product_name=product_name,
        company_url=company_url,
        sales_analysis=sales_analysis,
        research_analysis=research_analysis,
        competitor_analysis=competitor_analysis,
        strategy_leadership_analysis=strategy_leadership_analysis,
    )

    return {
        "sales_analysis": sales_analysis,
        "research_analysis": research_analysis,
        "competitor_analysis": competitor_analysis,
        "strategy_leadership_analysis": strategy_leadership_analysis,
        "final_report": final_report,
        "website_text": website_text,
        "corporate_source_data": corporate_source_data,
    }