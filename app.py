import streamlit as st
from src.workflows.sales_workflow import run_sales_workflow
from urllib.parse import urlparse

def is_valid_url(url):
    """
    Check whether a URL contains both a valid scheme
    and network location.
    """
    try:
        result = urlparse(url)

        return (result.scheme in ["http", "https"] and bool(result.netloc))

    except ValueError:
        return False
    

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

    if not product_name.strip():

        st.error(
            "Please enter a Product Name."
        )

    elif not company_url.strip():

        st.error(
            "Please enter a Company URL."
        )

    elif not is_valid_url(company_url):

        st.error(
            "Please enter a valid Company URL "
            "starting with http:// or https://."
        )

    elif not corporate_url.strip():

        st.error(
            "Please enter a Corporate Website."
        )

    elif not is_valid_url(corporate_url):

        st.error(
            "Please enter a valid Corporate Website URL "
            "starting with http:// or https://."
        )

    elif not product_category.strip():

        st.error(
            "Please enter a Product Category."
        )

    elif not value_proposition.strip():

        st.error(
            "Please enter a Value Proposition."
        )

    elif not target_customer.strip():

        st.error(
            "Please enter a Target Customer."
        )

    else:

        try:

            with st.spinner(
                "Researching company data and generating "
                "the intelligence report..."
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

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Product", product_name)

            with col2:
                st.metric("Product Category", product_category)

            with col3:
                st.metric("Target Customer", target_customer)

            st.divider()

            st.markdown(result["final_report"])

            st.download_button(
                label="Download Report",
                data=result["final_report"],
                file_name="sales_intelligence_report.md",
                mime="text/markdown",
            )

            # st.divider()

            # with st.expander("View Individual Agent Outputs"):

            #     st.subheader("Sales Agent")
            #     st.markdown(result["sales_analysis"])

            #     st.divider()

            #     st.subheader("Company Research Agent")

            #     st.markdown(result["research_analysis"])

            #     st.divider()

            #     st.subheader("Competitor Analysis Agent")

            #     st.markdown(result["competitor_analysis"])

            #     st.divider()

            #     st.subheader("Strategy & Leadership Agent")

            #     st.markdown(result["strategy_leadership_analysis"])

            # with st.expander("Research Statistics"):

            #     st.write(
            #         f"Company website characters processed: "
            #         f"{len(result['website_text'])}"
            #     )

            #     st.write(
            #         f"Corporate research characters processed: "
            #         f"{len(result['corporate_source_data'])}"
            #     )

        except Exception as error:

            st.error(
                "The report could not be generated."
            )

            st.write(
                "Please verify the website URLs and try again."
            )

            with st.expander(
                "Technical Error Details"
            ):

                st.exception(error)