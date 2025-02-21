import threading


class ScalpingFirstStrategy(threading.Thread):
    def __init__(self, instrument, marketOperator, stochasticIndicator):
        super().__init__()
        self.instrument = instrument
        self.stochasticIndicator = None
        self.marketOperator = marketOperator
        self.stochasticIndicator = stochasticIndicator
        
    def run(self):
        self.stochasticIndicator.start()
        threading.Thread(target=self.buyAnalysis1).start()

    def buyAnalysis1(self):
        while(True):
            if(self.stochasticIndicator.kAboveDInLowLimit["secondsElapsed"] > 1):
                numOrder = self.marketOperator.Buy(self.instrument)
                if(numOrder):    
                    print("se va a logear")

