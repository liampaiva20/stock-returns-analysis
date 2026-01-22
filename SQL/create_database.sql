-- Create database for our stock market data
CREATE DATABASE market_data;

USE market_data;

-- Create Companies table
CREATE TABLE companies (
    symbol VARCHAR(10) PRIMARY KEY,
    company_name VARCHAR(255),
    industry VARCHAR(255),
    sector VARCHAR(255),
    market_cap BIGINT,
    exchange VARCHAR(10),
    currency VARCHAR(10)
);

-- Create Dividends table
CREATE TABLE dividends (
    symbol VARCHAR(10),
    ex_date DATE,
    dividend DECIMAL(30,6),
    PRIMARY KEY (symbol, ex_date)
);

-- Create Price History table
CREATE TABLE price_history (
    symbol VARCHAR(10) NOT NULL,
    date DATE NOT NULL,
    open DECIMAL(30,10),
    high DECIMAL(30,10),
    low DECIMAL(30,10),
    close DECIMAL(30,10),
    adj_close DECIMAL(30,10),
    volume BIGINT,
    PRIMARY KEY (symbol, date)
);

CREATE INDEX idx_price_symbol_date
ON price_history (symbol, date);

