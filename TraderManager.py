import time
import MetaTrader5 as mt5
from Indicators.Stochastic.StochasticIndicator import StochasticIndicator
from MarketOperator.Mt5Operator import Mt5Operator
from Strategies.Scalping.ScalpingFirstStrategy import ScalpingFirstStrategy
from DataGenerators.Mt5PeriodsGenerator import Mt5PeriodsGenerator

def ScalpingFirstStrategyBuilder(instrument, marketOperator):
    periodTimeInMinutes = 1
    minPeriods = 25
    period_generator = Mt5PeriodsGenerator(instrument, periodTimeInMinutes, minPeriods)
    stochasticIndicator = StochasticIndicator(period_generator, instrument, 1, 25, 14, 3, 3)
    strateggy = ScalpingFirstStrategy(instrument, marketOperator, stochasticIndicator)

    strateggy.start()

if __name__ == "__main__":
    if not mt5.initialize():
        raise ValueError("No esta inicializado mt5")
    
    marketOperator = Mt5Operator()
    marketOperator.start()

    ScalpingFirstStrategyBuilder("BTCUSDm", marketOperator)
    #ScalpingFirstStrategyBuilder("ETHUSDm", marketOperator)

    while(True):
        time.sleep(60)

