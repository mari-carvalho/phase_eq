# Importando Bibliotecas:
import numpy as np
import math as mt
import matplotlib.pyplot as plt

# Estimativa do valor de Ki

def calculate_Ki(P:float, T:float, list_Pc:np.ndarray, list_Tc:np.ndarray, list_wi:np.ndarray) -> np.ndarray:

    Ki = np.zeros(len(list_wi))

    for i in range(len(list_wi)):
        Ki[i] = (list_Pc[i]/P)*np.exp(5.37*(1+list_wi[i])*(1-(list_wi[i]/T)))

    return Ki



