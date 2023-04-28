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
@st.cache
def st_fetch_prices(stock_code, start_date, end_date):
    # Create local version of the function that is cached
    return fetch_prices(stock_code, start_date, end_date)

def combine_columns(df_dict, column):
    """
    Combine a specified column from multiple pandas DataFrames with the same index and columns.

    Parameters:
    -----------
    df_dict : dict
        A dictionary containing pandas DataFrames as values and their descriptive names as keys.
    column : str
        The name of the column to extract from each DataFrame.

    Returns:
    --------
    result : pandas.DataFrame
        A new DataFrame containing the specified column from each input DataFrame.
        The column names of the new DataFrame correspond to the dictionary keys of the input DataFrames.
    """
    combined_columns = []

    for key, df in df_dict.items():
        temp_df = df[[column]].rename(columns={column: key})
        combined_columns.append(temp_df)

    result = pd.concat(combined_columns, axis=1)
    return result

def format_table(df, float_format='{:.2f}'):
    # Create copy with appropriate formatting for display
    formatted_df = df.copy()
    formatted_df.index = formatted_df.index.strftime('%Y-%m-%d')
    for col in formatted_df.columns:
        if pd.api.types.is_float_dtype(formatted_df[col]):
            formatted_df[col] = formatted_df[col].apply(lambda x: float_format.format(x))
    return formatted_df


def plot_prices(df_dict, column):
    fig = go.Figure()

    for key, df in df_dict.items():
        fig.add_trace(go.Scatter(x=df.index, y=df[column], mode='lines', name=key))

    fig.update_layout(xaxis_title='Date',
                    yaxis_title=f"Adjusted {column.capitalize()} price",
                    width=plot_width,   # Set the width of the plot
                    height=plot_height,  # Set the height of the plot
                    plot_bgcolor = 'white',  # Set the figure background color to white
                    # xaxis = dict(
                    #     gridcolor='lightgray',  # Set the x-axis grid lines color to light gray
                    #     line=dict(color='black', width=1)  # Add a border around the figure
                    # ),
                    # yaxis = dict(
                    #     gridcolor='lightgray',  # Set the y-axis grid lines color to light gray
                    #     line=dict(color='black', width=1)  # Add a border around the figure
                    # ),
                    margin = dict(l=10, r=10, t=30, b=10)  # Adjust the margins to ensure the border is visible

    )

    fig.update_xaxes(
        gridcolor='lightgray',  # Set the x-axis grid lines color to light gray
        linecolor='black',  # Add a border around the figure
        linewidth=1,
        mirror=True
    )

    fig.update_yaxes(
        gridcolor='lightgray',  # Set the y-axis grid lines color to light gray
        linecolor='black',  # Add a border around the figure
        linewidth=1,
        mirror=True
    )

    return fig

st.set_page_config(layout="wide")
st.title("Compare Stocks")

cols1 = st.columns(n_stocks)
stock_codes = []
for i in range(n_stocks):
    stock_codes.append(cols1[i].text_input(f"Stock code {i + 1}:", stock_codes_default[i], max_chars = 5))
    # There are 48 stocks having 5 character ticker symbols listed on the NYSE.
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
        df = st_fetch_prices(stock, start_date, end_date)
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

        with st.expander("Price table"):
            st.write(f"The table below shows the adjusted daily {plotted_price_type} prices for the selected stocks.")
            df = combine_columns(prices, plotted_price_type)
            df = format_table(df)
            st.dataframe(df)