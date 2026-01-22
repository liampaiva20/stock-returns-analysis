import pandas as pd
import yfinance as yf
import time

excel_path = r"C:\Users\123ca\Documents\Scraped Data\Filtered Stocks.xlsx"
filtered_stocks = pd.read_excel(excel_path)

# Getting all the symbols from the filtered excel file
tickers = (
    filtered_stocks["symbol"]
    .dropna()
    .unique()
    .tolist()
)

def normalize_symbol(symbol):
    return symbol.replace(".", "-").strip()

tickers = [normalize_symbol(t) for t in tickers]

print(f"Total tickers to process: {len(tickers)}")

companies_rows = []
price_rows = []
dividends_rows = []
failed_rows = []

BATCH_SIZE = 50

# This downloads the stock data using yfinance
for start in range(0, len(tickers), BATCH_SIZE):
    batch = tickers[start:start + BATCH_SIZE]
    print(f"\nProcessing tickers {start + 1} to {start + len(batch)}")

    for symbol in batch:
        try:
            ticker = yf.Ticker(symbol)

            info = ticker.info
            if not info:
                failed_rows.append((symbol, "No company info"))
                continue

            companies_rows.append({
                "symbol": symbol,
                "company_name": info.get("longName"),
                "industry": info.get("industry"),
                "sector": info.get("sector"),
                "market_cap": info.get("marketCap"),
                "exchange": info.get("exchange"),
                "currency": info.get("currency")
            })

            hist = ticker.history(period="max", interval="1d")
            if hist.empty:
                failed_rows.append((symbol, "No price history"))
                continue

            hist.reset_index(inplace=True)

            for _, row in hist.iterrows():
                adj_close = row["Adj Close"] if "Adj Close" in row else row["Close"]

                price_rows.append({
                    "symbol": symbol,
                    "date": row["Date"],
                    "open": row["Open"],
                    "high": row["High"],
                    "low": row["Low"],
                    "close": row["Close"],
                    "adj_close": adj_close,
                    "volume": row["Volume"]
                })

            for date, value in ticker.dividends.items():
                dividends_rows.append({
                    "symbol": symbol,
                    "ex_date": date,
                    "dividend": float(value)
                })

            print(f"Loaded {symbol}")

        except Exception as e:
            failed_rows.append((symbol, str(e)))
            print(f"Failed {symbol}: {e}")

        time.sleep(1)

# Saving all the data into csv files
pd.DataFrame(companies_rows).to_csv(r"C:\Users\123ca\Documents\Scraped Data\companies.csv", index=False)
pd.DataFrame(price_rows).to_csv(r"C:\Users\123ca\Documents\Scraped Data\price_history.csv", index=False)
pd.DataFrame(dividends_rows).to_csv(r"C:\Users\123ca\Documents\Scraped Data\dividends.csv", index=False)
pd.DataFrame(failed_rows, columns=["symbol", "reason"]).to_csv(
    r"C:\Users\123ca\Documents\Scraped Data\failed_tickers.csv", index=False)

print("\nPipeline completed!") 
