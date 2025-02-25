import time

from Indicators.RSI.RsiCalculator import RsiCalculator

class RsiIndicator():
    def __init__(self, numPeriod, upLimit, downLimit):
        self.numPeriod = numPeriod
        self.upLimit = upLimit
        self.downLimit = downLimit
        self.list = [] 
        
        self.crossUpLimit = None
        self.crossDownLimit = None

    def CalculateRsi(self, periods):
        try:            
            rsiCalculator = RsiCalculator()
            rsiResult = rsiCalculator.calculate(periods, self.numPeriod)
            self.EvaluateResult(rsiResult)
            self.list.append(rsiResult)
        except Exception as e:    
            print(f"Ocurrió un error: {e}")

    def EvaluateResult(self, result):
        if(len(self.list) == 0):
            return
        
        lastRsi = self.list[-1]
        if(lastRsi["value"] >= self.upLimit and result["value"] < self.upLimit):
            self.crossUpLimit = result

        if(lastRsi["value"] <= self.downLimit and result["value"] > self.downLimit):
            self.crossDownLimit = result

    def CutLists(self):
        try:
            current_timestamp = self.list[-1]["timestamp"]
            cutoff_timestamp = current_timestamp - 600 
            self.list[:] = [item for item in self.list if item["timestamp"] >= cutoff_timestamp]
        except Exception as e:    
            print(f"Ocurrió un error: {e}")
