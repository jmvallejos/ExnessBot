import time
import pandas as pd
import talib
import numpy as np

class EmaCalculator():

    def calculate(self, periods, pricipal, secundary):
        closing_prices = np.array([item["close"] for item in periods])

        principal = talib.EMA(closing_prices, timeperiod=pricipal)[-1]
        secundary = talib.EMA(closing_prices, timeperiod=secundary)[-1]

        return {"timestamp": int(time.time()), "principal" : round(float(principal),5), "secundary" : round(float(secundary),5)}