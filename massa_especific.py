# Importando Bibliotecas:
import numpy as np
import scipy
import math as mt
import matplotlib.pyplot as plt

def calculate_M_liq(xi:np.ndarray, list_wi:np.ndarray, M:np.ndarray) -> float:

    M_liq = 0

    for i in range(len(list_wi)):

        M_liq = M_liq + xi[i]*M[i]

    return M_liq

def calculate_M_gas(yi:np.ndarray, list_wi:np.ndarray, M:np.ndarray) -> float:

    M_gas = 0

    for i in range(len(list_wi)):

        M_gas = M_gas + yi[i]*M[i]

    return M_gas

def calculate_rho_o(M_liq:float, P:float, R:float, T:float, Z_liq:float) -> float:

    rho_o = (M_liq*P)/(Z_liq*R*T)

    return rho_o

def calculate_rho_g(M_gas:float, P:float, R:float, T:float, Z_gas:float) -> float:

    rho_g = (M_gas*P)/(Z_gas*R*T)

    return rho_g

