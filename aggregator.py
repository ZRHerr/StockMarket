import time

import config as cfg
import pandas as pd
from alpha_vantage.timeseries import TimeSeries

api_key = cfg.Secrets["api_key"]

ts = TimeSeries(key=api_key, output_format="pandas")
# Testing API
data, meta_data = ts.get_intraday(symbol="OAS", interval="1min", outputsize="full")
print(data)


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
    data = ts.get_digital_currency_daily(ticker=ticker, market=market)
    return data
