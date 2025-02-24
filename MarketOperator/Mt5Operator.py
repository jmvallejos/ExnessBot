import MetaTrader5 as mt5

class Mt5Operator():
    def __init__(self):
        super().__init__()
        self.orderList = []
        self.dataInstrument = {
            "EURUSDm": {"pipValue": 0.0001, "loteValue": 0.02},
            "USDJPYm": {"pipValue": 0.01, "loteValue": 0.03},
            "GBPUSDm": {"pipValue": 0.0001, "loteValue": 0.02},
            "USDCHFm": {"pipValue": 0.0001, "loteValue": 0.02},
            "AUDUSDm": {"pipValue": 0.0001, "loteValue": 0.02},
            "USDCADm": {"pipValue": 0.0001, "loteValue": 0.03},
            "NZDUSDm": {"pipValue": 0.0001, "loteValue": 0.02},
            "EURGBPm": {"pipValue": 0.0001, "loteValue": 0.02},
            "EURJPYm": {"pipValue": 0.01, "loteValue": 0.03},
            "GBPJPYm": {"pipValue": 0.01, "loteValue": 0.03},
        }

    def Buy(self, instrument):
        try:
            instrumentInfo = mt5.symbol_info(instrument)
            tick = mt5.symbol_info_tick(instrument)
            dataInstrument = self.dataInstrument[instrument]

            stop_loss_price = tick.ask - (2.5 * dataInstrument["pipValue"])      
            take_profit_price = tick.ask + (5 * dataInstrument["pipValue"])  

            request = {
                "action": mt5.TRADE_ACTION_DEAL,
                "symbol": instrument,
                "volume": dataInstrument["loteValue"],
                "type": mt5.ORDER_TYPE_BUY,
                "price": tick.ask,
                "sl": stop_loss_price,        
                "tp": take_profit_price,
                "slippage": 10,
                "magic": 234000,  # Número mágico para identificar la orden
                "comment": "",
                "type_time": mt5.ORDER_TIME_GTC,  # Orden válida hasta que se cancele
                "type_filling": mt5.ORDER_FILLING_IOC  # Llenado inmediato o cancelación
            }
            
            return mt5.order_send(request)        
        except Exception as e:
            print(f"Ocurrió un error: {e}")
            return None
    
    def Sell(self, instrument):
        try:
            instrumentInfo = mt5.symbol_info(instrument)
            tick = mt5.symbol_info_tick(instrument)
            dataInstrument = self.dataInstrument[instrument]
            
            stop_loss_price = tick.bid + (2.5 * dataInstrument["pipValue"]) 
            take_profit_price = tick.bid - (5 * dataInstrument["pipValue"])  

            request = {
                "action": mt5.TRADE_ACTION_DEAL,
                "symbol": instrument,
                "volume": dataInstrument["loteValue"],
                "type": mt5.ORDER_TYPE_SELL,
                "price": tick.bid,
                "sl": stop_loss_price,
                "tp": take_profit_price,
                "slippage": 10,
                "magic": 234000,  # Número mágico para identificar la orden
                "comment": "",
                "type_time": mt5.ORDER_TIME_GTC,  # Orden válida hasta que se cancele
                "type_filling": mt5.ORDER_FILLING_IOC  # Llenado inmediato o cancelación
            }
            
            return mt5.order_send(request)
        except Exception as e:
            print(f"Ocurrió un error: {e}")
            return None

        