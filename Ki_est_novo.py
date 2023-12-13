# Importando Bibliotecas:
import numpy as np
import math as mt

def calculate_Ki_novo(list_wi:np.ndarray, fugacity_liq:np.ndarray, fugacity_gas:np.ndarray, Ki:np.ndarray) -> np.ndarray:

    for i in range(len(list_wi)):

        Ki[i] = (Ki[-1])*((fugacity_liq[-1])/(fugacity_gas[-1]))

    return Ki