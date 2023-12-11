# Importando Bibliotecas:
import numpy as np
import scipy
import math as mt
import matplotlib.pyplot as plt


def func_Z_liq(Z: float, B_final_liq: float, A_final_liq: float, delta_1: float, delta_2: float):

    C1 = 1.
    C2 = ((delta_1 + delta_2 -1)*B_final_liq-1)
    C3 = (A_final_liq + delta_1*delta_2*B_final_liq**2) - (delta_1+delta_2) *B_final_liq*(B_final_liq + 1)
    C4 = -(A_final_liq*B_final_liq + delta_1*delta_2*B_final_liq**2 * (B_final_liq+1))

    return C1*Z**3 + C2*Z**2 + C3*Z + C4


def calculate_Z_liq(func_Z_liq) -> float:

    Z_liq = scipy.optimize.newton(func_Z_liq, 0.5, fprime=None, args=(), tol=1.48e-08, maxiter=50, fprime2=None, x1=None, rtol=0.0, full_output=False, disp=True)

    return Z_liq

def func_Z_gas(Z: float, B_final_gas:float, A_final_gas: float, eec: str):

    if eec == 'PR':
        delta_1 = 1 + np.sqrt(2)
        delta_2 = 1 - np.sqrt(2)
    elif eec == 'SRK':
        delta_1 = 0
        delta_2 = 1

    C1 = 1.
    C2 = ((delta_1 + delta_2 -1)*B_final_gas-1)
    C3 = (A_final_gas + delta_1*delta_2*B_final_gas**2) - (delta_1+delta_2) *B_final_gas*(B_final_gas + 1)
    C4 = -(A_final_gas*B_final_gas + delta_1*delta_2*B_final_gas**2 * (B_final_gas+1))

    return C1*Z**3 + C2*Z**2 + C3*Z + C4


def calculate_Z_gas(func_Z_gas) -> float:

    Z_gas = scipy.optimize.newton(func_Z_gas, 0.5, fprime=None, args=(), tol=1.48e-08, maxiter=50, fprime2=None, x1=None, rtol=0.0, full_output=False, disp=True)

    return Z_gas


