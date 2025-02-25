import datetime
import MetaTrader5 as mt5

from DataGenerators.Mt5PeriodsGenerator import Mt5PeriodsGenerator
from Indicators.EMA.EmaCalculator import EmaCalculator

if __name__ == "__main__":
    if not mt5.initialize():
        raise ValueError("No esta inicializado mt5")

    periodsGenerator = Mt5PeriodsGenerator("EURUSDm")
    while(True):
        periodTest1 = periodsGenerator.generate(1, 50)

        emaCalculator = EmaCalculator()

        resultTest1 = emaCalculator.calculate(periodTest1, 3, 9)
        print('\n')
        print(str(resultTest1["principal"]))
            
    