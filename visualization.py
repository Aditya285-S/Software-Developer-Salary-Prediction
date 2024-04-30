import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def shorten_categories(categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = 'Other'
    return categorical_map


def clean_experience(x):
    if x ==  'More than 50 years':
        return 'More than 50 years'
    elif x == 'Less than 1 year':
        return 'Less than 1 year'
    elif int(x)>=2 and int(x)<=5:
        return '2-5'
    elif int(x)>=6 and int(x)<=10:
        return '6-10'
    elif int(x)>=11 and int(x)<=15:
        return '11-15'
    elif int(x)>=16 and int(x)<=20:
        return '16-20'
    elif int(x)>=21 and int(x)<=30:
        return '21-30'
    elif int(x)>=31 and int(x)<=40:
        return '31-40'
    elif int(x)>=41 and int(x)<=50:
        return '41-50'
    else:
        return str(x)
    
def clean_workexp(x):
    if int(x) ==  1:
        return '1'
    elif int(x)>=2 and int(x)<=5:
        return '2-5'
    elif int(x)>=6 and int(x)<=10:
        return '6-10'
    elif int(x)>=11 and int(x)<=15:
        return '11-15'
    elif int(x)>=16 and int(x)<=20:
        return '16-20'
    elif int(x)>=21 and int(x)<=30:
        return '21-30'
    elif int(x)>=31 and int(x)<=40:
        return '31-40'
    elif int(x)>=41 and int(x)<=50:
        return '41-50'
    else:
        return str(x)


def clean_education(x):
    if 'Bachelor’s degree' in x:
        return 'Bachelor’s degree'
    if 'Master’s degree' in x:
        return 'Master’s degree'
    if 'Professional degree' in x or 'Other doctoral' in x:
        return 'Post grad'
    return 'Less than a Bachelors'


@st.cache
def load_data():
    df = pd.read_csv("Notebook\survey_results_public.csv")
    df = df[["EdLevel", "YearsCodePro", "Age", "DevType", "Country", 'WorkExp', "ConvertedCompYearly"]]
    df = df.rename({"ConvertedCompYearly": "Salary"}, axis=1)
    df = df.dropna()

    country_map = shorten_categories(df.Country.value_counts(), 400)
    df["Country"] = df["Country"].map(country_map)
    df = df[df["Salary"] <= 250000]
    df = df[df["Salary"] >= 10000]

    df["YearsCodePro"] = df["YearsCodePro"].apply(clean_experience)
    df['WorkExp'] = df['WorkExp'].apply(clean_workexp)
    df["EdLevel"] = df["EdLevel"].apply(clean_education)
    return df

df = load_data()

def show_explore_page():
    st.markdown("""
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
    """, unsafe_allow_html=True)


    st.markdown('<div class="title-box"><div class="title-text">Software Developer Survey 2023</div></div>', unsafe_allow_html=True)

    data = df["Country"].value_counts()
    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    ax1.axis("equal")
    st.pyplot(fig1)

    st.markdown('<div class="input-section"><div class="input-label">Average Salary Based On Country</div></div>', unsafe_allow_html=True)
    data = df.groupby(["Country"])["Salary"].mean().sort_values(ascending=True)
    st.bar_chart(data)

    st.markdown('<div class="input-section"><div class="input-label">Average Salary Based On Experience</div></div>', unsafe_allow_html=True)
    data = df.groupby(["WorkExp"])["Salary"].mean().sort_values(ascending=True)
    st.line_chart(data)

    st.markdown('<div class="input-section"><div class="input-label">Average Salary Based On Job-Type</div></div>', unsafe_allow_html=True)
    data = df.groupby(["DevType"])["Salary"].mean().sort_values(ascending=True)
    st.line_chart(data)

show_explore_page()