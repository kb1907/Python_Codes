import json
import requests
import pandas as pd

source = requests.get('https://api.covid19api.com/summary').text
data = json.loads(source)

with open("covid_summary.json","w") as f:
    json.dump(data, f, indent=2)

Country_Covid_Statistics = []

for country in data["Countries"]:
    Country_Covid_Statistics.append([country["Country"],
                                     country["TotalConfirmed"],
                                     country["TotalDeaths"]]
                                    )
Country_Covid_Statistics_df = pd.DataFrame(Country_Covid_Statistics,
                                           columns=["Country", "Total_Confirmed", "Total_Deaths"])

Country_Covid_Statistics_df.to_csv("Country_Covid_Statistics.csv")