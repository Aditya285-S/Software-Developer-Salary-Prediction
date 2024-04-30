# Software Developer Salary Prediction using Random Forest Classifier

This project aims to predict the salary of software developers based on survey data obtained from Stack Overflow. The dataset contains over 90,000 surveys with 84 features, which include information about developers' demographics, education, job preferences, and more.

## Overview

The goal of this project is to build a machine learning model that can predict the salary of software developers based on various attributes provided in the Stack Overflow Developer Survey dataset. The model is implemented using a Random Forest Classifier and deployed as a web application using Streamlit.

## Features

- **Data Preprocessing:** The project includes comprehensive data preprocessing steps such as handling missing values, encoding categorical variables, and feature scaling to prepare the dataset for modeling.

- **Model Training:** Utilizes a Random Forest Classifier to train the predictive model based on the preprocessed dataset. The model is optimized and evaluated to achieve accurate salary predictions.

- **Streamlit Web Application:** Implements a user-friendly web application using Streamlit, allowing users to input their information and receive a salary prediction from the trained machine learning model.

- **Visualization:** The project includes visualizations such as histograms, bar charts, and scatter plots to present key findings from the dataset and model predictions.


## Dataset

The dataset used in this project is sourced from Stack Overflow's annual developer survey. It can be downloaded from [Stack Overflow Annual Developer Survey](https://insights.stackoverflow.com/survey).

- **File:** `survey_results_public.csv`
- **Description:** Raw survey data containing responses from software developers of different countries.
- **Size:** Over 90,000 surveys and 84 features.
  
## Algorithm Used

In this project, we have utilized the Random Forest Classifier algorithm for building the predictive model. Random Forest is an ensemble learning method that constructs multiple decision trees during training and outputs the class that is the mode of the classes (classification) or mean prediction (regression) of the individual trees.

## Images of Visualizations

Perform Visualizations of different columns of dataset to determine the important features of dataset. Some example visualizations are:

### Developers by Age Group

![](https://github.com/Aditya285-S/Software-Developer-Salary-Prediction/blob/main/Visualizations/Develpoers%20by%20Age%20Group.png)

### Developers by Countries

![](https://github.com/Aditya285-S/Software-Developer-Salary-Prediction/blob/main/Visualizations/Develpoers%20by%20Countries.png)

### Developers by Prefered Cloud Platforms

![](https://github.com/Aditya285-S/Software-Developer-Salary-Prediction/blob/main/Visualizations/Develpoers%20by%20prefered%20Cloud%20Platforms.png)

### Developers learns from Online Platforms

![](https://github.com/Aditya285-S/Software-Developer-Salary-Prediction/blob/main/Visualizations/Develpoers%20learns%20form%20Online%20Platforms.png)


## Future Work

- Improve model performance by experimenting with different algorithms and hyperparameter tuning.
- Enhance the Streamlit application by adding more features and improving the user interface.
- Deploy the application to a cloud platform for wider accessibility.


## Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Aditya285-S/Software-Developer-Salary-Prediction.git

2. **Install Dependancies:**

   ```bash
   pip install -r requirements.txt

3.  **Run Streamlit app:**

   ```bash
   streamlit run app.py
