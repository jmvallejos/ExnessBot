import threading
import time
from datetime import datetime, timedelta
from Indicators.Stochastic.StochasticCalculator import StochasticCalculator

class StochasticIndicator(threading.Thread):
    def __init__(self, period_generator, k_fast, d_fast, d_slow):
        super().__init__()
        self.period_generator = period_generator
        self.k_fast = k_fast
        self.d_fast = d_fast
        self.d_slow = d_slow
        
        self.stochasticKValues = []
        self.stochasticDValues = []
        self.stochasticDSlowValues = []
    
        self.kAboveDInLowLimit = {
            "initTimeStamp": 0,
            "secondsElapsed": 0,
            "triggered": False
        }

        self.kBelowDInUpLimit = {
            "initTimeStamp": 0,
            "secondsElapsed": 0,
            "triggered": False
        }

    def run(self):
        threading.Thread(target=self.CalculateStochastic).start()
        threading.Thread(target=self.CutLists).start()


    def CalculateStochastic(self):
        # Bucle para calcular estocástico cada segundo
        while True:
            self.period_generator.generate()
            
            # Instanciar StochasticGenerator y calcular el estocástico
            stochasticCalculator = StochasticCalculator()
            stochastic_result = stochasticCalculator.calculateStochastic(self.period_generator.periods, self.k_fast, self.d_fast, self.d_slow)
            
            # Agregar valores a las listas
            timestamp = stochastic_result['timestamp']
            self.stochasticKValues.append({'x': timestamp, 'y': stochastic_result['stochasticKValue']})
            self.stochasticDValues.append({'x': timestamp, 'y': stochastic_result['stochasticDValue']})
            self.stochasticDSlowValues.append({'x': timestamp, 'y': stochastic_result['stochasticDSlowValue']})
            self.EvaluateResult(stochastic_result)

    def EvaluateResult(self, result):
        self.setkAboveDInLowLimit(result)
        self.setkBelowDInUpLimit(result)

    def setkAboveDInLowLimit(self,result):
        if(self.kAboveDInLowLimit["initTimeStamp"] == 0 and result['stochasticKValue'] > 20):
            return
        
        if(result['stochasticKValue'] >= result['stochasticDValue']):
            if(self.kAboveDInLowLimit["initTimeStamp"] == 0):
                self.kAboveDInLowLimit["initTimeStamp"] = result['timestamp']
            else:
                self.kAboveDInLowLimit["secondsElapsed"] = result['timestamp'] - self.kAboveDInLowLimit["initTimeStamp"]
        else:
            self.kAboveDInLowLimit["initTimeStamp"] = 0
            self.kAboveDInLowLimit["secondsElapsed"] = 0
            self.kAboveDInLowLimit["triggered"] = False

    def setkBelowDInUpLimit(self,result):
        if(self.kBelowDInUpLimit["initTimeStamp"] == 0 and result['stochasticKValue'] < 80):
            return
        
        if(result['stochasticKValue'] <= result['stochasticDValue']):
            if(self.kBelowDInUpLimit["initTimeStamp"] == 0):
                self.kBelowDInUpLimit["initTimeStamp"] = result['timestamp']
            else:
                self.kBelowDInUpLimit["secondsElapsed"] = result['timestamp'] - self.kBelowDInUpLimit["initTimeStamp"]
        else:
            self.kBelowDInUpLimit["initTimeStamp"] = 0
            self.kBelowDInUpLimit["secondsElapsed"] = 0
            self.kBelowDInUpLimit["triggered"] = False

    def CutLists(self):
        while(True):
            if(len(self.stochasticKValues) == 0):
                continue

            current_timestamp = self.stochasticKValues[-1]["x"]
            cutoff_timestamp = current_timestamp - 600 

            self.stochasticKValues[:] = [item for item in self.stochasticKValues if item["x"] >= cutoff_timestamp]
            self.stochasticDValues[:] = [item for item in self.stochasticDValues if item["x"] >= cutoff_timestamp]
            self.stochasticDSlowValues[:] = [item for item in self.stochasticDSlowValues if item["x"] >= cutoff_timestamp]
            
            time.sleep(60) 