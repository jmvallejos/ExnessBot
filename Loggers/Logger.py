import json
import threading
import time
import os
import winsound

class Logger():
    def __init__(self):
        self.rootPath = "C:/MarketLogs/"
        
    def logScalpingFirstStrategyBuyAnalysis1(self, instrument, numOrder, secondStochastic, stochasticKValues, stochasticDValues):
        threading.Thread(target=lambda: winsound.Beep(1000, 3000)).start()
        
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