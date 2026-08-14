from langchain_groq import ChatGroq
from settings import MODEL_ID
from langchain_core.output_parsers import StrOutputParser
from src.prompts.sales_prompt import sales_prompt


# Create the Groq model
model = ChatGroq(model=MODEL_ID, temperature=0)

# Convert the AI response into normal text
parser = StrOutputParser()

# Create the Sales Agent chain
sales_chain = sales_prompt | model | parser


def run_sales_agent(product_name, company_url, product_category,
    competitors, value_proposition, target_customer):
    """
    Run the Sales Intake Agent and return the analysis.
    """

    result = sales_chain.invoke(
        {
            "product_name": product_name,
            "company_url": company_url,
            "product_category": product_category,
            "competitors": competitors,
            "value_proposition": value_proposition,
            "target_customer": target_customer,
        }
    )

    return result