# Code for the Compare Stocks page
import streamlit as st
from datetime import date, timedelta
import plotly.graph_objs as go
import pandas as pd
from stock_quant import fetch_prices

# app parameters
n_stocks = 5
plotted_price_type = 'close'
stock_codes_default = ["AAPL", "GOOG", "MSFT", "META", "AMZN"]
plot_width = 800
plot_height = 600

def plot_prices(df_dict, column):
    fig = go.Figure()

    for key, df in df_dict.items():
        fig.add_trace(go.Scatter(x=df.index, y=df[column], mode='lines', name=key))

    fig.update_layout(xaxis_title='Date',
                    yaxis_title=f"Adjusted {column.capitalize()} price",
                    width=plot_width,   # Set the width of the plot
                    height=plot_height  # Set the height of the plot
                    )

    return fig

st.title("Compare Stocks")

cols1 = st.columns(n_stocks)
stock_codes = []
for i in range(n_stocks):
    stock_codes.append(cols1[i].text_input(f"Stock code {i + 1}:", stock_codes_default[i], max_chars = 4))
# Make stock codes sorted and unique and remove empty values
stock_codes = sorted(list(set([s for s in stock_codes if s])))

cols2 = st.columns(2)
start_date = cols2[0].date_input("Analysis Start Date:", date.today() - timedelta(days=365))
#start_date = start_date.strftime("%Y-%m-%d")
end_date = cols2[1].date_input("Analysis End Date:", date.today())
#end_date = end_date.strftime("%Y-%m-%d")

if st.button("Analyze"):
    prices, failed_stocks = {}, []
    for stock in stock_codes:
        df = fetch_prices(stock, start_date, end_date)
        if df is not None:
            prices[stock] = df
        else:
            failed_stocks.append(stock)
    if len(failed_stocks) > 0:
        st.error(f"Stock code does not exist: {', '.join(failed_stocks)}")

    if prices:
        st.subheader("")
        st.subheader(f"Adjusted Daily {plotted_price_type.capitalize()} Prices")
        fig = plot_prices(prices, plotted_price_type)
        st.plotly_chart(fig, use_container_width=True)

