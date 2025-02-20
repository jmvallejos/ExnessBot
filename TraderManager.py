import MetaTrader5 as mt5
from Indicators.Stochastic.StochasticIndicator import StochasticIndicator

if __name__ == "__main__":
    if not mt5.initialize():
        raise ValueError("No esta inicializado mt5")
    
    stochasticIndicator = StochasticIndicator("BTCUSDm", 1, 25,14,3,3)
    stochasticIndicator.start()
    stochasticIndicator.join()