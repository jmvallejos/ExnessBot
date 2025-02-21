import threading


class ScalpingFirstStrategy(threading.Thread):
    def __init__(self, instrument, marketOperator, stochasticIndicator, logger):
        super().__init__()
        self.instrument = instrument
        self.stochasticIndicator = None
        self.marketOperator = marketOperator
        self.stochasticIndicator = stochasticIndicator
        self.logger = logger

    def run(self):
        self.stochasticIndicator.start()
        threading.Thread(target=self.buyAnalysis1).start()

    def buyAnalysis1(self):
        while(True):
            secondToWaitStochasticConfirmation = 1
            if(self.stochasticIndicator.kAboveDInLowLimit["secondsElapsed"] < secondToWaitStochasticConfirmation):
                continue

            numOrder = self.marketOperator.Buy(self.instrument)
            if(numOrder): 
                secondStochastic = self.stochasticIndicator.kAboveDInLowLimit["secondsElapsed"] + self.stochasticIndicator.kAboveDInLowLimit["initTimeStamp"] 
                threading.Thread(target=self.logger.logScalpingFirstStrategyBuyAnalysis1, 
                                  args=(self.instrument, numOrder, secondStochastic, 
                                        self.stochasticKValues, self.stochasticDValues)).start()
