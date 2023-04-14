# Code for the landing page
import streamlit as st

st.title("Stock Quant")

st.write("""
## About
'Stock Quant' is a quantitative stock app that can pull time series data for any New York Stock Exchange (NYSE) stock code for individual investors. This will assist an investor to make buy/sell decisions about a stock. It will pull enough data to enable a dashboard of stock performance over time, provide finance metrics to help gauge company performance, and enable comparison with another stock or fund.

There are many stock analysis tools available in the market. However, most only provide basic services for free. This dashboard application provides advanced metrics and analysis capabilities that would normally be hidden behind a paywall.

This application will target advanced users of equity investing who want to compare corporate finance metrics to gauge if an investment is a “value investment” where the company’s current valuation may be undervalued relative to the market sector or market as a whole but displays strong finance fundamentals.

## Functionality

1. __Compare Stocks:__ The user can select up to 5 stocks and obtain key metrics and comparison plots between selected date ranges.

2. __Stock Price Forecast:__ The user can specify the training date range to be used for analysis and obtain forecast of stock price for a selected time period
""")

st.write("""
### Developed By
__Shubham Saurabh__  \n__Constantinos Vogiatzis__  \n__Seth Smithson__  \nLuddy School of Informatics, Computing, and Engineering, Indiana University, Bloomington  \nDSCI D590 Time Series Analysis, Final Project, Spring 2023  \nDr. Olga Scrivner  \nApr 15, 2023  \nLast updated on: Apr 15, 2023
""")
