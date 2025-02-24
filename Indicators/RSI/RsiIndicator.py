import time

from Indicators.RSI.RsiCalculator import RsiCalculator

class RsiIndicator():
    def __init__(self, numPeriod):
        self.numPeriod = numPeriod
        self.list = [] 

    def CalculateRsi(self, periods):
        try:            
            rsiCalculator = RsiCalculator()
            rsiResult = rsiCalculator.calculate(periods, self.numPeriod)
            
            timestamp = rsiResult['timestamp']
            self.list.append({'x': timestamp, 'y': rsiResult['rsiValue']})
        except Exception as e:    
            print(f"Ocurrió un error: {e}")

    def CutLists(self):
        try:
            if(len(self.list) == 0):
                return

            current_timestamp = self.list[-1]["x"]
            cutoff_timestamp = current_timestamp - 600 

            self.list[:] = [item for item in self.list if item["x"] >= cutoff_timestamp]
        except Exception as e:    
            print(f"Ocurrió un error: {e}")
