import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.summary_page import project_summary_page
from app_pages.hypothesis_page import project_hypothesis_page
from app_pages.sale_price_analysis_page import main_sale_price_analysis
from app_pages.price_prediction_ml_page import price_prediction_ml_page_body
# Create an instance of the app
app = MultiPage(app_name="Heritage Housing Sale Price Predictor")

# Add your app pages here using .add_page()
app.add_page("Project Summary", project_summary_page)
app.add_page("Project Hypotheses", project_hypothesis_page)
app.add_page("Sale Price Analysis", main_sale_price_analysis)
app.add_page("ML Model", price_prediction_ml_page_body)

app.run()  # Run the  app
