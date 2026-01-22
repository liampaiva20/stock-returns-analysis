------ QUESTIONS -------

-- List all companies
SELECT *
FROM companies;

-- Get the price history for one company
SELECT * 
FROM price_history
WHERE symbol="A";

-- Find the most recent price for each company
SELECT *
FROM price_history AS p
WHERE symbol="NVDA"
ORDER BY p.date ASC
LIMIT 1;

-- Show companies in a specific sector
SELECT *
FROM companies AS c
WHERE c.sector = 'Healthcare';

-- List dividend payments for one company
SELECT *
FROM dividends
WHERE symbol = 'GOOGL';

---------------------------------------------------

-- Show company name with its latest closing price
SELECT c.symbol, c.company_name, p.date, p.close AS latest_closing_price
FROM companies as c
INNER JOIN price_history AS p
on c.symbol = p.symbol
WHERE c.symbol = 'MIRM'
ORDER BY p.date DESC
LIMIT 1;

-- Average closing price per company
SELECT p.symbol, AVG(p.close) AS average_closing_price 
FROM price_history AS p
GROUP BY p.symbol;

-- Total dividends paid by each company
SELECT d.symbol, COUNT(d.dividend) AS total_dividends
FROM dividends AS d
GROUP BY d.symbol
ORDER BY COUNT(d.dividend) DESC;

-- Top 20 companies by average returns for the last 3 years
SELECT p.symbol, c.company_name, p.`3y`*100 AS '3_year_returns'
FROM performance AS p
INNER JOIN companies as c
ON p.symbol=c.symbol
ORDER BY p.`3y` DESC
LIMIT 20;

-- Top 20 companies by average returns for the last 5 years
SELECT p.symbol, c.company_name, p.`5y`*100 AS '5_year_returns'
FROM performance AS p
INNER JOIN companies as c
ON p.symbol=c.symbol
ORDER BY p.`5y` DESC
LIMIT 20;

-- Average 5 year returns for each sector
SELECT c.sector, AVG(p.`5y`)*100 AS 'Average 5 Year Returns'
FROM companies AS c
INNER JOIN performance AS p
ON c.symbol=p.symbol
GROUP BY c.sector
ORDER BY AVG(p.`5y`)*100 DESC;
-----------------------------------------------------
