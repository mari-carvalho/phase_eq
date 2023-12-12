# Importando Bibliotecas:
import numpy as np
import math as mt
import matplotlib.pyplot as plt

def calculate_eq_phase(fugacity_liq:np.ndarray, fugacity_gas:np.ndarray, list_wi:np.ndarray) -> float:
        
    eq_phase = 0

    for i in range(len(list_wi)):
        
        eq_phase += ((fugacity_liq[i])/(fugacity_gas[i]) -1)**2 

    return eq_phase

