import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src.data_management import (
    load_house_prices_data,
    load_pkl_file,
    load_inherited_houses_data)
from src.machine_learning.evaluate_regression import regression_performance
from src.machine_learning.predictive_analysis_ui import predict_price


def predict_price_body():

    # load regression pipeline files
    version = 'v1'
    _price_pipe = load_pkl_file(
        f"outputs/ml_pipeline/predict_price/{version}/best_regressor_pipeline.pkl"
    )
    sale_price_feat_importance = plt.imread(
        f"outputs/ml_pipeline/predict_price/{version}/features_importance.png"
    )
    X_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_price/{version}/X_train.csv")
    X_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_price/{version}/X_test.csv")
    y_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_price/{version}/y_train.csv")
    y_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_price/{version}/y_test.csv")
    df_inherited_houses_data = load_inherited_houses_data()
    pipeline_regressor = load_pkl_file(
        f"outputs/ml_pipeline/predict_price/{version}/best_regressor_pipeline.pkl")
    features = (pd.read_csv(
    f"outputs/ml_pipeline/predict_price/{version}/X_train.csv").columns.to_list())

    st.write("### House Sale Price Predictor")

    st.info(
            f"The client wants to predict house prices in Ames, Iowa. "
            f"Specifically, she wants to estimate the values of her inherited "
            f"properties, in line with the second business requirement.\n\n"
        )

    st.info(
        f"The price prediction relies on five key features that you can "
        f"input below. These features were selected by our machine learning "
        f"model as the most significant for predicting the sale price. "
        f"For more details on the model and feature importance, refer to the "
        f"**ML Model** page. \n\n"
    )
    st.write("---")

    st.write("### Inherited Houses")

    st.write("---")

    st.write("### Price Prediction for the Client's Inherited Properties:")
    inherited_df = load_inherited_houses_data()
    inherited_df = inherited_df.filter(features)

    st.write("* Features of Inherited Houses")
    st.write(inherited_df)

    if st.button("Run Prediction on Inherited Homes"):
        inherited_price_prediction = predict_price(
            inherited_df, features, pipeline_regressor)
        total_value = inherited_price_prediction.sum()
        total_value = float(total_value.round(1))
        total_value = '${:,.2f}'.format(total_value)

        st.write(f"* The total value of the inherited properties is estimated"
                 f" to be:")
        st.write(f"**{total_value}**")



    st.write("#### Predicting the Sale Price of Any Property in Ames, Iowa")

    st.info(
        f"Below, you can manipulate the input of property features into the"
        f" model (within given limits) to predict the sale price of any house"
        f" in Ames, Iowa."
    )

    # Add widgets to input attributes
    X_live = DrawInputsWidgets()

    price_prediction = predict_price(X_live, features, pipeline_regressor)

    if st.button("Predict Price"):
   
        st.success(f"Predicted house price: {price_prediction}")
# Function to create the input widgets for user predictions


def DrawInputsWidgets():

    # load dataset
    df = load_house_prices_data()
    percentageMin, percentageMax = 0.4, 2.0

    # create input widgets for the five best features
    col1, col2, col3 = st.beta_columns(3)
    col4, col5, col6 = st.beta_columns(3)

    # create an empty DataFrame, which will be the live data
    X_live = pd.DataFrame([], index=[0])

    # draw the widget based on the variable
    # and set initial values
    with col1:
        feature = "OverallQual"
        st_widget = st.number_input(
            label=feature,
            min_value=1,
            max_value=10,
            value=int(df[feature].median()),
            help="Grading from 1 (Very Poor) to 10 (Very Excellent)"
        )
    X_live[feature] = st_widget

    with col2:
        feature = "GrLivArea"
        st_widget = st.number_input(
            label=feature,
            min_value=0,
            max_value=10000,
            value=int(df[feature].median()),
            help="Above grade (ground) living area in whole square feet (max 10,000 sq feet)"
        )
    X_live[feature] = st_widget

    with col3:
        feature = "YearBuilt"
        st_widget = st.number_input(
            label=feature,
            min_value=1820,
            max_value=2023,
            value=int(df[feature].median()),
            help="Original construction date (range from 1820 to 2023)"
        )
    X_live[feature] = st_widget

    with col4:
        feature = "GarageArea"
        st_widget = st.number_input(
            label=feature,
            min_value=0,
            max_value=1700,
            value=int(df[feature].median()),
            help="Size of garage in whole square feet (max of 1,700 sq feet)"
        )
    X_live[feature] = st_widget

    with col5:
        feature = "1stFlrSF"
        st_widget = st.number_input(
            label=feature,
            min_value=0,
            max_value=5000,
            value=int(df[feature].median()),
            help="First Floor area in whole square feet (max of 5,000 sq feet)"
        )
    X_live[feature] = st_widget

    return X_live
