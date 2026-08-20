import streamlit as st
from src.workflows.sales_workflow import run_sales_workflow


st.set_page_config(
    page_title="Sales Intelligence Agent",
    layout="wide",)


st.title("Sales Intelligence Agent")

st.write(
    """
    Generate account intelligence by combining company research,
    competitive analysis, leadership insights, and product alignment.
    """
)


st.subheader("Sales Opportunity Information")


product_name = st.text_input(
    "Product Name",
    value="Snowflake Data Cloud")


company_url = st.text_input(
    "Company URL",
    value="https://www.target.com")


corporate_url = st.text_input(
    "Corporate Website",
    value="https://corporate.target.com")


product_category = st.text_input(
    "Product Category",
    value="Cloud Data Platform")


competitors = st.text_input(
    "Competitors",
    value="Databricks, Google BigQuery")


value_proposition = st.text_area(
    "Value Proposition",
    value=(
        "Helps organizations store, analyze, and share data "
        "using a scalable cloud platform."
    ))


target_customer = st.text_input(
    "Target Customer",
    value="Chief Data Officer")


generate_report = st.button(
    "Generate Intelligence Report",
    type="primary")


if generate_report:

    # Basic input validation
    if not product_name.strip():
        st.error("Please enter a Product Name.")

    elif not company_url.strip():
        st.error("Please enter a Company URL.")

    elif not corporate_url.strip():
        st.error("Please enter a Corporate Website.")

    elif not product_category.strip():
        st.error("Please enter a Product Category.")

    elif not target_customer.strip():
        st.error("Please enter a Target Customer.")

    else:

        try:

            with st.spinner(
                "Researching the company and generating "
                "the sales intelligence report..."
            ):

                result = run_sales_workflow(
                    product_name=product_name,
                    company_url=company_url,
                    corporate_url=corporate_url,
                    product_category=product_category,
                    competitors=competitors,
                    value_proposition=value_proposition,
                    target_customer=target_customer,
                )

            st.success("Sales Intelligence Report generated successfully!")

            st.divider()

            st.markdown(result["final_report"])

        except Exception as error:

            st.error("An error occurred while generating the report.")

            st.exception(error)