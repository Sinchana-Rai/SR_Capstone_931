from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser

from settings import MODEL_ID
from src.prompts.strategy_leadership_prompt import (
    strategy_leadership_prompt
)
from src.utils.output_cleaner import clean_llm_output


model = ChatGroq(
    model=MODEL_ID,
    temperature=0,
    max_tokens=5000
)


parser = StrOutputParser()


strategy_leadership_chain = (strategy_leadership_prompt | model | parser)


def run_strategy_leadership_agent(product_name, product_category, target_customer, company_url, source_data):
    """
    Analyze company strategy and leadership information
    from public source data.
    """

    res = strategy_leadership_chain.invoke(
        {
            "product_name": product_name,
            "product_category": product_category,
            "target_customer": target_customer,
            "company_url": company_url,
            "source_data": source_data,
        }
    )

    result = clean_llm_output(res)

    return result