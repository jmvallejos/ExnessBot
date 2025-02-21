import json
import threading
import MetaTrader5 as mt5

class Mt5Operator(threading.Thread):
    def __init__(self):
        super().__init__()
        self.orderList = []
    
    def run(self):
        threading.Thread(target=self.checkOrderStatuses).start()

    def checkOrderStatuses(self):
        while(True):
            if(len(self.orderList) == 0):
                continue
            positions = mt5.positions_get()
            self.orderList = [order for order in self.orderList if self.exists_in_ticket_list(positions, order)]

    def exists_in_ticket_list(self, positios, order_item):
        for ticket in positios:
            if (ticket.symbol == order_item["instrument"] and
                ticket.type == order_item["type"] and
                ticket.ticket == order_item["order"]):
                return True  # Existe un ítem que coincide
        return False  # No existe tal ítem

    def Buy(self, instrument):
        for order in self.orderList:
            if order["instrument"] == instrument and order["type"] == mt5.ORDER_TYPE_BUY:
                return False
    
        tick = mt5.symbol_info_tick(instrument)
        lote = 0.01
        spread = tick.ask - tick.bid 

        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": instrument,
            "volume": lote,
            "type": mt5.ORDER_TYPE_BUY,
            "price": tick.ask,
            "sl": round(tick.bid - spread / 2.5, 2),
            "tp": round(tick.bid + spread * 3, 2),
            "slippage": 10,
            "magic": 234000,  # Número mágico para identificar la orden
            "comment": "",
            "type_time": mt5.ORDER_TIME_GTC,  # Orden válida hasta que se cancele
            "type_filling": mt5.ORDER_FILLING_IOC  # Llenado inmediato o cancelación
        }
        
        # Enviar la orden de compra
        result = mt5.order_send(request)

        self.orderList.append({
            "instrument": instrument,
            "order": result.order,
            "type" : mt5.ORDER_TYPE_BUY
        })

        return result.order

        