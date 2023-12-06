# Importando Bibliotecas:
import numpy as np
import math as mt
import matplotlib.pyplot as plt

def calculate_eq_phase(fugacity_liq: np.ndarray, fugacity_gas: np.ndarray, list_wi: np.ndarray, xi:np.ndarray, yi:np.ndarray, Ki:np.ndarray) -> np.ndarray:

    eq_phase = np.zeros(len(list_wi))

    for i in range(len(list_wi)):
        eq_phase = ((fugacity_liq[i])/(fugacity_gas[i]) -1)**2 
        if eq_phase < 10**-8:
            Ki[i] = yi[i]/xi[i]
            print(Vr, L, xi, yi, Z_liq, Z_gas, Ki)

    return eq_phase