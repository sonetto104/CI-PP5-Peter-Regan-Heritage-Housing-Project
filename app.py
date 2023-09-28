import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.summary_page import project_summary_page

# Create an instance of the app
app = MultiPage(app_name="Heritage Housing Sale Price Predictor")

# Add your app pages here using .add_page()
app.add_page("Project Summary", project_summary_page)

app.run()  # Run the  app
