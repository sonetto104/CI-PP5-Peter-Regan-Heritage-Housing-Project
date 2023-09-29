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
  - [Project Hypotheses and Validation](#project-hypotheses-and-validation)
  - [Mapping Business Requirements to Data Visualisations and ML Tasks](#mapping-business-requirements-to-data-visualisations-and-ml-tasks)
  - [ML Business Case](#ml-business-case)
    - [Predict Sale Price](#predict-sale-price)
  - [Dashboard Design](#dashboard-design)
    - [Page 1: Project Summary](#page-1-project-summary)
    - [Page 2: Sale Price Correlation Analysis](#page-2-sale-price-correlation-analysis)
    - [Page 3: Sale Price Prediction](#page-3-sale-price-prediction)
    - [Page 4: Hypotheses and Validation](#page-4-hypotheses-and-validation)
    - [Page 5: Machine Learning Model](#page-5-machine-learning-model)
  - [Unfixed Bugs](#unfixed-bugs)
  - [Deployment](#deployment)
    - [Heroku](#heroku)
  - [Technologies](#technologies)
    - [Development Tools and Environment](#development-tools-and-environment)
    - [Data Analysis and Profiling](#data-analysis-and-profiling)
    - [Data Visualisation](#data-visualisation)
    - [Data Preparation and Feature Engineering](#data-preparation-and-feature-engineering)
    - [Machine Learning and Modelling](#machine-learning-and-modelling)
  - [Credits](#credits)
    - [Code Sources](#code-sources)


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
    - Yes, we can use conventional data analysis to investigate how house attributes are correlated with the sale prices.

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

## Project Hypotheses and Validation

In this project, we formulated and validated the following hypotheses:

### Hypothesis 1: House Size and Sale Price

We hypothesized that the size of a house is positively correlated with the sale price. This correlation is likely to be reflected in features such as `GrLivArea` (ground living space), `GarageArea`, and `1stFlrSF`, among others. Larger houses are expected to have higher sale prices.

### Hypothesis 2: Property Quality and Sale Price

Our second hypothesis proposed that the quality and condition of the property, represented by features like `OverallQual`, are positively correlated with the sale price. Higher-quality properties are anticipated to command higher sale prices.

### Hypothesis 3: House Age and Sale Price

The third hypothesis suggested a negative correlation between the age of a house, as represented by `YearBuilt`, and the sale price. Older houses are expected to have lower sale prices.

Our correlation analysis supported these hypotheses:

- We observed strong positive relationships between `Overall Quality (OverallQual)`, `Ground Living Area (GrLivArea)`, and `SalePrice`, indicating that houses of higher quality and larger living areas generally result in higher sale prices.

- The study revealed a similar strong positive relationship between `1st Floor Square Footage (1stFlrSF)` and `SalePrice`, further confirming that larger houses tend to have higher sale prices.

- A negative correlation was observed between `YearBuilt` and `SalePrice`, supporting the hypothesis that older houses tend to have lower sale prices.

These findings support our hypotheses, suggesting that house size, quality, and age significantly impact the sale price.

## Mapping Business Requirements to Data Visualisations and ML Tasks

**Business Requirement 1: Data Exploration and Correlation Analysis**
- Our initial objective was to delve into the dataset, specifically focusing on property sale prices in Ames, Iowa.
- We conducted comprehensive correlation studies, employing both Pearson and Spearman methods, to gain a deeper understanding of how various variables related to sale prices.
- Furthermore, we created visually informative plots to illustrate key insights derived from the data.

**Business Requirement 2: Regression Modelling and Data Analysis**
- Our primary goal was to predict the sale prices of homes in Ames, Iowa. To achieve this, we constructed a regression model with sale price as the target variable.
- Rigorous optimisation and evaluation steps were carried out to attain an R-squared (R2) value of 0.75 or higher, indicating the model's effectiveness.

**Business Requirement 3: Online Application Development and Deployment**
- We developed a user-friendly web application using Streamlit, offering comprehensive data analysis, visualization, and a prediction feature for property sale prices in Ames, Iowa.
- Subsequently, the application was deployed on the Heroku platform, ensuring online accessibility for the client and other users.

## ML Business Case

### Predicting House Sale Prices with Machine Learning

- Our objective is to develop an ML model capable of predicting the sale price, in dollars, for homes in Ames, Iowa. This task falls under regression, a supervised and uni-dimensional modeling approach.
- The ultimate goal is to provide our client with a reliable tool for predicting the sale price of specific properties in Ames, Iowa, including the inherited properties of particular concern to the client.
- The success criteria for our model include:
  - Achieving an R2 score of at least 0.75 on both the training and test datasets.
  - The model is considered a failure if: after 12 months of usage, the model predictions are 50% off more than 30% of the time, and/or the R2 score is less than 0.75.

- The model's output is a continuous value representing the sale price in dollars. This web application is designed to be accessible to private homeowners and clients, allowing them to input their property details and obtain a sale price estimate. Real estate agents can also benefit by using the app to quickly provide estimates to prospective clients during live interactions. **However, note it is only applicable for homes in Ames, Iowa**.
- The training dataset is sourced from a public dataset containing approximately 1,500 property sales records. It consists of a single target feature, the sale price, while the remaining 23 variables are considered features for prediction.

## Dashboard Design

The project was built using Streamlit and satisfies the client's requirement for visualisations of the data analysis. It contains the following pages:

## Page 1: Project Summary

On this page, you'll find:

- A clear statement of the project's purpose and objectives.
- Explanations of some project-specific terms and jargon.
- A concise overview of the dataset being used in the project.
- A detailed description of the project's business requirements.
- A link to this README if the client desires further context.
<details>
<summary>Project Summary Page Screenshot</summary>
<img src="/media/project_summary_page.png">
</details>

## Page 2: Sale Price Correlation Analysis

This page addresses the project's first business requirement and offers the client the option to visualise various aspects of the dataset. It includes:

- A sample representation of data from the dataset to provide an initial glimpse.
- Pearson and Spearman correlation plots, highlighting relationships between dataset features and sale prices.
- Histograms and scatterplots showcasing the most influential predictive features.
- An analysis using Predictive Power Score (PPS) to assess feature predictability.
<details>
<summary>Sale Price Analysis Page Screenshots</summary>
<img src="/media/sale_analysis_dataset.png">
<img src="/media/sale_analysis_pearson.png">
<img src="/media/sale_analysis_spearman.png">
<img src="/media/sale_analysis_plots.png">
<img src="/media/sale_analysis_pps.png">
</details>

## Page 3: Sale Price Prediction

This page fulfills the second Business Requirement and provides a tool for predicting sale prices. It features:

- Input fields where users can enter property attributes to generate a sale price prediction.
- A specific functionality to predict sale prices for the client's inherited properties based on her input data.
<details>
<summary>Price Predictor Page Screenshots</summary>
<img src="/media/price_predictor_one.png">
<img src="/media/price_predictor_two.png">
</details>

## Page 4: Hypotheses and Validation

On this page, you'll find a comprehensive list of the project's hypotheses and a detailed account of how each hypothesis was tested and validated.
<details>
<summary>Sale Price Analysis Page Screenshots</summary>
<img src="/media/hypothesis_and_validation_page.png">
</details>

## Page 5: Machine Learning Model

This page offers insights into the Machine Learning (ML) model used in the project, including:

- An overview of the ML pipeline employed for training and prediction.
- A demonstration of feature importance to highlight key predictors.
- A review of the performance metrics and results achieved by the ML model.
<details>
<summary>ML Model Page Screenshots</summary>
<img src="/media/ml_pipeline_overview.png">
<img src="/media/feature_importance_plot.png">
<img src="/media/test_set_performance.png">
<img src="/media/train_set_performance.png">
</details>

## Unfixed Bugs

As per current knowledge, there are no unfixed bugs in the app. There are some instances where some lines of code are slightly longer than 79 characters but not significantly. Oddly, "from src.data_management" is registering as an error in the CodeAnywhere IDE, but not on Gitpod. It does not effect the performance of the app at all, but it is something to be explored. 

## Deployment

### Heroku

- The App live link is: <https://heritage-housing-peter-regan-f0bf9f7122d0.herokuapp.com/>
- Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
- The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App.
2. At the Deploy tab, select GitHub as the deployment method.
3. Make sure your app is using Heroku Stack-20 by following these steps:
    - In Heroku click on Account Settings (under the avatar menu) on the Heroku Dashboard.
    - Scroll down to the API Key section and click Reveal. Copy the key.
    - Back in your IDE workspace, enter the following command in the terminal: heroku login -i , and enter your email then API key that you copied when prompted.
    - Then use the command heroku stack:set heroku-20 -a <the_name_of_your_app>
    - Now deploy again in the Heroku app
4. Select your repository name and click Search. Once it is found, click Connect.
5. Select the branch you want to deploy, then click Deploy Branch.
6. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
7. If the slug size is too large then add large files not required for the app to the .slugignore file.

## Technologies

This section contains information on resources and technologies used to complete this project.

### Development Tools and Environment

- **Version Control**: [GitHub](https://github.com/)
- **Development Environment**: [Code Anywhere](https://codeanywhere.com/)
- **Data Access**: [Kaggle](https://www.kaggle.com/)
- **Deployment**: [Heroku](https://www.heroku.com/)
- **Development Notebooks**: [Jupyter Notebooks](https://jupyter.org/)

### Data Analysis and Profiling

- **Data Manipulation**: [NumPy](https://numpy.org/), [Pandas](https://pandas.pydata.org/)
- **Data Profiling**: [ydata_profiling](https://ydata-profiling.ydata.ai/docs/master/index.html)
- **Predictive Power Analysis**: [PPScore](https://pypi.org/project/ppscore/)

### Data Visualisation

- **Visualisation Libraries**: [Matplotlib](https://matplotlib.org/), [Seaborn](https://seaborn.pydata.org/)

### Data Preparation and Feature Engineering

- **Data Cleaning and Preparation**: [Feature Engine](https://feature-engine.trainindata.com/en/latest/index.html)

### Machine Learning and Modelling

- **Machine Learning Toolkit**: [SciKit Learn](https://scikit-learn.org/stable/)
- **Ensemble Learning**: [XGBoost](https://xgboost.readthedocs.io/en/stable/)
- **Regression Modeling**: [XGBoostRegressor](https://xgboost.readthedocs.io/en/stable/)
- **Model Evaluation**: [r2_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html)

### App Development

- **App Interface**: [Streamlit](https://streamlit.io/)


## Credits

### Code Sources 

- Various functions and classes used in the development process, including HyperparameterOptimizationSearch, Feature Importance analysis, evaluation of train and test sets, PPS and Correlation Analysis, Missing Data Evaluation, and Data Cleaning Effect, were sourced from both the Code Institute's Churnometer Walkthrough Project and the Code Institute course content. These components played a significant role in the Jupyter Notebooks during the project's development.

- Additionally, the Steamlit pages used in this project were originally derived from the CI Churnometer Walkthrough Project and were subsequently customized and adapted to create the app deployed in this project.

I thank my fellow students at Code Institute Ulrike Riemenschneider, Chris Cherng, Corentin Vidick and Toby Hullis whose projects were very helpful in showing me the way during the moments I inevitably became stuck.
Their repos can be found here:
- [Ulrike Riemenschneider's Heritage Housing Project](https://github.com/URiem/heritage-housing-PP5)
- [Chris Cherng's Heritage Housing Project](https://github.com/ChrisCherng/heritage-housing)
- [Corentin Vidick's Heritage Housing Project](https://github.com/Corentin-Vidick/P5-heritage-housing-issues)
- [Toby Hullis's Heritage Housing Project](https://github.com/t-hullis/milestone-project-heritage-housing-issues)







