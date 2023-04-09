# tsa_final_project
Time Series Analysis Project @ IU Bloomington in Spring 2023

## Project: Stock Quant

## Team 
•	Constantinos Vogiatzis cvogiatz@iu.edu 
•	Shubham Saurabh ssaurab@iu.edu 
•	Seth Smithson sesmit@iu.edu 

## Project Objectives 
•	Objectives: 
Create a quantitative stock app that can pull time series data for any New York Stock Exchange (NYSE) stock code for personal, enthusiast investors. This will assist an investor to make buy/sell decisions about a stock. It will pull enough data to enable a dashboard of stock performance over time, provide finance metrics to help gauge company performance, and enable comparison with another stock or fund.

## Project Description
•	Usefulness: 
There are many stock analysis tools available in the market. However, most only provide basic services for free. This dashboard application provides advanced metrics and analysis capabilities that would normally be hidden behind a paywall.
This application will target advanced users of equity investing who want to compare corporate finance metrics to gauge if an investment is a “value investment” where the company’s current valuation may be undervalued relative to the market sector or market as a whole but displays strong finance fundamentals.

•	Dataset: 
There are 3 potential sources of data for this project:
1.	Alpha Vantage APIs
2.	Yahoo Finance APIs
3.	Google Finance APIs
We will experiment will all 3 and decide upon the one that works best for our purpose. As per our initial analysis, all 3 of these APIs can be invoked within Python and converted into Pandas DataFrames for further processing.
These APIs provide data in the JSON format, which is easily readable for humans and machines. It will not require any data cleaning or complex operations to utilize. These stock market data are curated by the respective providers hence, the data is complete (no data cleanup or imputation required). 
The data is available on a daily cadence for each stock code. We will also try to obtain the monthly, quarterly, and annual company financial data to be used for comparison and analysis. The stock data is available going back at least 30 years – which is sufficient for our time series analysis. 
Out of the 3, the Alpha Vantage API operates on a freemium model where some base-level data is available for free at a certain bandwidth restriction. The free data provided at the time of this project proposal submission is more than sufficient. However, if there are any changes in their offering, this may necessitate moving to another free API, such as Yahoo or Google Finance, which may limit the variety of available metrics. This, in turn, may limit the scope of the project. Nevertheless, while there is a contingency plan in place, the expansion of Alpha Vantage’s freemium model is not predicted to be an issue over the course of the remaining semester.

Datasets:
Alpha Vantage Dataset: https://www.alphavantage.co/documentation/
Google Finance Dataset: https://pypi.org/project/googlefinance/ 
Yahoo Finance Dataset: https://pypi.org/project/yfinance/ 
