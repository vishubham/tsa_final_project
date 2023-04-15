# Code for the Compare Stocks page
import streamlit as st
from datetime import date, timedelta

st.title("Compare Stocks")

cols1 = st.columns(5)
stock_code1 = cols1[0].text_input("Stock 1 Code:", "AAPL")
stock_code2 = cols1[1].text_input("Stock 2 Code:", "GOOG")
stock_code3 = cols1[2].text_input("Stock 3 Code:", "MSFT")
stock_code4 = cols1[3].text_input("Stock 4 Code:", "META")
stock_code5 = cols1[4].text_input("Stock 5 Code:", "AMZN")

cols2 = st.columns(2)
start_date = cols2[0].date_input("Analysis Start Date:", date.today() - timedelta(days=365))
#start_date = start_date.strftime("%Y-%m-%d")
end_date = cols2[1].date_input("Analysis End Date:", date.today())
#end_date = end_date.strftime("%Y-%m-%d")

st.button("Analyze")

# loop to call function to fetch the data from yahoo finance
    # if stock code does not exist
    # cols1[i] https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/

st.subheader("")
st.subheader("Adjusted Daily Close Prices")
# call function to Plot the Adjusted Daily Close Prices
st.image("https://clauswilke.com/dataviz/balance_data_context_files/figure-html/price-plot-hgrid-1.png")
