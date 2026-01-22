# Stock Returns Analysis (Python, SQL, Power BI)

## Project Overview
This project analyzes historical stock price data to evaluate long-term performance across multiple symbols and sectors. The workflow demonstrates data collection, database design, SQL analytics, and business intelligence visualization.

## Tools & Technologies
- Python (data collection and processing)
- SQL (table creation, returns calculation, analysis)
- Power BI (interactive dashboards)
- GitHub (version control)

## Workflow
1. Collected historical stock price data using Python
2. Loaded cleaned data into a SQL database
3. Created a returns table calculating 3-year and 5-year returns
4. Used SQL queries to explore trends and performance
5. Imported tables into Power BI for visualization

## Power BI Dashboard
### Page 1 – Returns Analysis
- Symbol and sector slicers
- Top 10 stocks by 3-year returns
- Top 10 stocks by 5-year returns
- Stock summary table

### Page 2 – Price Trends
- Symbol slicer
- Date range slicer
- Line chart showing stock price over time

## Key Insights
- Long-term returns vary significantly by sector
- Some stocks outperform consistently over both 3-year and 5-year periods
- Time-series visualization helps identify volatility and trend strength

## Repository Contents
- `python/`: Python scripts for data collection
- `sql/`: SQL scripts for table creation and analysis
- `powerbi/`: Dashboard screenshots
- `data/`: Sample dataset (if applicable)

## Future Improvements
- Add automated data refresh
- Expand analysis to include volatility and risk metrics
- Deploy Power BI dashboard to Power BI Service
