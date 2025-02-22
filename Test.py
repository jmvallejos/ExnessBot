import MetaTrader5 as mt5
from DataGenerators.Mt5PeriodsGenerator import Mt5PeriodsGenerator
from Indicators.RSI.RsiIndicator import RsiIndicator
from Indicators.Stochastic.StochasticIndicator import StochasticIndicator
from MarketOperator.Mt5Operator import Mt5Operator;

if __name__ == "__main__":
    if not mt5.initialize():
        raise ValueError("No esta inicializado mt5")
    
    period_generator = Mt5PeriodsGenerator("BTCUSDm", 1, 20)
    rsiIndicator = RsiIndicator(period_generator, 14)    
    rsiIndicator.start()
    rsiIndicator.join()
    
    
        
    
    

