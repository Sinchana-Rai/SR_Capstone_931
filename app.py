import streamlit as st


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

    st.success("Input received successfully!")

    st.subheader("Opportunity Summary")

    st.write(f"**Product:** {product_name}")
    st.write(f"**Company:** {company_url}")
    st.write(f"**Corporate Website:** {corporate_url}")
    st.write(f"**Category:** {product_category}")
    st.write(f"**Competitors:** {competitors}")
    st.write(f"**Target Customer:** {target_customer}")
    st.write(f"**Value Proposition:** {value_proposition}")