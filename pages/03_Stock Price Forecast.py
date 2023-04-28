# Code for the Forecasting page
import streamlit as st
from datetime import date, timedelta
import pandas as pd
from stock_quant import fetch_daily_prices
from prophet import Prophet
from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay
from prophet.plot import plot_plotly

st.set_page_config(layout="wide")
st.title("Stock Price Forecast")

stock_code = st.text_input("NYSE Stock Code:", "AAPL", max_chars = 5)
# There are 48 stocks having 5 character ticker symbols listed on the NYSE.
col1, col2 = st.columns(2)

train_start_date = col1.date_input("Training Start Date:", date.today() - timedelta(days=3650))
train_start_date = train_start_date.strftime("%Y-%m-%d")
train_end_date = col1.date_input("Training End Date:", date.today() - timedelta(days=1))
train_end_date = train_end_date.strftime("%Y-%m-%d")

forecast_start_date = col2.date_input("Forecast Start Date:", date.today() + timedelta(days=1))
forecast_start_date = forecast_start_date.strftime("%Y-%m-%d")
forecast_end_date = col2.date_input("Forecast End Date:", date.today() + timedelta(days=365))
forecast_end_date = forecast_end_date.strftime("%Y-%m-%d")

if st.button("Predict"):
    # Fetch the daily adjusted prices for max duration
    data = fetch_daily_prices(stock_code, train_start_date, forecast_end_date, adjust_all = True)

    if len(data) == 0:
        st.write("Invalid stock code or no data found. Please verify stock code and dates before trying again.")

    # display raw data in a collapsible section
    raw_data = st.expander("Raw Data")
    raw_data.write(data)

    # Slice the dataframe for training and select only adj_close column
    train_data = data[train_start_date:train_end_date]['adj_close'].copy()
    train_data = train_data.reset_index()  # Move datetime index into a column
    train_data.columns = ['ds', 'y']  # Rename the columns
    # st.write(train_data.info())  # Uncomment for debugging
    # st.write(train_data)  # Uncomment for debugging
    
    # Define the prophet model
    model = Prophet()  # Create the model
    model.add_country_holidays(country_name='US')
    model.fit(train_data)  # Fit the training data

    # Make dataframe to hold forecast data
    # define US federal holidays
    us_bdays = CustomBusinessDay(calendar=USFederalHolidayCalendar())
    # count business days between training end date and prediction date
    delta = len(pd.bdate_range(train_end_date, forecast_end_date, freq=us_bdays))-1
    future = model.make_future_dataframe(periods=delta, freq=us_bdays)
    # st.write(future)  # Uncomment for debugging

    # Predict
    forecast = model.predict(future)

    # display raw forecast data in a collapsible section
    raw_data = st.expander("Raw forecast data for " + stock_code)
    raw_data.write(forecast)
 
    # Plot the forecast
    #    Placeholder for plot containing lines for:
    #    1.	Train values
    #    2.	Test values
    #    3.	Forecasted values
    #    4.	Confidence interval band
    st.subheader('Forecasted Trend line')
    fig_forecast = plot_plotly(model, forecast)
    fig_forecast.layout.update(title_text='Daily close price predictions for '+stock_code, 
                                xaxis_rangeslider_visible=True,
                                xaxis_title='Timeline',
                                yaxis_title='Unit Price (USD)')
    st.plotly_chart(fig_forecast)

    st.subheader("Forecast Components")
    fig2 = model.plot_components(forecast)
    st.write(fig2)
