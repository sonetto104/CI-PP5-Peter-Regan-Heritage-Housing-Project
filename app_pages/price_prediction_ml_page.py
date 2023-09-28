import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_house_prices_data, load_pkl_file
from src.machine_learning.evaluate_regression import (
    regression_performance,
    regression_evaluation,
    regression_evaluation_plots)


def price_prediction_ml_page_body():

    # Load regression pipeline files
    version = 'v1'
    predict_price_pipeline = load_pkl_file(
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

    st.write("### ML Pipeline: Predict Property Sale Price")
    # Display pipeline training summary conclusions
    st.success(
        f"A Regressor model was trained to predict the sale price of"
        f" properties in Ames, Iowa. "
        f"The initial data set contained 23 features and 'SalePrice' as "
        f"the target."
        f" Two features were dropped due to around 90% of data points missing."
        f" Feature engineering was carried out on the remaining data. "
        f"The model was then tuned using a hyperparameter search and was "
        f"found to "
        f"**meet the business requirement** with an R2 Score of 0.75 or "
        f"better on "
        f"both train and test sets. The model identified the five most "
        f"important features necessary to achieve the best predictive "
        f"power."
    )
    st.write("---")

    # Show pipeline steps
    st.write("### ML pipeline to predict property sale prices.")
    st.code(predict_price_pipeline)
    st.write("---")

    # Show best features
    st.write("### The features the model was trained on.")
    st.write("The model was trained on the following features:")
    st.write("1. Overall Quality (OverallQual)")
    st.write("2. Garage Area (GarageArea)")
    st.write("3. Year Built (YearBuilt)")
    st.write("4. 1st Floor Area (1stFlrSF)")
    st.write("5. Ground Level Living Area (GrLivArea)")

    st.image(sale_price_feat_importance)

    st.write(
        f"These features were chosen because of their significance in" 
        f" predicting property sale prices."
    )
    st.write("---")

    # Evaluate performance on both sets
    st.write("### Pipeline Performance")
    regression_performance(X_train=X_train, y_train=y_train,
                           X_test=X_test, y_test=y_test,
                           pipeline=sale_price_pipe)

    st.write("**Performance Plot**")
    regression_evaluation_plots(X_train=X_train, y_train=y_train,
                                X_test=X_test,
                                y_test=y_test, pipeline=sale_price_pipe,
                                alpha_scatter=0.5)
