import time
import pandas as pd
import numpy as np

class StochasticCalculator:
    def calculateStochastic(self, periods, fastK, fastD, slowD):
        # Convert the list of periods into a DataFrame
        df = pd.DataFrame(periods)

        # Configurar 'timestamp' como índice, convirtiendo el timestamp a formato de fecha
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')  
        df.set_index('timestamp', inplace=True)  
    
        # Calculate the stochastic manually
        df['highest_high'] = df['high'].rolling(window=fastK).max()
        df['lowest_low'] = df['low'].rolling(window=fastK).min()
        df['%K'] = 100 * ((df['close'] - df['lowest_low']) / (df['highest_high'] - df['lowest_low']))
        df['%D'] = df['%K'].rolling(window=fastD).mean()
        df['%D_slow'] = df['%D'].rolling(window=slowD).mean()

        # Get the last value of the stochastic
        lastValue = df.iloc[-1]
        return {
            "stochasticKValue": float(lastValue['%K']), 
            "stochasticDValue": float(lastValue['%D']),
            "stochasticDSlowValue": float(lastValue['%D_slow']),
            "timestamp": int(lastValue["timestamp"])      
        }