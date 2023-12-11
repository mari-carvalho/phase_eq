# Importando Bibliotecas:
import numpy as np
import math as mt
import matplotlib.pyplot as plt


def calculate_eq_phase(fugacity_liq:np.ndarray, fugacity_gas:np.ndarray, list_wi:np.ndarray, xi:np.ndarray, yi:np.ndarray, Ki:np.ndarray, P:float, T:float, list_Pc:np.ndarray, list_Tc:np.ndarray, V:float, list_Zi:np.ndarray, R:float, func_Z_gas, func_Z_liq, delta_1:float, delta_2:float, L:float) -> np.ndarray:

    eq_phase = np.zeros(len(list_wi))
    
    for i in range(len(list_wi)):
        
        eq_phase = ((fugacity_liq[i])/(fugacity_gas[i]) -1)**2 

        if eq_phase[i] < 10**-8:
            Ki[i] = yi[i]/xi[i]
            print(Vr, L, xi, yi, Z_liq, Z_gas, Ki)
        else: 
            for n in range(len(list_wi)):
                Ki[i] = (Ki**i)*(((fugacity_liq[i])/(fugacity_gas[i]))**i)

    return eq_phase