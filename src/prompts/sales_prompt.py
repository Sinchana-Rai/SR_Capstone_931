from langchain_core.prompts import ChatPromptTemplate


sales_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a Sales Intake Agent.

Your role is to analyze information provided by a sales representative
about a prospective customer.

Your job is to understand:
- what product is being sold
- what type of company is being targeted
- the product category
- the product value proposition
- the target customer
- known competitors

Do not perform web research.
Do not make a final sales recommendation.
Do not invent missing information.

Only analyze the information provided by the user.

Return your response using these sections:

1. Product
2. Product Category
3. Prospect Company
4. Value Proposition
5. Target Customer
6. Competitors
7. Sales Objective
8. Missing Information
"""
        ),
    (
            "human",
            """
Product Name:
{product_name}

Company URL:
{company_url}

Product Category:
{product_category}

Competitors:
{competitors}

Value Proposition:
{value_proposition}

Target Customer:
{target_customer}
"""
        ),
    ]
)



if __name__ == "__main__":

    test_prompt = sales_prompt.invoke(
        {
            "product_name": "Snowflake Data Cloud",
            "company_url": "https://www.target.com",
            "product_category": "Cloud Data Platform",
            "competitors": "Databricks, Google BigQuery",
            "value_proposition": "Helps organizations store, analyze, and share data using a scalable cloud platform.",
            "target_customer": "Chief Data Officer",
        }
    )

    print(test_prompt)