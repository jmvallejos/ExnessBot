import datetime
import MetaTrader5 as mt5

from DataGenerators.Mt5PeriodsGenerator import Mt5PeriodsGenerator
from Indicators.EMA.EmaCalculator import EmaCalculator
from Indicators.MACD.MacdCalculator import MacdCalculator
from Indicators.MACD.MacdIndicator import MacdIndicator

if __name__ == "__main__":
    if not mt5.initialize():
        raise ValueError("No esta inicializado mt5")

    periodsGenerator = Mt5PeriodsGenerator("EURUSDm")
    while(True):
        periods = periodsGenerator.generate(1, 75)
        macdIndicator = MacdIndicator(12, 26, 9)
        macdIndicator.CalculateMacd(periods)
        result = macdIndicator.list[-1]
        print(str(result["macd"]) + ' ' +  str(result["macdSignal"]) + ' ' +  str(result["macdHist"]))
            
    