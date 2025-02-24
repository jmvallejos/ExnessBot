import time
import pandas as pd
import talib
import numpy as np

class EmaCalculator():

    def calculate(self, periods):
        closing_prices = np.array([item["close"] for item in periods])

        ema_21 = talib.EMA(closing_prices, timeperiod=21)[-1]
        ema_9 = talib.EMA(closing_prices, timeperiod=9)[-1]

        return {"timestamp": int(time.time()), "ema9" : round(float(ema_9),4), "ema21" : round(float(ema_21),4)}