import datetime
import MetaTrader5 as mt5

from BackTesting.TicksLevel import TicksLevel

if __name__ == "__main__":
    if not mt5.initialize():
        raise ValueError("No esta inicializado mt5")
    
    ticksLevel = TicksLevel("EURUSDm")
    
    date_start = datetime.datetime(2025, 2, 21, 0, 0, 0)    
    date_end = datetime.datetime(2025, 2, 21, 23, 59, 59)

    ticksLevel.generateListOfTicks(date_start, date_end)