# Code for the Forecasting page
import streamlit as st
from datetime import date, timedelta

st.title("Stock Price Forecast")

stock_code = st.text_input("NYSE Stock Code:", "AAPL")
col1, col2 = st.columns(2)

train_start_date = col1.date_input("Training Start Date:", date.today() - timedelta(days=3650))
train_start_date = train_start_date.strftime("%Y-%m-%d")
train_end_date = col1.date_input("Training End Date:", date.today() - timedelta(days=1))
train_end_date = train_end_date.strftime("%Y-%m-%d")

forecast_start_date = col2.date_input("Forecast Start Date:", date.today() + timedelta(days=1))
forecast_start_date = forecast_start_date.strftime("%Y-%m-%d")
forecast_end_date = col2.date_input("Forecast End Date:", date.today() + timedelta(days=365))
forecast_end_date = forecast_end_date.strftime("%Y-%m-%d")

st.button("Predict")

# call function to fetch the data from yahoo finance

# display raw data in a collapsible section
raw_data = st.expander("Raw Data")
#raw_data.write(data)

st.subheader("Forecast for " + stock_code)
# Plot the forecast
"""
Placeholder for plot containing lines for:
1.	Train values
2.	Test values
3.	Forecasted values
4.	Confidence interval band
"""
