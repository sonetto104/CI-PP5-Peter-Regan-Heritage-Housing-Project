import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.summary_page import project_summary_page
from app_pages.hypothesis_page import project_hypothesis_page
from app_pages.sale_price_analysis_page import main
# Create an instance of the app
app = MultiPage(app_name="Heritage Housing Sale Price Predictor")

# Add your app pages here using .add_page()
app.add_page("Project Summary", project_summary_page)
app.add_page("Project Hypotheses", project_hypothesis_page)
app.add_page("Sale Price Analysis", sale_price_analysis_page)

app.run()  # Run the  app
