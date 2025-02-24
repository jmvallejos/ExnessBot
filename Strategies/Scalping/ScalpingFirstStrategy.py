import json
import threading
import time
import MetaTrader5 as mt5

class ScalpingFirstStrategy(threading.Thread):
    def __init__(self, instrument, marketOperator, periodsGenerator, 
                 rsiIndicator, emaIndicator, logger):
        super().__init__()
        self.instrument = instrument
        self.marketOperator = marketOperator
        self.periodsGenerator = periodsGenerator
        self.rsiIndicator = rsiIndicator
        self.emaIndicator = emaIndicator
        self.logger = logger
        self.currentRsiBuyAlert = None
        self.currentRsiSellAlert = None

    def run(self):
        threading.Thread(target=self.runIndicators).start()
        threading.Thread(target=self.buyAnalysis1).start()
        threading.Thread(target=self.sellAnalysis1).start()

    def runIndicators(self):
        init = time.time()
        while(True):
            periods = self.periodsGenerator.generate(1, 50)
            self.rsiIndicator.CalculateRsi(periods)
            self.emaIndicator.CalculateEma(periods)

            if((init - time.time()) % 600):
                self.rsiIndicator.CutLists()
                self.emaIndicator.CutLists()


    def buyAnalysis1(self):
        init = int(time.time())
        while(True):
            try:
                if((init - time.time()) % 10):
                    print(self.instrument + ' buyAnalysis1 healthy')

                if(len(self.rsiIndicator.list) == 0):
                    continue

                currentRsi = self.rsiIndicator.list[-1]
                if(currentRsi["y"] < 30):
                    continue
                
                
                lastRsiItemBelow30 = None 
                for item in reversed(self.rsiIndicator.list):
                    if item["y"] < 30:
                        lastRsiItemBelow30 = item
                        break

                if(lastRsiItemBelow30 is None or currentRsi["x"] - lastRsiItemBelow30["x"] > 60):
                    continue
                

                if(self.currentRsiBuyAlert is not None and self.currentRsiBuyAlert["x"] == lastRsiItemBelow30["x"]):
                    return
                
                currentEma9 = self.emaIndicator.ema9[-1]["y"]
                currentEma21 = self.emaIndicator.ema21[-1]["y"]

                if(currentEma9 > currentEma21):
                    continue
                
                
                init = time.time()
                ema9CrossedToEma21 = False
                while(True):

                    currentEma9 = self.emaIndicator.ema9[-1]["y"]
                    currentEma21 = self.emaIndicator.ema21[-1]["y"]
                    
                    if(currentEma9 > currentEma21):
                        ema9CrossedToEma21 = True
                        break

                    if(time.time() - init > 480): #si ya pasaron 8 minutos salgo del bucle
                        break
                
                if(ema9CrossedToEma21 == False):
                    return

                i = 1
                response = None
                while(i <= 5):
                    i = i+1
                    response = self.marketOperator.Buy(self.instrument)
                    if(response.order is not None and response.order > 0):
                        break

                if(response.order > 0):
                    self.currentRsiBuyAlert = lastRsiItemBelow30
                    orderTime = currentRsi["x"]
                    threading.Thread(target=self.logger.log, 
                                    args=(self.instrument, response.order, orderTime, "ScalpingFirstStrategy", "buyAnalisys1", self.rsiIndicator.list)).start()
            except Exception as e:    
                print(f"Ocurrió un error: {e}")
                continue

    def sellAnalysis1(self):
        init = time.time()
        while(True):
            try:
                if((init - time.time()) % 10):
                    print(self.instrument + ' buyAnalysis1 healthy')

                if(len(self.rsiIndicator.list) == 0):
                    continue

                currentRsi = self.rsiIndicator.list[-1]
                if(currentRsi["y"] > 70):
                    continue
                
                lastRsiItemUp70 = None 
                for item in reversed(self.rsiIndicator.list):
                    if item["y"] > 70:
                        lastRsiItemUp70 = item
                        break

                if(lastRsiItemUp70 is None or currentRsi["x"] - lastRsiItemUp70["x"] > 60):
                    continue

                if(self.currentRsiSellAlert is not None and self.currentRsiSellAlert["x"] == lastRsiItemUp70["x"]):
                    return
                
                currentEma9 = self.emaIndicator.ema9[-1]["y"]
                currentEma21 = self.emaIndicator.ema21[-1]["y"]

                if(currentEma9 < currentEma21):
                    continue
                    
                init = time.time()
                ema9CrossedToEma21 = False
                while(True):
                    currentEma9 = self.emaIndicator.ema9[-1]["y"]
                    currentEma21 = self.emaIndicator.ema21[-1]["y"]
                    
                    if(currentEma9 < currentEma21):
                        ema9CrossedToEma21 = True
                        break

                    if(time.time() - init > 480): #si ya pasaron 8 minutos salgo del bucle
                        break
                
                if(ema9CrossedToEma21 == False):
                    return

                i = 1
                response = None
                while(i <= 5):
                    i = i+1
                    response = self.marketOperator.Sell(self.instrument)
                    if(response.order is not None and response.order > 0):
                        break
                
                if(response.order > 0):
                    self.currentRsiBuyAlert = lastRsiItemUp70
                    orderTime = currentRsi["x"]
                    threading.Thread(target=self.logger.log, 
                                    args=(self.instrument, response.order, orderTime, "ScalpingFirstStrategy", "sellAnalisys1", self.rsiIndicator.list)).start()
            except Exception as e:    
                print(f"Ocurrió un error: {e}")
                continue