from alpha_vantage.timeseries import TimeSeries
from datetime import datetime
import yfinance as yf
import plotly.graph_objs as go
import pandas as pd

VANTAGE_KEY = 'MUQXX1BUB5ZP3ZIC'    # Costas' free key

def fetch_prices(stock_code, start_date, end_date):
    """Fetches daily adjusted stock prices for a given stock code within a specified date range.

    This function queries the Alpha Vantage API for daily adjusted stock prices, processes the data to adjust
    open, high, low, and close prices for splits, and returns a pandas DataFrame with the fetched stock prices
    within the specified date range.

    Parameters
    ----------
    stock_code : str
        The stock code (ticker symbol) for which to fetch the stock prices.
    start_date : str or datetime
        The start date of the desired date range.
    end_date : str or datetime
        The end date of the desired date range.

    Returns
    -------
    df_prices_filtered : pandas.DataFrame
        A DataFrame with daily adjusted stock prices within the specified date range, indexed by date
        and columns: 'open', 'high', 'low', 'close', 'adj_close', 'volume', 'dividend', 'split'.

    Example
    -------
    >>> df_prices_filtered = fetch_prices('MSFT', '2021-04-16', '2021-04-22')
    >>> print(df_prices_filtered.head())
                   open        high         low       close   adj_close      volume  dividend  split
    date
    2021-04-16  260.739  263.301000  260.171000  260.740000  253.038165  24878600.0       0.0    1.0
    2021-04-19  260.190  261.537000  257.821000  258.260000  250.622997  23209300.0       0.0    1.0
    2021-04-20  257.821  260.600000  256.840000  258.097000  250.465010  19722900.0       0.0    1.0
    2021-04-21  255.400  259.820000  254.000000  259.501000  251.833362  24030400.0       0.0    1.0
    2021-04-22  260.209  261.779000  255.890000  255.891000  248.320740  25606200.0       0.0    1.0
    """
    if isinstance(start_date, str):
        start_date = datetime.strptime(start_date, "%Y-%m-%d")

    if isinstance(end_date, str):
        end_date = datetime.strptime(end_date, "%Y-%m-%d")

    # df_prices = _fetch_prices_vantage(stock_code, date_range='full')
    # df_prices_filtered = df_prices[(df_prices.index >= start_date) & (df_prices.index <= end_date)]
    #
    # return df_prices_filtered

    return _fetch_prices_yahoo(stock_code, start_date, end_date)

def _fetch_prices_yahoo(stock_code, start_date, end_date):
    """
    Fetches daily historical stock prices for a given stock code from Yahoo Finance within a specified date range.

    This function queries the Yahoo Finance API for daily historical stock prices and returns a pandas DataFrame
    with the fetched stock prices within the specified date range.

    Parameters
    ----------
    stock_code : str
        The stock code (ticker symbol) for which to fetch the stock prices.
    start_date : str or datetime
        The start date of the desired date range.
    end_date : str or datetime
        The end date of the desired date range.

    Returns
    -------
    df_prices : pandas.DataFrame
        A DataFrame with daily historical stock prices within the specified date range, indexed by date
        and columns: 'open', 'high', 'low', 'close', 'volume', 'divident', 'split'.

    Example
    -------
    >>> df_prices = _fetch_prices_yahoo('MSFT', '2021-04-16', '2021-04-22')
    >>> print(df_prices.head())
                                     open        high         low       close    volume  dividend  split
    Date
    2021-04-16 00:00:00-04:00  254.873177  256.376070  253.036311  256.120667  24878600       0.0    0.0
    2021-04-19 00:00:00-04:00  255.580436  256.847591  253.252428  254.156113  23209300       0.0    0.0
    2021-04-20 00:00:00-04:00  253.252485  255.590326  252.289836  253.684692  19722900       0.0    0.0
    2021-04-21 00:00:00-04:00  254.352571  256.061735  252.692509  255.963501  24030400       0.0    0.0
    """
    if isinstance(start_date, str):
        start_date = datetime.strptime(start_date, "%Y-%m-%d")

    if isinstance(end_date, str):
        end_date = datetime.strptime(end_date, "%Y-%m-%d")

    stock = yf.Ticker(stock_code)

    try:
        df_prices = stock.history(start=start_date, end=end_date)
    except Exception as e:
        df_prices = None

    if df_prices is not None and df_prices.empty:
        df_prices = None

    if df_prices is not None:
        df_prices.rename(columns={
            'Open': 'open',
            'High': 'high',
            'Low': 'low',
            'Close': 'close',
            'Volume': 'volume',
            'Dividends': 'dividend',
            'Stock Splits': 'split'
        }, inplace=True)

    return df_prices

def _fetch_prices_vantage(stock_code, date_range='full'):
    """
    This function queries the Alpha Vantage API for daily adjusted stock prices,
    processes the data to adjust open, high, low, and close prices for splits,
    and returns a pandas DataFrame with the fetched stock prices. Rows are ordered
    from oldest to newest.

    Parameters
    ----------
    stock_code : str
        The stock code (ticker symbol) for which to fetch the stock prices.
    date_range : str, optional, default: 'full'
        The range of data to return. Either 'compact' for the last 100 trading days,
        or 'full' for the entire historical data.

    Returns
    -------
    df_prices : pandas.DataFrame
        A DataFrame with daily adjusted stock prices, indexed by date and columns:
        'open', 'high', 'low', 'close', 'adj_close', 'volume', 'dividend', 'split'.

    Example
    -------
    >>> df_prices = _fetch_prices_vantage('MSFT', date_range='compact')
    >>> print(df_prices.head())
                   open        high         low       close   adj_close      volume  dividend  split
    date
    2021-04-16  260.739  263.301000  260.171000  260.740000  253.038165  24878600.0       0.0    1.0
    2021-04-19  260.190  261.537000  257.821000  258.260000  250.622997  23209300.0       0.0    1.0
    2021-04-20  257.821  260.600000  256.840000  258.097000  250.465010  19722900.0       0.0    1.0
    2021-04-21  255.400  259.820000  254.000000  259.501000  251.833362  24030400.0       0.0    1.0
    2021-04-22  260.209  261.779000  255.890000  255.891000  248.320740  25606200.0       0.0    1.0
"""

    ts = TimeSeries(key=VANTAGE_KEY, output_format='pandas', indexing_type='date')
    df_prices, meta_data = ts.get_daily_adjusted(stock_code, outputsize=date_range)
    df_prices.rename(columns={
        '1. open': 'open',
        '2. high': 'high',
        '3. low': 'low',
        '4. close': 'close',
        '5. adjusted close': 'adj_close',
        '6. volume': 'volume',
        '7. dividend amount': 'dividend',
        '8. split coefficient': 'split'
    }, inplace=True)

    # Sort from old to new data
    df_prices.sort_index(ascending=False, inplace=True)

    # Adjust open, low, high the same way as adjusted close - all prices are now adjusted for splits
    split_ratio = df_prices['adj_close'] / df_prices['close']
    df_prices['open'] = df_prices['open'] * split_ratio
    df_prices['high'] = df_prices['high'] * split_ratio
    df_prices['low'] = df_prices['low'] * split_ratio
    df_prices['close'] = df_prices['close'] * split_ratio

    return df_prices