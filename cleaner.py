def experience(x):
    if x ==  'More than 50 years':
        return 'More than 50 years'
    elif x == 'Less than 1 year':
        return 'Less than 1 year'
    elif x>=2 and x<=5:
        return '2-5'
    elif x>=6 and x<=10:
        return '6-10'
    elif x>=11 and x<=15:
        return '11-15'
    elif x>=16 and x<=20:
        return '16-20'
    elif x>=21 and x<=30:
        return '21-30'
    elif x>=31 and x<=40:
        return '31-40'
    elif x>=41 and x<=50:
        return '41-50'
    else:
        return x
    


def age_range(x):
    if x>=15 and x<=17:
        return 'Under 18 years old'
    elif x>=18 and x<=24:
        return '18-24 years old'
    elif x>=25 and x<=34:
        return '25-34 years old'
    elif x>=35 and x<=44:
        return '35-44 years old'
    elif x>=45 and x<=54:
        return '45-54 years old'
    elif x>=55 and x<=64:
        return '55-64 years old'
    else:
        return '65 years or older'



def workexp(x):
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
        return x



countries = [
    "United States of America","Germany","United Kingdom of Great Britain and Northern Ireland","India","Canada","France",
    "Poland","Brazil","Netherlands","Australia","Spain","Italy","Sweden"
]

def country_map(x):
    if x in countries:
        if x == "United States of America":
            return 'USA'
        elif x == "United Kingdom of Great Britain and Northern Ireland":
            return 'UK and Ireland '
        else:
            return x

    else:
        return 'Other'