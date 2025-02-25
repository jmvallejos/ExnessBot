from Indicators.MACD.MacdCalculator import MacdCalculator


class MacdIndicator():
    def __init__(self, fast, slow, signal):
        self.list = []
        self.fast = fast
        self.slow = slow
        self.signal = signal

    def CalculateMacd(self, periods):
        try:            
            macdCalculator = MacdCalculator()
            macdResult = macdCalculator.calculate(periods, self.fast, self.slow, self.signal)            
            self.list.append(macdResult)
        except Exception as e:
            print(f"Ocurrió un error: {e}")

    def CutLists(self):
        try:
            current_timestamp = self.list[-1]["timestamp"]
            cutoff_timestamp = current_timestamp - 600 
            self.list[:] = [item for item in self.list if item["timestamp"] >= cutoff_timestamp] 
        except Exception as e:
            print(f"Ocurrió un error: {e}")