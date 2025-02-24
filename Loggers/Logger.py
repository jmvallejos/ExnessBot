import json
import threading
import time
import os
import winsound
import pandas as pd
from datetime import datetime, timezone

class Logger():
    def __init__(self):
        self.rootPath = "C:/MarketLogs/"
        
    def log(self, instrument, numOrder, orderTime, strateggy, analisys, rsiList):
        try:
            threading.Thread(target=lambda: winsound.Beep(1000, 3000)).start()
            pathFile = self.rootPath + "/" + instrument + "/" + str(numOrder) + ".txt"

            with open(pathFile, 'w') as file:
                # Escribir contenido en el archivo
                file.write("Strattegy: "+strateggy+"\n\n")
                file.write("Analisys: "+analisys+"\n\n")
                file.write("Order Time: "+ str(orderTime) +"\n\n")
                file.write("Rsi: \n\n"+ json.dumps(rsiList) +"\n\n")
        except Exception as e:    
            print(f"Ocurrió un error: {e}")

    def logEvent(self, instrument, strateggy, analisys, message):
        try:
            pathFile = self.rootPath + "/" + instrument + "/" + strateggy + "_" + analisys + ".txt"
            hora_utc = datetime.now(timezone.utc).strftime("%H:%M:%S")
            with open(pathFile, 'a') as file:
                file.write(hora_utc+ ' ' +message+"\n")
        except Exception as e:    
            print(f"Ocurrió un error: {e}")