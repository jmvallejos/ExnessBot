import threading
import time

from Indicators.RSI.RsiCalculator import RsiCalculator

class RsiIndicator(threading.Thread):
    def __init__(self, period_generator, numPeriod):
        super().__init__()
        self.period_generator = period_generator
        self.numPeriod = numPeriod
        self.list = [] 

    def run(self):
        threading.Thread(target=self.CalculateRsi).start()
        threading.Thread(target=self.CutLists).start()

    def CalculateRsi(self):
        # Bucle para calcular estocástico cada segundo
        while True:
            self.period_generator.generate()
            
            # Instanciar StochasticGenerator y calcular el estocástico
            rsiCalculator = RsiCalculator()
            rsiResult = rsiCalculator.calculate(self.period_generator.periods, self.numPeriod)
            
            # Agregar valores a las listas
            timestamp = rsiResult['timestamp']
            self.list.append({'x': timestamp, 'y': rsiResult['rsiValue']})
            self.EvaluateResult(rsiResult)

    def EvaluateResult(self, rsiResult):
        print(round(rsiResult["rsiValue"], 2))

    def CutLists(self):
        while(True):
            if(len(self.list) == 0):
                continue

            current_timestamp = self.list[-1]["x"]
            cutoff_timestamp = current_timestamp - 600 

            self.list[:] = [item for item in self.list if item["x"] >= cutoff_timestamp]
            
            time.sleep(60)
