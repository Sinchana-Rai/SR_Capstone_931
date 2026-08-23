from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser

from settings import MODEL_ID
from src.prompts.competitor_prompt import competitor_prompt
from src.utils.output_cleaner import clean_llm_output


model = ChatGroq(
    model=MODEL_ID,
    temperature=0,
    max_tokens=2000,
    reasoning_effort="none"
)

parser = StrOutputParser()

competitor_chain = competitor_prompt | model | parser


def run_competitor_agent(
    product_name,
    product_category,
    competitors,
    sales_analysis,
    research_analysis
):
    """
    Analyze competitors in the context of the prospect company.
    """

    res = competitor_chain.invoke(
        {
            "product_name": product_name,
            "product_category": product_category,
            "competitors": competitors,
            "sales_analysis": sales_analysis,
            "research_analysis": research_analysis,
        }
    )

    result = clean_llm_output(res)

    return result
