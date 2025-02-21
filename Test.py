import MetaTrader5 as mt5
from DataGenerators.Mt5PeriodsGenerator import Mt5PeriodsGenerator
from Indicators.Stochastic.StochasticIndicator import StochasticIndicator;



if __name__ == "__main__":
    if not mt5.initialize():
        raise ValueError("No esta inicializado mt5")
    
    period_generator = Mt5PeriodsGenerator("BTCUSDm", 1, 25)
    stochasticIndicator = StochasticIndicator(period_generator, "BTCUSDm", 14, 3, 3)
    stochasticIndicator.start()
    listaK = stochasticIndicator.stochasticKValues
    listaD = stochasticIndicator.stochasticDValues
    
    while True:
        continue    
    
    

