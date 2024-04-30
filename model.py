import joblib
import pandas as pd

model = joblib.load('model.pkl')

regressor = model["regressor"]
scaler = model["scaler"]

def prediction(edu_lev,years_code,age,job_type,country,years_exp):

    values = [edu_lev, years_code, age, job_type, country, years_exp]
    df = pd.DataFrame([values], columns=['EdLevel', 'YearsCodePro', 'Age', 'DevType', 'Country', 'WorkExp'])

    input = scaler.transform(df)
    salary = regressor.predict(input)[0]

    return salary