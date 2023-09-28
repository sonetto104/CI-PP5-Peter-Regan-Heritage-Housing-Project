import plotly.express as px
import numpy as np
import streamlit as st
from src.data_management import load_house_prices_data
import matplotlib.pyplot as plt
import seaborn as sns
import ppscore as pps
sns.set_style("whitegrid")


def main_sale_price_analysis():

    # load data
    df = load_house_prices_data()
    # Variables Identified in Correlation Study Notebook
    vars_strongly_correlated_to_saleprice = ['OverallQual', 'GrLivArea',
                                             'GarageArea', 'YearBuilt', '1stFlrSF', 'TotalBsmtSF', 'KitchenQual']

    st.write("### Sale Price Analysis")
    st.success(
        f"* As per the first business requirement, the client wishes to"
        f" understand the correlation between a property's attributes/features"
        f" and the sale price and requires visualisations to illustrate these"
        f" correlations. \n"
    )

    # inspect data
    if st.checkbox("Inspect Sale Price Dataset"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns. "
            f" You may inspect the first 10 rows here.")
        st.write(df.head(10))

    st.write("---")

    st.write("### Correlation Study")

    vars_strongly_correlated_to_saleprice = ['OverallQual', 'GrLivArea',
                                             'GarageArea', 'YearBuilt', '1stFlrSF', 'TotalBsmtSF', 'KitchenQual']

    # Correlation Study Summary
    st.write(
        f"A correlation study was conducted to better understand how "
        f"the variables are correlated to Sale Price. \n"
        f" Below, the results from the Pearson and Spearman correlations"
        f" are displayed in heatmaps. "
        f"Based on the results of this study,"
        f" the variables most strongly correlated to sale price are: "
        f" **{vars_strongly_correlated_to_saleprice}**"
    )

    st.info(
        f"*** Heatmap: Pearson Correlation *** \n\n"
        f"The Pearson Correlation evaluates the linear relationship between "
        f" two continuous variables. \n")

    if st.checkbox("Pearson Correlation"):
        calc_display_pearson_corr_heat(df)

    st.info(
        f"*** Heatmap: Spearman Correlation ***  \n\n"
        f"The Spearman correlation evaluates monotonic relationship. "
        f"Note this means the related variables behave similarly "
        f"but the relationship may not be linear.")

    if st.checkbox("Spearman Correlation"):
        calc_display_spearman_corr_heat(df)

        st.info(
            "The key correlations with Sale Price are as follows:\n"
            "- Sale Price tends to increase with Overall Quality (OverallQual).\n"
            "- Sale Price tends to increase with larger Groundlevel Living Area "
            "(GrLivArea).\n"
            "- Sale Price tends to increase with greater Garage Area (GarageArea)."
            "\n"
            "- Sale Price tends to increase with more Total Basement Area "
            "(TotalBsmtSF).\n"
            "- Sale Price tends to increase with newer properties (YearBuilt).\n"
            "- Sale Price tends to increase with larger 1st Floor Square Footage "
            "(1stFlrSF).\n\n"
            "The scatterplots below illustrate these correlations."
            " Note the scatterplots use darker shades of red to represent"
            " OverallQual in addition to the variable being measured on the"
            " X-axis."
        )

    # Correlation plots adapted from the Data Cleaning Notebook
    if st.checkbox("Correlation Plots of Variables vs Sale Price"):
        correlation_to_sale_price_hist_scat(
            df, vars_strongly_correlated_to_saleprice)

    st.info(
        f"*** Heatmap: Predictive Power Score (PPS) ***  \n\n"
        f"Finally, the PPS detects linear or non-linear relationships "
        f"between two variables.\n"
        f"The score ranges from 0 (no predictive power) to 1 "
        f"(perfect predictive power). \n"
        f" As we can see, Overall Quality (OverallQual) is the variable"
        f" with the highest predictive power for the Sale Price target.")

    if st.checkbox("Predictive Power Score"):
        calc_display_pps_matrix(df)


def correlation_to_sale_price_hist_scat(df, vars_to_study):
    """ Display correlation plot between variables and sale price """
    target_var = 'SalePrice'
    for col in vars_to_study:
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

        # Histogram
        sns.histplot(data=df, x=col, ax=ax1, palette='Blues')
        ax1.set_title(f"{col} Histogram", fontsize=15)

        # Scatter Plot
        sns.scatterplot(data=df, x=col, y=target_var,
                        hue='OverallQual', ax=ax2, palette='Reds')
        ax2.set_title(f"{col} vs Sale Price", fontsize=15)

        st.pyplot(fig)
        st.write("\n\n")


def calc_display_pearson_corr_heat(df):
    """ Calcuate and display Pearson Correlation """
    df_corr_pearson = df.corr(method="pearson")
    heatmap_corr(df=df_corr_pearson, threshold=0.6,
                 figsize=(12, 10), font_annot=10)


def calc_display_spearman_corr_heat(df):
    """ Calcuate and display Spearman Correlation """
    df_corr_spearman = df.corr(method="spearman")
    heatmap_corr(df=df_corr_spearman, threshold=0.6,
                 figsize=(12, 10), font_annot=10)


def calc_display_pps_matrix(df):
    """ Calcuate and display Predictive Power Score """
    pps_matrix_raw = pps.matrix(df)
    pps_matrix = pps_matrix_raw.filter(['x', 'y', 'ppscore']).pivot(
        columns='x', index='y', values='ppscore')
    heatmap_pps(df=pps_matrix, threshold=0.15, figsize=(12, 10), font_annot=10)

    pps_topscores = pps_matrix.iloc[19].sort_values(
        key=abs, ascending=False)[1:6]

    fig, axes = plt.subplots(figsize=(6, 3))
    axes = plt.bar(x=pps_topscores.index, height=pps_topscores)
    plt.xticks(rotation=90)
    plt.title("Predictive Power Score for Sale Price", fontsize=15, y=1.05)
    st.pyplot(fig)


def heatmap_corr(df, threshold, figsize=(20, 12), font_annot=8):
    """ Heatmap for correlations from CI template"""
    if len(df.columns) > 1:
        mask = np.zeros_like(df, dtype=bool)
        mask[np.triu_indices_from(mask)] = True
        mask[abs(df) < threshold] = True
        fig, axes = plt.subplots(figsize=figsize)
        axes = sns.heatmap(df, annot=True, xticklabels=True, yticklabels=True,
                           mask=mask, cmap='viridis',
                           annot_kws={"size": font_annot},
                           ax=axes, linewidth=0.5
                           )
        axes.set_yticklabels(df.columns, rotation=0)
        plt.ylim(len(df.columns), 0)
        st.pyplot(fig)


def heatmap_pps(df, threshold, figsize=(20, 12), font_annot=8):
    """ Heatmap for predictive power score from CI template"""
    if len(df.columns) > 1:
        mask = np.zeros_like(df, dtype=bool)
        mask[abs(df) < threshold] = True
        fig, axes = plt.subplots(figsize=figsize)
        axes = sns.heatmap(df, annot=True, xticklabels=True, yticklabels=True,
                           mask=mask, cmap='rocket_r',
                           annot_kws={"size": font_annot},
                           linewidth=0.05, linecolor='grey')
        plt.ylim(len(df.columns), 0)
        st.pyplot(fig)
