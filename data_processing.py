import pandas as pd
df = pd.read_csv('covid_19_cases.csv')
def fetch_country_info(country_name):
    if not isinstance(country_name,str):
        print("Please input a valid country name")
        return "Bad input, NO data return"
    country_data = df[df['Country'] == country_name]
    if len(country_data) ==0 :
        print("There is no data for this country")
        return "No data for this country"
    else:
        print(country_data.iloc[0,0:5])
        return country_data.iloc[0,0:5]

fetch_country_info("Japan")