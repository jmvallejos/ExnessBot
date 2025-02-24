import time
import MetaTrader5 as mt5
from Indicators.EMA.EmaIndicator import EmaIndicator
from Indicators.RSI.RsiIndicator import RsiIndicator
from Indicators.Stochastic.StochasticIndicator import StochasticIndicator
from Loggers.Logger import Logger
from MarketOperator.Mt5Operator import Mt5Operator
from Strategies.Scalping.ScalpingFirstStrategy import ScalpingFirstStrategy
from DataGenerators.Mt5PeriodsGenerator import Mt5PeriodsGenerator

def ScalpingFirstStrategyBuilder(instrument, marketOperator, logger):
    periodsGenerator = Mt5PeriodsGenerator(instrument)

    rsiIndicator = RsiIndicator(5)
    emaIndicator = EmaIndicator()

    strateggy = ScalpingFirstStrategy(instrument, marketOperator, periodsGenerator, rsiIndicator, emaIndicator, logger)
    
    strateggy.start()

if __name__ == "__main__":
    if not mt5.initialize():
        raise ValueError("No esta inicializado mt5")
    
    logger = Logger()
    marketOperator = Mt5Operator()

    ScalpingFirstStrategyBuilder("EURUSDm", marketOperator, logger)
    ScalpingFirstStrategyBuilder("USDJPYm", marketOperator, logger)
    ScalpingFirstStrategyBuilder("GBPUSDm", marketOperator, logger)
    ScalpingFirstStrategyBuilder("USDCHFm", marketOperator, logger)
    ScalpingFirstStrategyBuilder("AUDUSDm", marketOperator, logger)
    ScalpingFirstStrategyBuilder("USDCADm", marketOperator, logger)
    ScalpingFirstStrategyBuilder("NZDUSDm", marketOperator, logger)
    ScalpingFirstStrategyBuilder("EURGBPm", marketOperator, logger)
    ScalpingFirstStrategyBuilder("EURJPYm", marketOperator, logger)
    ScalpingFirstStrategyBuilder("GBPJPYm", marketOperator, logger)
        
    while(True):
        time.sleep(60)

