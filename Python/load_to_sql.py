import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
import pymysql

# Creating the Python connection to MySQL
engine = create_engine(
    "mysql+pymysql://root:L#####3@localhost/market_data" # I hashed out the password for safety reasons
)

# Loading the companies data into SQL
companies = pd.read_csv(
    r"C:\Users\123ca\Documents\Scraped Data\companies_cleaned.csv"
)
companies.to_sql(
    name="companies",
    con=engine,
    if_exists="append",
    index=False
)
print("Companies loaded")

# Loading the dividends data into SQL
dividends = pd.read_csv(
    r"C:\Users\123ca\Documents\Scraped Data\filtered_dividends.csv",
    parse_dates=["ex_date"]
)
dividends.to_sql(
    name="dividends",
    con=engine,
    if_exists="append",
    index=False
)
print("Dividends loaded")

# Loading the price history data into SQL
price_file = r"C:\Users\123ca\Documents\Scraped Data\filtered_price_history.csv"

# Because the file is so big, we need to load it in chunks
chunksize = 100_000

for chunk in pd.read_csv(
    price_file,
    chunksize=chunksize,
    parse_dates=["date"]
):
    chunk.to_sql(
        name="price_history",
        con=engine,
        if_exists="append",
        index=False
    )

print("Price history loaded")
