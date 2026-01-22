INSERT INTO performance
WITH latest_price AS (
    SELECT
        symbol,
        MAX(date) AS latest_date
    FROM price_history
    GROUP BY symbol
),
first_price AS (
    SELECT
        symbol,
        MIN(date) AS first_date
    FROM price_history
    GROUP BY symbol
)
SELECT
    lp.symbol,

    p.adj_close / p_1m.adj_close  - 1 AS return_1m,
    p.adj_close / p_3m.adj_close  - 1 AS return_3m,
    p.adj_close / p_6m.adj_close  - 1 AS return_6m,
    p.adj_close / p_1y.adj_close  - 1 AS return_1y,
    p.adj_close / p_3y.adj_close  - 1 AS return_3y,
    p.adj_close / p_5y.adj_close  - 1 AS return_5y,
    p.adj_close / p_10y.adj_close - 1 AS return_10y,
    p.adj_close / p_life.adj_close - 1 AS return_life

FROM latest_price lp

JOIN price_history p
  ON p.symbol = lp.symbol
 AND p.date = lp.latest_date

LEFT JOIN price_history p_1m
  ON p_1m.symbol = lp.symbol
 AND p_1m.date = (
     SELECT MAX(date)
     FROM price_history
     WHERE symbol = lp.symbol
       AND date <= DATE_SUB(lp.latest_date, INTERVAL 1 MONTH)
 )

LEFT JOIN price_history p_3m
  ON p_3m.symbol = lp.symbol
 AND p_3m.date = (
     SELECT MAX(date)
     FROM price_history
     WHERE symbol = lp.symbol
       AND date <= DATE_SUB(lp.latest_date, INTERVAL 3 MONTH)
 )

LEFT JOIN price_history p_6m
  ON p_6m.symbol = lp.symbol
 AND p_6m.date = (
     SELECT MAX(date)
     FROM price_history
     WHERE symbol = lp.symbol
       AND date <= DATE_SUB(lp.latest_date, INTERVAL 6 MONTH)
 )

LEFT JOIN price_history p_1y
  ON p_1y.symbol = lp.symbol
 AND p_1y.date = (
     SELECT MAX(date)
     FROM price_history
     WHERE symbol = lp.symbol
       AND date <= DATE_SUB(lp.latest_date, INTERVAL 1 YEAR)
 )

LEFT JOIN price_history p_3y
  ON p_3y.symbol = lp.symbol
 AND p_3y.date = (
     SELECT MAX(date)
     FROM price_history
     WHERE symbol = lp.symbol
       AND date <= DATE_SUB(lp.latest_date, INTERVAL 3 YEAR)
 )

LEFT JOIN price_history p_5y
  ON p_5y.symbol = lp.symbol
 AND p_5y.date = (
     SELECT MAX(date)
     FROM price_history
     WHERE symbol = lp.symbol
       AND date <= DATE_SUB(lp.latest_date, INTERVAL 5 YEAR)
 )

LEFT JOIN price_history p_10y
  ON p_10y.symbol = lp.symbol
 AND p_10y.date = (
     SELECT MAX(date)
     FROM price_history
     WHERE symbol = lp.symbol
       AND date <= DATE_SUB(lp.latest_date, INTERVAL 10 YEAR)
 )

JOIN first_price fp
  ON fp.symbol = lp.symbol

JOIN price_history p_life
  ON p_life.symbol = fp.symbol
 AND p_life.date = fp.first_date;
