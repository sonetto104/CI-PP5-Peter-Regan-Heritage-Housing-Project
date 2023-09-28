import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import ppscore as pps
from src.data_management import load_house_prices_data

sns.set_style("whitegrid")


def main():
    st.set_page_config(
        page_title="Housing Sales Analysis",
        page_icon="🏡",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.title("Housing Sales Analysis Dashboard")
    st.sidebar.title("Navigation")

    page_options = [
        "Overview",
        "Correlation Study",
        "Sale Price Analysis"
    ]

    page = st.sidebar.radio("Go to", page_options)

    if page == "Overview":
        page_overview()
    elif page == "Correlation Study":
        page_correlation_study()
    elif page == "Sale Price Analysis":
        page_sale_price_analysis()


def page_overview():
    st.write("### Overview")
    st.info(
        "This dashboard provides an overview of housing sales data, including "
        "correlation analysis and insights into factors influencing sale prices."
    )
    st.write("---")

    st.write("#### Business Requirements")
    st.info(
        "- The client is interested in discovering how the house attributes "
        "correlate with the sale price.\n"
        "- The client expects data visualizations of the correlated variables "
        "against the sale price."
    )
    st.write("---")

    st.write("#### Data Inspection")
    st.info(
        "The dataset contains information about various housing features and "
        "their sale prices. Below, you can inspect the first 10 rows of the data."
    )
    df = load_house_prices_data()
    if st.checkbox("Inspect Housing Data"):
        st.write(df.head(10))
    st.write("---")

    st.write("#### Key Insights")
    st.info(
        "Some of the key insights from the analysis include:\n"
        "- Higher quality of materials and finish (OverallQual) correlates with"
        " higher sale prices.\n"
        "- Larger living areas (GrLivArea) and garage size (GarageArea) tend to"
        " result in higher sale prices.\n"
        "- Newer properties (YearBuilt) generally command higher prices.\n"
        "- First-floor square footage (1stFlrSF)"
        " influences sale prices positively."
    )


def page_correlation_study():
    st.write("### Correlation Study")
    st.info(
        "This section explores the correlation between various housing "
        "attributes and sale prices."
    )
    st.write("---")

    st.write("#### Data Inspection")
    st.info(
        "You can inspect the first 10 rows of the dataset to get an idea of"
        " the data."
    )
    df = load_house_prices_data()
    if st.checkbox("Inspect Housing Data"):
        st.write(df.head(10))
    st.write("---")

    st.write("#### Correlation Analysis")
    st.info(
        "A correlation study was conducted to better understand how the"
        " variables are correlated with sale prices. Key findings include "
        "the following attributes having strong correlations with sale prices:\n"
        "- Overall Quality (OverallQual)\n"
        "- Ground Living Area (GrLivArea)\n"
        "- Garage Area (GarageArea)\n"
        "- Year Built (YearBuilt)\n"
        "- First Floor Square Footage (1stFlrSF)"
    )
    st.write("---")

    st.write("#### Correlation Plots")
    st.info(
        "The following plots illustrate the correlation of key attributes with "
        "sale prices."
    )
    correlation_to_sale_price_plots(df)


def page_sale_price_analysis():
    st.write("### Sale Price Analysis")
    st.info(
        "This section provides an in-depth analysis of sale prices and their "
        "correlation with various housing attributes."
    )
    st.write("---")

    st.write("#### Data Inspection")
    st.info(
        "You can inspect the first 10 rows of the dataset to get an idea"
        " of the data."
    )
    df = load_house_prices_data()
    if st.checkbox("Inspect Housing Data"):
        st.write(df.head(10))
    st.write("---")

    st.write("#### Key Attributes")
    st.info(
        "The following attributes are strongly correlated with sale prices and "
        "are analyzed in detail:\n"
        "- Overall Quality (OverallQual)\n"
        "- Ground Living Area (GrLivArea)\n"
        "- Garage Area (GarageArea)\n"
        "- Year Built (YearBuilt)\n"
        "- First Floor Square Footage (1stFlrSF)"
    )
    st.write("---")

    st.write("#### Correlation Analysis")
    st.info(
        "Correlation heatmaps and bar plots are provided to visualize the "
        "relationships between the selected attributes and sale prices."
    )
    correlation_plots(df)


def correlation_to_sale_price_plots(df):
    vars_to_study = [
        'OverallQual',
        'GrLivArea',
        'GarageArea',
        'YearBuilt',
        '1stFlrSF'
    ]
    target_var = 'SalePrice'

    for col in vars_to_study:
        st.write(f"#### {col} vs. Sale Price")
        st.info(
            f"This scatterplot shows the relationship between {col} and Sale"
            f" Price. "
            f"The color represents the Overall Quality (OverallQual) of the"
            f" property."
        )
        scatter_plot(df, col, target_var)


def scatter_plot(df, col, target_var):
    fig, axes = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=df, x=col, y=target_var,
                    hue='OverallQual', palette='viridis')
    plt.title(f"{col} vs. Sale Price", fontsize=18)
    st.pyplot(fig)


def correlation_plots(df):
    st.write("#### Pearson Correlation")
    st.info(
        "The Pearson Correlation evaluates the linear relationship between two"
        " continuous variables."
    )
