import streamlit as st


def project_summary_page():
    st.write("### Project Summary")

    st.info(
        f"**Project Purpose**\n\n"
        f"This project aims to predict property sale prices in Ames, Iowa. "
        f"We'll use a dataset to build a machine learning model that estimates "
        f"the sale prices, including inherited properties."
    )

    st.info(
        f"**Terminology**\n\n"
        f"* A **client** is someone using this tool.\n"
        f"* **Sale price** is a property's estimated value in a typical sale.\n"
        f"* The **target variable** is the sale price we want to predict."
    )

    st.info(
        f"**Dataset Summary**\n\n"
        f"The dataset records house features (e.g., Floor Area, Basement) "
        f"and sale prices for Ames, Iowa properties built from 1872 to 2010."
        f"* It contains about 1500 sales records.\n"
        f"* The data source is"
        f"[Kaggle](https://www.kaggle.com/datasets/codeinstitute/housing-prices-data)."
    )

    st.success(
        f"**Business Requirements**\n\n"
        f"We have two key business requirements:\n"
        f"* **Requirement 1:** The client is interested in understanding how "
        f"the house attributes correlate with the sale price. Therefore, the "
        f"client expects data visualisations of the correlated variables "
        f"against the sale prices for illustration.\n"
        f"* **Requirement 2:** The client is interested in predicting the "
        f"potential sale prices for properties in Ames, Iowa. Specifically, "
        f"she wants to determine potential values for the properties she "
        f"inherited.\n"
    )

    st.write(
        f"For more details, including data variable descriptions, see the "
        f"[Project README](https://github.com/sonetto104/CI-PP5-Peter-Regan-Heritage-Housing-Project#readme)."
    )