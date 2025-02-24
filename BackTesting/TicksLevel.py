import MetaTrader5 as mt5
import pandas as pd

class TicksLevel:
    def __init__(self, instrument):
        self.instrument = instrument
        self.ticks = None

    def generateListOfTicks(self, dateStart, dateEnd):
        ticks = mt5.copy_ticks_range(self.instrument, dateStart, dateEnd, mt5.COPY_TICKS_ALL)
        self.ticks = pd.DataFrame(ticks)

