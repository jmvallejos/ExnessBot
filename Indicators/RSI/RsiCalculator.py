import time
import pandas as pd
import numpy as np

class RsiCalculator:
    def calculate(self, periods, numPeriod):
        df = pd.DataFrame(periods)
        
        window_rsi = numPeriod
        delta = df['close'].diff()
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)

        # Use EMA instead of SMA
        gain_ema = gain.ewm(alpha=1/window_rsi, adjust=False).mean()
        loss_ema = loss.ewm(alpha=1/window_rsi, adjust=False).mean()

        rs = gain_ema / loss_ema
        df['rsi'] = 100 - (100 / (1 + rs))
        last = df.iloc[-1]

        return {"timestamp": int(time.time()) ,"value" : round(float(last["rsi"]),5)}