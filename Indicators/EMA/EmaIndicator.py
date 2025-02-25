import threading
import time

from Indicators.EMA.EmaCalculator import EmaCalculator


class EmaIndicator():
    def __init__(self, principal, secundary):
        self.list = [] 
        self.principal = principal
        self.secundary = secundary

        self.CrossUp = None
        self.CrossDown = None
        

    def CalculateEma(self, periods):
        try:            
            emaCalculator = EmaCalculator()
            emaResult = emaCalculator.calculate(periods, self.principal, self.secundary)            
            self.EvaluateResult(emaResult)
            self.list.append(emaResult)
        except Exception as e:
            print(f"Ocurrió un error: {e}")

    def EvaluateResult(self, result):
        if(len(self.list) == 0):
            return
        
        lastItem = self.list[-1]
        if(lastItem["principal"] <= lastItem["secundary"] and result["principal"] > result["secundary"]):
            self.CrossUp = result

        if(lastItem["principal"] >= lastItem["secundary"] and result["principal"] < result["secundary"]):
            self.CrossDown = result

    def CutLists(self):
        try:
            current_timestamp = self.list[-1]["timestamp"]
            cutoff_timestamp = current_timestamp - 600 
            self.list[:] = [item for item in self.list if item["timestamp"] >= cutoff_timestamp]
        
        except Exception as e:
            print(f"Ocurrió un error: {e}")
