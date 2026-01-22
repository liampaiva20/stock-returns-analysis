import pandas as pd

# Load CSV files (small ones only)
companies = pd.read_csv(
    r"C:\Users\123ca\Documents\Scraped Data\companies.csv"
)

dividends = pd.read_csv(
    r"C:\Users\123ca\Documents\Scraped Data\dividends.csv"
)

# Clean companies file
print("Cleaning companies file...")
companies_cleaned = companies.dropna()
companies_cleaned.to_csv(
    r"C:\Users\123ca\Documents\Scraped Data\companies_cleaned.csv",
    index=False
)
print("Cleaned companies file!")

valid_symbols = set(companies_cleaned['symbol'])

# Filtering and cleaning the dividends file
print("Filtering dividends file...")

df_dividends_filtered = dividends[
    dividends['symbol'].isin(valid_symbols)
].copy()

#I need to remove timezone and the time from ex_date in order to load into sql
df_dividends_filtered['ex_date'] = (
    pd.to_datetime(df_dividends_filtered['ex_date'], utc=True)
      .dt.date
)

# Remove duplicates
df_dividends_filtered = df_dividends_filtered.drop_duplicates(
    subset=['symbol', 'ex_date']
)

df_dividends_filtered.to_csv(
    r"C:\Users\123ca\Documents\Scraped Data\filtered_dividends.csv",
    index=False
)
print("Filtered dividends file!")

# Filtering and cleaning the price history file
print("Filtering price history file in chunks...")

price_history_file = r"C:\Users\123ca\Documents\Scraped Data\price_history.csv"
filtered_price_file = r"C:\Users\123ca\Documents\Scraped Data\filtered_price_history.csv"

# I need to do this in chunks as there are too many rows in the file
chunksize = 2_000_000
first_chunk = True

for chunk in pd.read_csv(price_history_file, chunksize=chunksize):

    filtered_chunk = chunk[
        chunk['symbol'].isin(valid_symbols)
    ].copy()

    filtered_chunk['date'] = (
        pd.to_datetime(filtered_chunk['date'], utc=True)
          .dt.date
    )

    filtered_chunk = filtered_chunk.drop_duplicates(
        subset=['symbol', 'date']
    )

    if first_chunk:
        filtered_chunk.to_csv(filtered_price_file, index=False, mode='w')
        first_chunk = False
    else:
        filtered_chunk.to_csv(
            filtered_price_file,
            index=False,
            header=False,
            mode='a'
        )

print("Filtered price history file!")
print("All tasks completed successfully!")
