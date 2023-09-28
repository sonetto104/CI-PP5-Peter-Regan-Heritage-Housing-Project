import streamlit as st


def project_hypothesis_page():
    st.write("### Project Hypotheses and Validation")

    st.success(
        f"**Hypothesis 1:**\n"
        f"The size of the house is positively correlated with the sale price."
        f"This is likely to be reflected in features like GrLiveArea (ground"
        f" living space), GarageArea and 1stFlrSF among others. Larger houses"
        f" will tend to have a higher sale price."
    )

    st.success(
        f"**Hypothesis 2:**\n"
        f"The quality and condition of the property, reflected in features such"
        f" as OverallQual, are positively correlated with the sale price."
        f" Properties of higher quality tend to have a higher sale price."
    )

    st.success(
        f"**Hypothesis 3:**\n"
        f"The age of a house, as represented by YearBuilt, is negatively"
        f" correlated with the sale price. Older houses tend to have lower sale"
        f" prices."
    )

    
    st.success(
        f"Our correlation analysis supports our hypotheses:"
        f"\n\n"
        f"1. Strong positive relationships between Overall Quality"
        f" (OverallQual), Ground Living Area (GrLivArea) and SalePrice were"
        f" observed,"
        f" indicating that houses of higher quality and larger living areas"
        f" generally result in higher sale prices."
        f"\n\n"
        f"2. The study revealed a similar strong positive"
        f" relationship between 1st Floor Square Footage (1stFlrSF) and Sale"
        f"Price, further confirming that larger houses tend to have higher"
        f" sale prices.\n\n"
        f"3. A negative correlation was observed between YearBuilt and"
        f" SalePrice, supporting the hypothesis that older houses tend to have"
        f" lower sale prices."
        f"\n\n"
        f"These findings support our hypotheses, suggesting that house size,"
        f" quality and age significantly impact the sale price."
    )
