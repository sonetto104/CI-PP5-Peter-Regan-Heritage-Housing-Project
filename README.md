# Heritage Housing Issues

**Predictive Analytics and Modelling Study**

**Developed by: Peter Regan**

![Mockup of Site on Different Devices](/media/amiresponsive_screenshot.png)

**Live Site:** [Live webpage](https://heritage-housing-peter-regan-f0bf9f7122d0.herokuapp.com/)

**Link to Repository:** [Repository](https://github.com/sonetto104/CI-PP5-Peter-Regan-Heritage-Housing-Project/tree/main)

## Table of Contents

- [Heritage Housing Issues](#heritage-housing-issues)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [CRISP-DM Workflow](#crisp-dm-workflow)
  - [Business Requirements](#business-requirements)
    - [Business Case Assessment](#business-case-assessment)
  - [Dataset Content](#dataset-content)
  - [Hypothesis, proposed validation and actual validation](#hypothesis-proposed-validation-and-actual-validation)
  - [Mapping the business requirements to the Data Visualisations and ML tasks](#mapping-the-business-requirements-to-the-data-visualisations-and-ml-tasks)
  - [ML Business Case](#ml-business-case)
    - [Predict Sale Price](#predict-sale-price)
  - [Dashboard Design](#dashboard-design)
    - [Page 1: Project Summary](#page-1-project-summary)
    - [Page 2: Sale Price Correlation Analysis](#page-2-sale-price-correlation-analysis)
    - [Page 3: Sale Price Prediction](#page-3-sale-price-prediction)
    - [Page 4: Hypothesis and Validation](#page-4-hypothesis-and-validation)
    - [Page 5: Machine Learning Model](#page-5-machine-learning-model)
  - [Unfixed Bugs](#unfixed-bugs)
  - [PEP8 Compliance Testing](#pep8-compliance-testing)
  - [Deployment](#deployment)
    - [Heroku](#heroku)
  - [Technologies](#technologies)
    - [Development and Deployment](#development-and-deployment)
    - [Main Data Analysis and Machine Learning](#main-data-analysis-and-machine-learning)
  - [Credits](#credits)
    - [Sources of code](#sources-of-code)
    - [Media](#media)
  - [Acknowledgements](#acknowledgements)


## Introduction

This Machine Learning Project, part of the Code Institute's Diploma in Full Stack Development, focuses on Predictive Analytics. It utilizes a Machine Learning and Data Analysis toolkit to work with a real estate dataset. The project's primary objective is to enable users to predict a property's sale value based on specific home features. Additionally, it provides insights into the correlations between various home features and their impact on the sale price.

## CRISP-DM Workflow

The project follows the CRISP-DM (Cross Industry Standard Process for Data Mining) workflow, involving a series of well-defined steps that underwent multiple iterations:

1. **Business Understanding** (Epic 1): This phase involved in-depth discussions with the client to understand their expectations and establish acceptance criteria, which are detailed in the [Business Requirements](#business-requirements) section below.

2. **Data Understanding** (Epic 2): In this step, we identify the data necessary to address the business requirements. An initial statistical analysis was conducted to assess the adequacy of the available data. This analysis was performed in the Data Cleaning Notebook.

3. **Data Preparation** (Epic 3): Data cleaning, imputation, feature engineering (including transformations and scaling), and reformatting were carried out in this phase. The goal was to ensure the data's effectiveness and accuracy for modelling. This stage was executed in the Data Cleaning and Feature Engineering Notebooks.

4. **Modelling** (Epic 4): Model algorithms were selected, and the data was divided into training and testing sets. The training sets were used to validate various algorithms and fine-tune them through hyperparameter optimization. This process was documented in the Modelling and Evaluation Notebook.

5. **Evaluation** (Epic 5): Model performance was assessed using the test set, and the results were compared against the established business acceptance criteria. This evaluation took place in the Modelling and Evaluation Notebook.

6. **Deployment** (Epic 6): The project culminated in the development of a Streamlit web application that met the business requirements defined in collaboration with the client. The app was deployed on Heroku, and the deployment process is outlined in the [Deployment](#deployment) section below.

We can also consider these stages in terms of User Stories:

**User Story 1**: 
As an end user, I would like the ability to explore how different aspects of a home relate to its sale price. This will help me understand the significance of these features in determining the home's selling price.

**User Story 2**: 
As an end user, I want to be able to estimate the probable sale price of a home based on specific characteristics. This will enable me to gauge the expected values of homes in a given area.

**User Story 3**: 
As an end user, I expect convenient online access to the necessary information. This way, I can easily access relevant data in a user-friendly manner whenever I need it.


## Business Requirements

In theory, according to the rubric applied to this project, the client has only two business requirements. However, it is worth considering all the questions presented in the business case assessment provided by Code Institute and reproduced here:

### Business Case Assessment
You have already conducted a business case assessment, so you can also use that information to build your project README file.

- What are the business requirements?
    - The client is interested in discovering how house attributes correlate with sale prices. Therefore, the client expects data visualizations of the correlated variables against the sale price.
    - The client is interested in predicting the house sale prices from her 4 inherited houses, and any other house in Ames, Iowa.<br>

- Is there any business requirement that can be answered with conventional data analysis?
    -Yes, we can use conventional data analysis to investigate how house attributes are correlated with the sale prices.

- Does the client need a dashboard or an API endpoint?
    - The client needs a dashboard

- What does the client consider as a successful project outcome?
    - A study showing the most relevant variables correlated to sale price.
      Also, a capability to predict the sale price for the 4 inherited houses, as well as any other house in Ames, Iowa.

- Can you break down the project into Epics and User Stories?
    - Information gathering and data collection.
    - Data visualization, cleaning, and preparation.
    - Model training, optimization and validation.
    - Dashboard planning, designing, and development.
    - Dashboard deployment and release.

- Ethical or Privacy concerns?
    - No. The client found a public dataset.

- Does the data suggest a particular model?
    - The data suggests a regressor where the target is the sale price.

- What are the model's inputs and intended outputs?
    - The inputs are house attribute information and the output is the predicted sale price.

- What are the criteria for the performance goal of the predictions?
    - We agreed with the client an R2 score of at least 0.75 on the train set as well as on the test set.

- How will the client benefit?
    - The client will maximize the sales price for the inherited properties.


## Dataset Content

- The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data). The business requirements are based on a fictitious, but realistic, user story described above. Predictive analytics can be applied here in a real world scenario.

- The dataset has almost 1.5 thousand rows and represents housing records from Ames, Iowa, indicating house profile (Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built, etc.) and its respective sale price for houses built between 1872 and 2010.

|Variable|Meaning|Units|
|:----|:----|:----|
|1stFlrSF|First Floor square feet|334 - 4692|
|2ndFlrSF|Second-floor square feet|0 - 2065|
|BedroomAbvGr|Bedrooms above grade (does NOT include basement bedrooms)|0 - 8|
|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Minimum Exposure; No: No Exposure; None: No Basement|
|BsmtFinType1|Rating of basement finished area|GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement|
|BsmtFinSF1|Type 1 finished square feet|0 - 5644|
|BsmtUnfSF|Unfinished square feet of basement area|0 - 2336|
|TotalBsmtSF|Total square feet of basement area|0 - 6110|
|GarageArea|Size of garage in square feet|0 - 1418|
|GarageFinish|Interior finish of the garage|Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|
|GarageYrBlt|Year garage was built|1900 - 2010|
|GrLivArea|Above grade (ground) living area square feet|334 - 5642|
|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor|
|LotArea| Lot size in square feet|1300 - 215245|
|LotFrontage| Linear feet of street connected to property|21 - 313|
|MasVnrArea|Masonry veneer area in square feet|0 - 1600|
|EnclosedPorch|Enclosed porch area in square feet|0 - 286|
|OpenPorchSF|Open porch area in square feet|0 - 547|
|OverallCond|Rates the overall condition of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|OverallQual|Rates the overall material and finish of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|WoodDeckSF|Wood deck area in square feet|0 - 736|
|YearBuilt|Original construction date|1872 - 2010|
|YearRemodAdd|Remodel date (same as construction date if no remodelling or additions)|1950 - 2010|
|SalePrice|Sale Price|34900 - 755000|





