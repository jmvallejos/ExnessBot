import time
from Indicators.Stochastic.StochasticCalculator import StochasticCalculator

class StochasticIndicator():
    def __init__(self, k_fast, d_fast, d_slow):
        self.k_fast = k_fast
        self.d_fast = d_fast
        self.d_slow = d_slow
        
        self.stochasticKValues = []
        self.stochasticDValues = []
        self.stochasticDSlowValues = []

    def CalculateStochastic(self, periods):
        try:            
            stochasticCalculator = StochasticCalculator()
            stochastic_result = stochasticCalculator.calculateStochastic(periods, self.k_fast, self.d_fast, self.d_slow)
            
            # Agregar valores a las listas
            timestamp = stochastic_result['timestamp']
            self.stochasticKValues.append({'x': timestamp, 'y': stochastic_result['stochasticKValue']})
            self.stochasticDValues.append({'x': timestamp, 'y': stochastic_result['stochasticDValue']})
            self.stochasticDSlowValues.append({'x': timestamp, 'y': stochastic_result['stochasticDSlowValue']})
        except Exception as e:
            print(f"Ocurrió un error: {e}")
            
            
    def CutLists(self):        
        try:
            if(len(self.stochasticKValues) == 0):
                return

            current_timestamp = self.stochasticKValues[-1]["x"]
            cutoff_timestamp = current_timestamp - 600 

            self.stochasticKValues[:] = [item for item in self.stochasticKValues if item["x"] >= cutoff_timestamp]
            self.stochasticDValues[:] = [item for item in self.stochasticDValues if item["x"] >= cutoff_timestamp]
            self.stochasticDSlowValues[:] = [item for item in self.stochasticDSlowValues if item["x"] >= cutoff_timestamp]

        except Exception as e:
            print(f"Ocurrió un error: {e}")