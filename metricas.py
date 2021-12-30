import numpy as np

# Calculo de las métricas de medición
def mae(predictions, targets):
    return abs(predictions - targets)

def mape(predictions, targets):
    return abs((targets - predictions) / targets) * 100

def rmse(predictions, targets):
    return np.sqrt(((predictions - targets) ** 2).mean())
