import threading


class ScalpingFirstStrategy(threading.Thread):
    def __init__(self, instrument, marketOperator, stochasticIndicator, rsiIndicator, logger):
        super().__init__()
        self.instrument = instrument
        self.marketOperator = marketOperator
        self.stochasticIndicator = stochasticIndicator
        self.rsiIndicator = rsiIndicator
        self.logger = logger

    def run(self):
        self.stochasticIndicator.start()
        threading.Thread(target=self.buyAnalysis1).start()
        threading.Thread(target=self.sellAnalysis1).start()

    def buyAnalysis1(self):
        while(True):
            secondToWaitStochasticConfirmation = 8
            kAbove = self.stochasticIndicator.kAboveDInLowLimit
            if(kAbove["secondsElapsed"] < secondToWaitStochasticConfirmation or kAbove["triggered"]):
                continue

            numOrder = self.marketOperator.Buy(self.instrument)
            if(numOrder):
                kAbove["triggered"] = True; 
                secondStochastic = kAbove["secondsElapsed"] + kAbove["initTimeStamp"] 
                threading.Thread(target=self.logger.logScalpingFirstStrategyBuyAnalysis1, 
                                  args=(self.instrument, numOrder, secondStochastic, 
                                      self.stochasticIndicator.stochasticKValues, self.stochasticIndicator.stochasticDValues)).start()
                
    def sellAnalysis1(self):
        while(True):
            kBelow = self.stochasticIndicator.kBelowDInUpLimit
            secondToWaitStochasticConfirmation = 8
            if(kBelow["secondsElapsed"] < secondToWaitStochasticConfirmation or kBelow["triggered"]):
                continue

            numOrder = self.marketOperator.Sell(self.instrument)
            if(numOrder): 
                kBelow["triggered"] = True
                secondStochastic = kBelow["secondsElapsed"] + kBelow["initTimeStamp"] 
                threading.Thread(target=self.logger.logScalpingFirstStrategySellAnalysis1, 
                                  args=(self.instrument, numOrder, secondStochastic, 
                                        self.stochasticIndicator.stochasticKValues, self.stochasticIndicator.stochasticDValues)).start()
