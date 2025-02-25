import json
import threading
import time
import MetaTrader5 as mt5

class ScalpingFirstStrategy(threading.Thread):
    def __init__(self, instrument, marketOperator, periodsGenerator, emaIndicator, rsiIndicator, logger):
        super().__init__()
        self.instrument = instrument
        self.marketOperator = marketOperator
        self.periodsGenerator = periodsGenerator
        self.emaIndicator = emaIndicator
        self.rsiIndicator = rsiIndicator
        self.logger = logger

        self.emaBuySignal = None
        self.emaSellSignal = None 

    def run(self):
        while(True):
            self.runIndicators()
            self.buyAnalysis1()
            self.sellAnalysis1()
        
    def runIndicators(self):
        periods = self.periodsGenerator.generate(1, 50)
        self.emaIndicator.CalculateEma(periods)
        self.rsiIndicator.CalculateRsi(periods)

        if(len(self.emaIndicator.list) == 0 or len(self.rsiIndicator.list) == 0):
            return
        
        if(time.time() - self.emaIndicator.list[0]["timestamp"] > 2700):
            self.emaIndicator.CutLists()
            self.rsiIndicator.CutLists()

    def buyAnalysis1(self):
        try:
            ema = self.emaIndicator.list[-1]
            #solo interesa si ema principal esta por encima de ema secundaria
            if(ema["principal"] < ema["secundary"]):
                return
            
            #encuentro el item donde se produjo el cruce.
            emaCross = self.emaIndicator.CrossUp
            if(emaCross is None):
                return
            
            #si el cruce ocurrio hace menos de 3 segundos retorno.
            if(ema["timestamp"] - emaCross["timestamp"] <= 3):
                return
            
            #si el cruce ocurrio hace mas de 30 segundos retorno.
            if(ema["timestamp"] - emaCross["timestamp"] >= 30):
                return
            
            #si el cruce es el mismo que disparó el ultimo evento de compra, retorno.
            if(self.emaBuySignal is not None and emaCross["timestamp"] == self.emaBuySignal["timestamp"]):
                return
            
            rsi = self.rsiIndicator.list[-1]
            crossRsi = self.rsiIndicator.crossDownLimit

            if(crossRsi is None):
                return
            
            if(rsi["timestamp"] - crossRsi["timestamp"] > 480):
                return

            #Compro la accion y guardo la señal de compra
            buySuccess = self.marketOperator.Buy(self.instrument)
            if(buySuccess):
                self.emaBuySignal = emaCross

        except Exception as e:    
            print(f"Ocurrió un error: {e}")
            

    def sellAnalysis1(self):        
        try:
            ema = self.emaIndicator.list[-1]
            
            #solo interesa si ema principal esta por debajo de ema secundaria
            if(ema["principal"] > ema["secundary"]):
                return
            
            #encuentro el item donde se produjo el cruce.
            emaCross = self.emaIndicator.CrossDown
            if(emaCross is None):
                return
            
            #si el cruce ocurrio hace menos de 5 segundos retorno.
            if(ema["timestamp"] - emaCross["timestamp"] <= 5):
                return
            
            #si el cruce ocurrio hace mas de 30 segundos retorno.
            if(ema["timestamp"] - emaCross["timestamp"] >= 30):
                return
            
            #si el cruce es el mismo que disparó el ultimo evento de venta, retorno.
            if(self.emaSellSignal is not None and emaCross["timestamp"] == self.emaSellSignal["timestamp"]):
                return
            
            rsi = self.rsiIndicator.list[-1]
            crossRsi = self.rsiIndicator.crossUpLimit

            if(crossRsi is None):
                return
            
            if(rsi["timestamp"] - crossRsi["timestamp"] > 480):
                return

            #Vendo la accion y guardo la señal de venta
            sellSuccess = self.marketOperator.Sell(self.instrument)
            if(sellSuccess):
                self.emaSellSignal = emaCross

        except Exception as e:    
            print(f"Ocurrió un error: {e}")
        