import time

import config as cfg
import pandas as pd
from alpha_vantage.techindicators import TechIndicators

api_key = cfg.Secrets["api_key"]

ti = TechIndicators(key=api_key, output_format="pandas")


def get_simple_moving_average_bi_weekly(ticker):
    """arithmetic moving average calculated by adding recent prices and dividing that by the number of time periods

    Arguments:
        ticker {string} -- unique series of letters assigned to a security for trading purposes

    Returns:
        Pandas -- Formatted dataframe of SMA
    """
    data = ti.get_sma(ticker=ticker, interval="daily", time_period=14, series_type="close")
    return data


def get_exponential_moving_average_bi_weekly(ticker):
    """Type of moving average that places a greater weight and significance on most recent data points 

    Arguments:
        ticker {string} -- unique series of letters assigned to a security for trading purposes

    Returns:
        Pandas -- Formatted dataframe of EMA
    """
    data = ti.get_ema(ticker=ticker, interval="daily", time_period=14, series_type="close")
    return data


# looking to create custom indicators will come back to this after working on some more of the ground-work.
