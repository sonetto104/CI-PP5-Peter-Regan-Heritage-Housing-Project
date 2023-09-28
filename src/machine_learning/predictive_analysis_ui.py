import streamlit as st
import pandas as pd

# Function to predict house prices using the regression pipeline
def predict_house_price(X_live, house_features, price_pipeline):

    # From live data, subset features related to this pipeline
    X_live_price = X_live.filter(house_features)

    # Predict
    price_prediction = price_pipeline.predict(X_live_price)

    return price_prediction

# Function to predict inherited house prices using the regression pipeline
def predict_inherited_house_price(X_inherited, house_features, price_pipeline):

    # From inherited houses data, subset features related to this pipeline
    X_inherited_price = X_inherited.filter(house_features)

    # Predict
    price_prediction_inherited = price_pipeline.predict(X_inherited_price)

    return price_prediction_inherited

# Function to display and format the predicted price
def display_predicted_price(price_prediction, is_inherited=False):

    if not is_inherited:
        st.write("Predicted House Price:")
    else:
        st.write("Predicted Inherited House Price:")

    # Format the value as currency with two decimal places
    formatted_price = '${:,.2f}'.format(price_prediction[0])

    st.write(f"**{formatted_price}**")

# Main Streamlit app
def main():
    st.title("House Price Prediction")

    # Load the regression pipelines and input data
    price_pipeline = load_price_pipeline()  # Implement a function to load the pipeline
    X_live = load_live_data()  # Implement a function to load live data
    X_inherited = load_inherited_data()  # Implement a function to load inherited data

    # Sidebar selection
    option = st.sidebar.selectbox("Select Prediction Type", ["Live House Price", "Inherited House Price"])

    if option == "Live House Price":
        st.sidebar.header("Live House Features")
        house_features = select_live_features()  # Implement a function to select features
        prediction = predict_house_price(X_live, house_features, price_pipeline)
        display_predicted_price(prediction)
    else:
        st.sidebar.header("Inherited House Features")
        house_features = select_inherited_features()  # Implement a function to select features
        prediction = predict_inherited_house_price(X_inherited, house_features, price_pipeline)
        display_predicted_price(prediction, is_inherited=True)

if __name__ == "__main__":
    main()

# Function to predict house prices using the regression pipeline


def predict_house_price(X_live, house_features, price_pipeline):
    # From live data, subset features related to this pipeline
    X_live_price = X_live.filter(house_features)

    # Predict
    price_prediction = price_pipeline.predict(X_live_price)

    return price_prediction

# Function to predict inherited house prices using the regression pipeline


def predict_inherited_house_price(X_inherited, house_features, price_pipeline):
    # From inherited houses data, subset features related to this pipeline
    X_inherited_price = X_inherited.filter(house_features)

    # Predict
    price_prediction_inherited = price_pipeline.predict(X_inherited_price)

    return price_prediction_inherited

# Function to display and format the predicted price


def display_predicted_price(price_prediction, is_inherited=False):
    if not is_inherited:
        st.write("Predicted House Price:")
    else:
        st.write("Predicted Inherited House Price:")

    # Format the value as currency with two decimal places
    formatted_price = '${:,.2f}'.format(price_prediction[0])

    st.write(f"**{formatted_price}**")

# Main Streamlit app


def main():
    st.title("House Price Prediction")

    # Load the regression pipelines and input data
    price_pipeline = load_price_pipeline()  # Load the pipeline
    X_live = load_live_data()  # Load live data
    X_inherited = load_inherited_data()  # Load inherited data

    # Sidebar selection
    option = st.sidebar.selectbox("Select Prediction Type",
                                  ["Live House Price", "Inherited House Price"])

    if option == "Live House Price":
        st.sidebar.header("Live House Features")
        house_features = select_live_features()  # Select features
        prediction = predict_house_price(
            X_live, house_features, price_pipeline)
        display_predicted_price(prediction)
    else:
        st.sidebar.header("Inherited House Features")
        house_features = select_inherited_features()  # Select features
        prediction = predict_inherited_house_price(
            X_inherited, house_features, price_pipeline)
        display_predicted_price(prediction, is_inherited=True)


if __name__ == "__main__":
    main()
