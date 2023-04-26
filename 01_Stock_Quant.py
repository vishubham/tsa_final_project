# Code for the landing page
import streamlit as st

#st.set_page_config(layout="wide")
st.title("Stock Quant")

st.write("""
_Stock Quant_ is a quantitative stock app that can pull time series data for any New York Stock Exchange (NYSE) stock code for individual investors. You can use this information to make investment decisions about a stock. 

## Functionality

1. __Compare Stocks:__ Select up to 5 stocks and obtain key metrics and comparison plots between selected date ranges.

2. __Stock Price Forecast:__ Specify the training date range to be used for analysis and obtain forecast of the stock's price for a selected time period.
""")

st.write("""
### Developed By
__Shubham Saurabh__  \n__Constantinos Vogiatzis__  \n__Seth Smithson__  \nLuddy School of Informatics, Computing, and Engineering, Indiana University, Bloomington  \nDSCI D590 Time Series Analysis, Final Project, Spring 2023  \nDr. Olga Scrivner  \nApr 15, 2023  \n  \nLast updated on: Apr 26, 2023
""")
