import pandas as pd

class IndicatorGenerator:
    def __init__(self, ticksLevel):
        self.ticksLevel = ticksLevel

    def GenerateData(self, periodsInMinute, numPeriods):
        dfTicks = self.ticksLevel.ticks

        secondsToJump = periodsInMinute * numPeriods * 60
        start_time = dfTicks['time'].min() + secondsToJump

        resultados = []
        
        for current_time in dfTicks['time']:    
            if current_time < start_time:
                continue

            registros_filtrados = dfTicks[dfTicks['time'] <= current_time]
            for i in range(numPeriods):
                start_period = current_time - (i + 1) * periodsInMinute * 60        
                end_period = current_time - i * periodsInMinute * 60
                registros_periodo = registros_filtrados[(registros_filtrados['time'] > start_period) & (registros_filtrados['time'] <= end_period)]

                high = registros_periodo['ask'].max()            
                low = registros_periodo['ask'].min()            
                close = registros_periodo['ask'].iloc[-1] 
                last_time = registros_periodo['time'].iloc[-1]

                # Guardar los resultados
                resultados.append({
                    'high': high,
                    'low': low,
                    'close': close,
                    'timestamp': last_time
                })

            result_df = pd.DataFrame(resultados)
            print(result_df)