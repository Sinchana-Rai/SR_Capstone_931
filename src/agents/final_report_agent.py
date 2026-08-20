from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser

from settings import MODEL_ID
from src.prompts.final_report_prompt import final_report_prompt
from src.utils.output_cleaner import clean_llm_output


model = ChatGroq(
    model=MODEL_ID,
    temperature=0,
    max_tokens=2500,
    reasoning_effort="none"
)

parser = StrOutputParser()

final_report_chain = (final_report_prompt | model | parser)


def run_final_report_agent(product_name, company_url, sales_analysis, research_analysis, competitor_analysis, strategy_leadership_analysis):
    res = final_report_chain.invoke(
        {
            "product_name": product_name,
            "company_url": company_url,
            "sales_analysis": sales_analysis,
            "research_analysis": research_analysis,
            "competitor_analysis": competitor_analysis,
            "strategy_leadership_analysis": strategy_leadership_analysis,
        }
    )

    return clean_llm_output(res)