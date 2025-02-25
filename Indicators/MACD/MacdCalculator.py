import pandas as pd


class MacdCalculator:
    def calculate(self, periods, fast, slow, signal):
        df = pd.DataFrame(periods)
        df.reset_index(drop=True, inplace=True)
        df.set_index('timestamp', inplace=True)

        df['EMA_FAST'] = df['close'].ewm(span=fast, adjust=False).mean()
        df['EMA_SLOW'] = df['close'].ewm(span=slow, adjust=False).mean()

        df['MACD'] = df['EMA_FAST'] - df['EMA_SLOW']
        df['MACD_SIGNAL'] = df['MACD'].ewm(span=signal, adjust=False).mean()
        df['MACD_HIST'] = df['MACD'] - df['MACD_SIGNAL']

        last = df.iloc[-1]
        return {
            "timestamp": df.index[-1],
            "macd": round(last["MACD"], 6),
            "macdSignal": round(last["MACD_SIGNAL"], 6),
            "macdHist":  round(last["MACD_HIST"], 6)
        }