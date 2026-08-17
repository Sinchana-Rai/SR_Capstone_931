from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser

from src.utils.output_cleaner import clean_llm_output

from settings import MODEL_ID
from src.prompts.research_prompt import research_prompt

# Create Groq model
model = ChatGroq(model=MODEL_ID, temperature=0)

#convert the model respons into normal text
parser = StrOutputParser()

#build research agent chain
research_chain = research_prompt | model | parser

def run_research_agent(product_name, product_category, company_url, website_text):
    """
    Analyze website information about a prospect company.
    """

    res = research_chain.invoke(
        {
            "product_name": product_name,
            "product_category": product_category,
            "company_url": company_url,
            "website_text": website_text,
        })

    result = clean_llm_output(res)

    return result
