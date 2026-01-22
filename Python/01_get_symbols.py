import requests
import pandas as pd
import openpyxl

# I hashed out the api key for safety reasons
API_KEY = "c####c"

url = "https://api.twelvedata.com/stocks"
params = {
    "apikey" : API_KEY
}

response = requests.get(url, params=params)
data = response.json()

stocks = pd.DataFrame(data["data"])

# I only need the NYSE and Nasdaq stocks, so I will filter them from the stocks dataframe
filtered_stocks = stocks[
    stocks["exchange"].isin(["NYSE", "NASDAQ"])
].reset_index(drop=True)

filtered_stocks.to_excel(r"C:\Users\123ca\Documents\Scraped Data\Filtered Stocks.xlsx", index=False)
print("Succesfully downloaded!")
