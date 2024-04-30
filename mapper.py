def map_edu_lev(category):
    category_to_code = {
        "Bachelor’s degree": 0,
        "Less than a Bachelors": 1,
        "Master’s degree": 2,
        "Post grad": 3
    }
    value = category_to_code.get(category, -1)
    return value



def map_years_code(category):
    category_to_code = {
        '1': 4,
        '11-15': 7,
        '16-20': 3,
        '2-5': 8,
        '21-30': 1,
        '31-40': 2,
        '41-50': 5,
        '6-10': 0,
        'Less than 1 year': 6,
        'More than 50 years': 9
    }
    value = category_to_code.get(category, -1)    
    return value



def map_age(category):
    category_to_code = {
        "55-64 years old": 0,
        "25-34 years old": 1,
        "35-44 years old": 2,
        "18-24 years old": 3,
        "45-54 years old": 4,
        "65 years or older": 5,
        "Under 18 years old": 6
    }
    value = category_to_code.get(category, -1)    
    return value



def map_job_type(category):
    category_to_code = {
        'Academic researcher': 11,
        'Blockchain': 14,
        'Cloud infrastructure engineer': 15,
        'Data or business analyst': 10,
        'Data scientist or machine learning specialist': 4,
        'Database administrator': 27,
        'Designer': 32,
        'DevOps specialist': 13,
        'Developer Advocate': 12,
        'Developer Experience': 2,
        'Developer, QA or test': 24,
        'Developer, back-end': 9,
        'Developer, desktop or enterprise applications': 21,
        'Developer, embedded applications or devices': 17,
        'Developer, front-end': 7,
        'Developer, full-stack': 5,
        'Developer, game or graphics': 19,
        'Developer, mobile': 30,
        'Educator': 20,
        'Engineer, data': 3,
        'Engineer, site reliability': 0,
        'Engineering manager': 16,
        'Hardware Engineer': 29,
        'Marketing or sales professional': 8,
        'Other (please specify)': 1,
        'Product manager': 25,
        'Project manager': 26,
        'Research & Development role': 22,
        'Scientist': 28,
        'Security professional': 23,
        'Senior Executive (C-Suite, VP, etc.)': 6,
        'Student': 18,
        'System administrator': 31
    }
    value = category_to_code.get(category, -1)    
    return value



def map_country(country):
    country_to_code = {
        "Australia": 13,
        "Brazil": 8,
        "Canada": 12,
        "France": 7,
        "Germany": 4,
        "India": 3,
        "Italy": 10,
        "Netherlands": 6,
        "Other": 2,
        "Poland": 1,
        "Spain": 0,
        "Sweden": 11,
        "UK and Ireland": 5,
        "USA": 9
    }
    value = country_to_code.get(country, -1)   
    return value



def map_work_exp(category):
    category_to_code = {
        '0.0':5,
        '1': 8,
        '11-15': 4,
        '16-20': 2,
        '2-5': 3,
        '21-30': 6,
        '31-40': 1,
        '41-50': 7,
        '6-10': 0,
    }
    value = category_to_code.get(category, -1)
    return value
