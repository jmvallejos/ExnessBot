import time
import MetaTrader5 as mt5
from Indicators.Stochastic.StochasticIndicator import StochasticIndicator
from Loggers.Logger import Logger
from MarketOperator.Mt5Operator import Mt5Operator
from Strategies.Scalping.ScalpingFirstStrategy import ScalpingFirstStrategy
from DataGenerators.Mt5PeriodsGenerator import Mt5PeriodsGenerator

def ScalpingFirstStrategyBuilder(instrument, marketOperator, logger):
    periodTimeInMinutes = 1
    minPeriods = 25
    k_fast = 14
    d_fast = 3
    d_slow = 3
    period_generator = Mt5PeriodsGenerator(instrument, periodTimeInMinutes, minPeriods)
    stochasticIndicator = StochasticIndicator(period_generator, instrument, k_fast, d_fast, d_slow)
    strateggy = ScalpingFirstStrategy(instrument, marketOperator, stochasticIndicator, logger)

    strateggy.start()

if __name__ == "__main__":
    if not mt5.initialize():
        raise ValueError("No esta inicializado mt5")
    
    logger = Logger()
    marketOperator = Mt5Operator()
    marketOperator.start()

    ScalpingFirstStrategyBuilder("BTCUSDm", marketOperator, logger)
    ScalpingFirstStrategyBuilder("ETHUSDm", marketOperator, logger)

    while(True):
        time.sleep(60)

