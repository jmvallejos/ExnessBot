import time
import MetaTrader5 as mt5
from Indicators.RSI.RsiIndicator import RsiIndicator
from Indicators.Stochastic.StochasticIndicator import StochasticIndicator
from Loggers.Logger import Logger
from MarketOperator.Mt5Operator import Mt5Operator
from Strategies.Scalping.ScalpingFirstStrategy import ScalpingFirstStrategy
from DataGenerators.Mt5PeriodsGenerator import Mt5PeriodsGenerator

def ScalpingFirstStrategyBuilder(instrument, marketOperator, logger):
    period_generator = Mt5PeriodsGenerator(instrument, 1, 25)
    stochasticIndicator = StochasticIndicator(period_generator, 14, 3, 3)

    period_generator = Mt5PeriodsGenerator(instrument, 1, 14)
    rsiIndicator = RsiIndicator(period_generator)
    strateggy = ScalpingFirstStrategy(instrument, marketOperator, stochasticIndicator, rsiIndicator, logger)
    
    strateggy.start()

if __name__ == "__main__":
    if not mt5.initialize():
        raise ValueError("No esta inicializado mt5")
    
    logger = Logger()
    marketOperator = Mt5Operator()
    marketOperator.start()

    ScalpingFirstStrategyBuilder("BTCUSDm", marketOperator, logger)
    
    while(True):
        time.sleep(60)

