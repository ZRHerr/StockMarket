import time

import config as cfg
import pandas as pd
from alpha_vantage.timeseries import TimeSeries

api_key = cfg.Secrets["api_key"]

ts = TimeSeries(key=api_key, output_format="pandas")
data, meta_data = ts.get_intraday(symbol="OAS", interval="1min", outputsize="full")
print(data)
