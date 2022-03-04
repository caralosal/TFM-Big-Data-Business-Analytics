import numpy as np
import pandas as pd

def mae(predictions, targets):
    """Función que calcula el MAE (Mean Absolute Error) entre la predicción
    y la variable real.
    Params:
        - predictions: array de las predicciones
        - targets: array de los valores reales.
    """
    return abs(predictions - targets)


def mape(predictions, targets):
    """Función que calcula el MAPE (Mean Absolute Percentage Error) entre la predicción
    y la variable real.
    Params:
        - predictions: array de las predicciones
        - targets: array de los valores reales.
    """
    return abs((targets - predictions) / targets) * 100

def wmape(predictions, targets):
    """Función que calcula el WMAPE (Weight Mean Absolute Percentage Error) entre la predicción
    y la variable real.
    Params:
        - predictions: array de las predicciones
        - targets: array de los valores reales.
    """
    return np.sum(abs(targets - predictions)) / np.sum(targets) * 100


def rmse(predictions, targets):
    """Función que calcula el RMSE (Root Mean Squared Error) entre la predicción
    y la variable real.
    Params:
        - predictions: array de las predicciones
        - targets: array de los valores reales.
    """
    return np.sqrt(((predictions - targets) ** 2).mean())


def calculo_metricas(dataframe):
    """Función que saca por pantalla todas las métricas que estamos trabajando.
    Params:
        - dataframe: es un dataframe con tres columnas importantes:
            + Fecha: fechas de 2021 (es donde vamos a comparar las métricas)
            + Pred: variable que recoge las predicciones
            + Real: variable que recoge los valores reales
    """
    
    # Cálculos de las métricas de MAE y MAPE
    dataframe.loc[:, "MAE"] = mae(dataframe.Pred, dataframe.Real)
    dataframe.loc[:, "MAPE"] = mape(dataframe.Pred, dataframe.Real)
    
    # Dataframe de predicción de tendencia
    up_down_price = dataframe[["Pred", "Real"]].diff(1).dropna()
    up_down_price.loc[:, "Ind_Pred"] = [1 if data > 0 else 0 for data in up_down_price.Pred]
    up_down_price.loc[:, "Ind_Real"] = [1 if data > 0 else 0 for data in up_down_price.Real]
    up_down_price.loc[:, "Aciertos"] = up_down_price.loc[:, "Ind_Pred"] == up_down_price.loc[:, "Ind_Real"]
    
    # Creación del dataframe que se mostrará por pantalla
    metrica = pd.DataFrame({"MAE" : round(float(dataframe.loc["2021"][['MAE']].mean()), 2),
                            "MAE (median)" : round(float(np.median(dataframe.loc["2021"][['MAE']])), 2),
                            "MAPE" : round(float(dataframe.loc["2021"][['MAPE']].mean()), 2),
                            "WMAPE" : round(wmape(dataframe.loc["2021"].Pred, dataframe.loc["2021"].Real), 2),
                            "RMSE" : round(rmse(dataframe.loc["2021"].Pred, dataframe.loc["2021"].Real), 2),
                            "% Trend" : round(up_down_price.Aciertos.value_counts()[1] / 
                                              up_down_price.Aciertos.value_counts().sum() * 100, 2)}, index = [0])
    
    # Mostramos por pantalla el dataframe de métricas
    print(metrica)                 
                            
    # Dataframe de métricas por meses                        
    metricas_mensuales_dataframe = dataframe.groupby([dataframe.index.year,dataframe.index.month])[["MAE", "MAPE"]].mean()
    return dataframe, metricas_mensuales_dataframe, metrica
