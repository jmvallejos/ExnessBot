import threading
import time

from Indicators.EMA.EmaCalculator import EmaCalculator


class EmaIndicator(threading.Thread):
    def __init__(self):
        super().__init__()   
        self.ema9 = []
        self.ema21 = [] 

    def run(self):
        threading.Thread(target=self.CalculateEma).start()
        threading.Thread(target=self.CutLists).start()
    
    def CalculateEma(self, periods):
        try:            
            emaCalculator = EmaCalculator()
            emaResult = emaCalculator.calculate(periods)
            
            timestamp = emaResult['timestamp']
            self.ema9.append({'x': timestamp, 'y': emaResult['ema9']})
            self.ema21.append({'x': timestamp, 'y': emaResult['ema21']})

        except Exception as e:
            print(f"Ocurrió un error: {e}")

    def CutLists(self):
        try:
            if(len(self.ema9) == 0 or len(self.ema21) == 0):
                return

            current_timestamp = self.ema9[-1]["x"]
            cutoff_timestamp = current_timestamp - 600 

            self.ema9[:] = [item for item in self.ema9 if item["x"] >= cutoff_timestamp]
            self.ema21[:] = [item for item in self.ema21 if item["x"] >= cutoff_timestamp]

        except Exception as e:
            print(f"Ocurrió un error: {e}")
