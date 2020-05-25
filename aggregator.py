import datetime
import time

import config as cfg
import pandas as pd
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.timeseries import TimeSeries

api_key = cfg.Secrets["api_key"]

ts = TimeSeries(key=api_key, output_format="pandas")
ti = TechIndicators(key=api_key, output_format="pandas")
# Testing API
# data, meta_data = ts.get_intraday(symbol="OAS", interval="1min", outputsize="full")
# print(data)


def get_intraday_data_one_minute(ticker):
    """Real-time 1 minute intraday data of a given stock ticker

    Arguments:
        ticker {string} -- unique series of letters assigned to a security for trading purposes

    Returns:
        Pandas -- Formatted dataframe of exchange rates and data
    """
    data = ts.get_intraday(symbol=ticker, interval="1min", outputsize="full")
    return data


def get_intraday_data_five_minute(ticker):
    """Real-time 5 minute intraday data of a given stock ticker

    Arguments:
        ticker {string} -- unique series of letters assigned to a security for trading purposes

    Returns:
        Pandas -- Formatted dataframe of exchange rates and data
    """
    data = ts.get_intraday(symbol=ticker, interval="5min", outputsize="full")
    return data


def get_intraday_data_fifteen_minute(ticker):
    """Real-time 15 minute intraday data of a given stock ticker

    Arguments:
        ticker {string} -- unique series of letters assigned to a security for trading purposes

    Returns:
        Pandas -- Formatted dataframe of exchange rates and data
    """
    data = ts.get_intraday(symbol=ticker, interval="15min", outputsize="full")
    return data


def get_intraday_data_thirty_minute(ticker):
    """Real-time 30 minute intraday data of a given stock ticker

    Arguments:
        ticker {string} -- unique series of letters assigned to a security for trading purposes

    Returns:
        Pandas -- Formatted dataframe of exchange rates and data
    """
    data = ts.get_intraday(symbol=ticker, interval="30min", outputsize="full")
    return data


def get_intraday_data_sixty_minute(ticker):
    """Real-time 60 minute intraday data of a given stock ticker

    Arguments:
        ticker {string} -- unique series of letters assigned to a security for trading purposes

    Returns:
        Pandas -- Formatted dataframe of exchange rates and data
    """
    data = ts.get_intraday(symbol=ticker, interval="60min", outputsize="full")
    return data


def get_daily_data(ticker):
    """Real-time daily data of a given stock ticker

    Arguments:
        ticker {string} -- unique series of letters assigned to a security for trading purposes

    Returns:
        Pandas -- Formatted dataframe of exchange rates and data
    """
    data = ts.get_daily(symbol=ticker, outputsize="full")
    return data


def get_weekly_data(ticker):
    """Real-time weekly data of a given stock ticker

    Arguments:
        ticker {string} -- unique series of letters assigned to a security for trading purposes

    Returns:
        Pandas -- Formatted dataframe of exchange rates and data
    """
    data = ts.get_weekly(symbol=ticker, outputsize="full")
    return data


def get_monthly_data(ticker):
    """Real-time Monthly data of a given stock ticker

    Arguments:
        ticker {string} -- unique series of letters assigned to a security for trading purposes

    Returns:
        Pandas -- Formatted dataframe of exchange rates and data
    """
    data = ts.get_monthly(symbol=ticker, outputsize="full")
    return data


def get_crypto_daily(ticker, market="USD"):
    """API returning the daily historical time series for a digital currency (e.g., BTC)

    Arguments:
        ticker {string} -- digital/cryptocurrency ticker symbol

    Keyword Arguments:
        market {str} -- Exchange market you wish to pull the data from for example: CNY-Chinese Yuan (default: {"USD"})

    Returns:
        pandas -- dataframe of daily data refreshed at midnight (UTC).
    """
    data = ts.get_digital_currency_daily(symbol=ticker, market=market)
    return data


def get_percentage_change(ticker):
    """Retrieve the percentage change in 5 minute increments

    Arguments:
        ticker {string} -- unique series of letters assigned to a security for trading purposes

    Returns:
        Pandas -- Formatted dataframe of percent change over 5 minute increments
    """
    data = ts.get_intraday(symbol=ticker, interval="5min", outputsize="full")
    close_data = data["4. close"]
    percentage_change = close_data.pct_change()
    return percentage_change


def set_alert_volatility(ticker, increased_change=0.0008):
    """Day trading alert can be set on watched tickers

    Arguments:
        ticker {string} -- unique series of letters assigned to a security for trading purposes

    Keyword Arguments:
        increased_change {float} -- incremental change you are seeking within the 1 minute increments (default: {0.0008})

    Returns:
        Alert -- returns alert stamped with date & time of incremental change conditional statement
    """
    now = datetime.now()
    alert_message = (
        now.strftime("%I:%M:%S %p")
        + " ALERT "
        + ticker
        + " Has increased above "
        + increased_change
        + " in the last minute"
    )
    data = ts.get_intraday(symbol=ticker, interval="1min", outputsize="full")
    close_data = data["4. close"]
    percentage_change = close_data.pct_change()
    last_change = percentage_change[-1]
    if abs(last_change) > increased_change:
        return alert_message


def get_simple_moving_average_bi_weekly(ticker):
    """arithmetic moving average calculated by adding recent prices and dividing that by the number of time periods

    Arguments:
        ticker {string} -- unique series of letters assigned to a security for trading purposes

    Returns:
        Pandas -- Formatted dataframe of SMA
    """
    data_ti = ti.get_sma(symbol=ticker, interval="daily", time_period=14, series_type="close")
    return data_ti


def get_exponential_moving_average_bi_weekly(ticker):
    """Type of moving average that places a greater weight and significance on most recent data points 

    Arguments:
        ticker {string} -- unique series of letters assigned to a security for trading purposes

    Returns:
        Pandas -- Formatted dataframe of EMA
    """
    data_ti = ti.get_ema(symbol=ticker, interval="daily", time_period=14, series_type="close")
    return data_ti


def get_sma_to_close_indicator(ticker, period=60):
    """Looking for closing price much lower than SMA (betting the stock price will correct itself)

    Arguments:
        ticker {string} -- unique series of letters assigned to a security for trading purposes

    Keyword Arguments:
        period {int} -- number of time periods used to divide for SMA (default: {60})

    Returns:
        pandas -- Formatted data of close price to SMA 
    """
    data_ti = ti.get_sma(symbol=ticker, interval="1min", time_period=period, series_type="close")
    data_ts = ts.get_intraday(symbol=ticker, interval="1min", outputsize="full")
    dataframe1 = data_ti
    dataframe2 = data_ts["4. close"].iloc[
        period - 1 : :
    ]  # Remove first 60 entries to have same amount of values in both frames
    dataframe2.index = dataframe1.index
    total_dataframe = pd.concat([dataframe1, dataframe2], axis=1)
    return total_dataframe
