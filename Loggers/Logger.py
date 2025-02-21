import json
import time
import os

class Logger():
    def __init__(self):
        self.rootPath = "C:/MarketLogs/"
        
    def logScalpingFirstStrategyBuyAnalysis1(self, instrument, numOrder, secondStochastic, stochasticKValues, stochasticDValues):
        time.sleep(15) 

        pathFile = self.rootPath + "/" + instrument + "/" + str(numOrder) + ".txt"

        with open(pathFile, 'w') as file:
            # Escribir contenido en el archivo
            file.write("Strattegy: FirstStrategy\n\n")
            file.write("Analisys: buyAnalysis1\n\n")
            file.write("Second Stochastic: "+ str(secondStochastic) +"\n\n")
            file.write("StochasticKValues:\n\n")
            file.write(json.dumps(stochasticKValues))
            file.write("\n\n")
            file.write("StochasticDValues:\n\n")
            file.write(json.dumps(stochasticDValues))