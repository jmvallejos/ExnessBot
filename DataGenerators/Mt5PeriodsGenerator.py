import MetaTrader5 as mt5

class Mt5PeriodsGenerator:
    def __init__(self, instrument):
        self.instrument = instrument
        
    def generate(self, timePeriodInMinutes, numPeriods):
        try:            
            # Obtener las tasas de precios
            periods = []
            timeFrame = None
            if(timePeriodInMinutes == 1):
                timeFrame = mt5.TIMEFRAME_M1

            rates = mt5.copy_rates_from_pos(self.instrument, timeFrame, 0, numPeriods)
            for rate in rates:
                periods.append({
                    "high": float(rate['high']),
                    "low": float(rate['low']),
                    "close": float(rate['close']),
                    "timestamp": int(rate['time'])  
                })
            return periods
        except Exception as e:
            print(f"Ocurrió un error: {e}")
            return []