import streamlit as st
from Options import countries, job_types, education
from cleaner import experience, workexp, country_map, age_range
from mapper import map_edu_lev, map_years_code, map_country, map_work_exp, map_age, map_job_type
from model import prediction

# Set page title and configuration
st.set_page_config(page_title="Software Developer Salary Prediction")

def main():
    # Define custom CSS styles for the app
    css = """
    <style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f9f9f9;
        color: #333333;
    }
    .container {
        max-width: 800px;
        padding: 20px;
        margin: auto;
        background-color: #ffffff;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    }
    .title-box {
        padding: 15px;
        background-color: #0072b5;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 30px;
    }
    .title-text {
        color: black;
        font-size: 30px;
        font-weight: bold;
        text-transform: uppercase;
        text-align: center;
    }
    .input-section {
        margin-bottom: 20px;
    }
    .input-label {
        font-weight: bold;
        margin-bottom: 10px;
    }
    .input-widget {
        width: 100%;
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #ccc;
    }
    </style>
    """

    st.markdown(css, unsafe_allow_html=True)
    st.markdown("<div class='title-box'><h2 class='title-text'>Software Developer Salary Prediction</h2></div>", unsafe_allow_html=True)

    st.header("Personal Information")
    age = st.slider("Enter your Age", 15, 80)

    st.header("Location Information")
    country = st.selectbox("Enter your Country", countries)

    st.header("Employment Information")
    job_type = st.selectbox("Job Type", job_types)
    education_lev = st.selectbox("Education Level", education)
    years_code = st.number_input("Years of Coding Experience", min_value=0, max_value=70, step=1)
    years_exp = st.number_input("Years of Overall Experience", min_value=0, max_value=50, step=1)

    button_clicked = st.button("### Predict Salary")

    if button_clicked:
        if years_code == 0:
            st.error("### Please, fill the details!!")
        else:
            age = age_range(age)
            age = map_age(age)

            country = country_map(country)
            country = map_country(country)

            job_type = map_job_type(job_type)

            edu_lev = map_edu_lev(education_lev)

            years_code = workexp(years_code)
            years_code = map_years_code(years_code)

            years_exp = experience(years_exp)
            years_exp = map_work_exp(years_exp)

            salary = prediction(edu_lev, years_code, age, job_type, country, years_exp)
            st.success(f"## The Predicted Salary : ${salary:.2f}")