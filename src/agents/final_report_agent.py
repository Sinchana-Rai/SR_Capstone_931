import re
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser

from settings import MODEL_ID
from src.prompts.final_report_prompt import final_report_prompt
from src.utils.output_cleaner import clean_llm_output


model = ChatGroq(
    model=MODEL_ID,
    temperature=0,
    max_tokens=2000,
    reasoning_effort="none"
)


parser = StrOutputParser()


final_report_chain = (final_report_prompt | model | parser)


def limit_text(text, max_characters):
    """
    Limit text size before sending it to the final report model.
    """

    if not text:
        return ""

    return text[:max_characters]

def extract_urls(text):
    """
    Extract unique URLs from text while preserving order.
    """

    urls = re.findall(
        r"https?://[^\s\)\]\>]+",
        text or ""
    )

    return list(dict.fromkeys(urls))

def run_final_report_agent(
    product_name,
    company_url,
    sales_analysis,
    research_analysis,
    competitor_analysis,
    strategy_leadership_analysis,
    source_urls
):
    """
    Generate the final Sales Intelligence Report
    from the outputs of the specialized agents.
    """

    # Limit upstream agent outputs to control token usage
    sales_analysis = limit_text(sales_analysis, 1800)

    research_analysis = limit_text(research_analysis, 3000)

    competitor_analysis = limit_text(competitor_analysis, 3500)

    strategy_leadership_analysis = limit_text(strategy_leadership_analysis, 5000)

    verified_sources = "\n".join(source_urls)

    
    res = final_report_chain.invoke(
        {
            "product_name": product_name,
            "company_url": company_url,
            "sales_analysis": sales_analysis,
            "research_analysis": research_analysis,
            "competitor_analysis": competitor_analysis,
            "strategy_leadership_analysis": strategy_leadership_analysis,
            "verified_sources": verified_sources,
        }
    )


    result = clean_llm_output(res)

    return result