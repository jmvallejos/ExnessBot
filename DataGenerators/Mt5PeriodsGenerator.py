import MetaTrader5 as mt5

class Mt5PeriodsGenerator:
    def __init__(self, instrument, timePeriodInMinutes, numPeriods):
        self.instrument = instrument
        self.timePeriodInMinutes = timePeriodInMinutes
        self.numPeriods = numPeriods
        
    def generate(self):
        # Obtener las tasas de precios
        self.periods = []
        timeFrame = None
        if(self.timePeriodInMinutes == 1):
            timeFrame = mt5.TIMEFRAME_M1

        rates = mt5.copy_rates_from_pos(self.instrument, timeFrame, 0, self.numPeriods)
        for rate in rates:
            self.periods.append({
                "high": float(rate['high']),
                "low": float(rate['low']),
                "close": float(rate['close']),
                "timestamp": int(rate['time'])  # Usamos el timestamp del final del periodo
            })
