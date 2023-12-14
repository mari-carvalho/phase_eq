# Importando Bibliotecas:
import numpy as np
import scipy
import math as mt
import matplotlib.pyplot as plt


def calculate_Delta(delta_1: float, delta_2: float) -> float:

    Delta = delta_1 - delta_2

    return Delta

def calculate_phi_liq(Aij:np.ndarray, xi:np.ndarray, list_wi:np.ndarray) -> np.ndarray:

    phi_liq = np.zeros(len(list_wi))

    for i in range(len(list_wi)):
        for j in range(len(list_wi)):
            phi_liq[i] = Aij[i,j]*xi[j]
    
    return phi_liq

def calculate_phi_gas(Aij:np.ndarray, yi:np.ndarray, list_wi:np.ndarray) -> np.ndarray:

    phi_gas = np.zeros(len(list_wi))

    for i in range(len(list_wi)):
        for j in range(len(list_wi)):
            phi_gas[i] = Aij[i,j]*yi[j]
    
    return phi_gas

def calculate_phi_fug_liq(Bi:np.ndarray, B_final_liq:float, A_final_liq:float, delta_1:float, delta_2:float, list_wi:np.ndarray, Z_liq:float, Delta:float, phi_liq:np.ndarray) -> np.ndarray:

    phi_fug_liq = np.zeros(len(list_wi))
    
    for i in range(len(list_wi)):

        term1 = (Z_liq-1)*(Bi[i]/B_final_liq)
        term2 = np.log(Z_liq - B_final_liq)
        term3 = (A_final_liq/(Delta*B_final_liq))*(2*(phi_liq[i]/A_final_liq) - (Bi[i]/B_final_liq))
        term4 = np.log((Z_liq + (delta_1*B_final_liq))/(Z_liq + (delta_2*B_final_liq)))

        phi_fug_liq[i] = np.exp(term1 - term2 - term3 * term4)

    return phi_fug_liq
    
def calculate_phi_fug_gas(Bi:np.ndarray, B_final_gas:float, A_final_gas:float, delta_1:float, delta_2: float, list_wi:np.ndarray, Z_gas:float, Delta:float, phi_gas:np.ndarray) -> np.ndarray:

    phi_fug_gas = np.zeros(len(list_wi))

    for i in range(len(list_wi)):

        phi_fug_gas[i] = np.exp((Z_gas-1)*(Bi[i]/B_final_gas) - np.log(Z_gas - B_final_gas) - (A_final_gas/(Delta*B_final_gas))*(2*(phi_gas[i]/A_final_gas) - (Bi[i]/B_final_gas)) * np.log((Z_gas + (delta_1*B_final_gas))/(Z_gas + (delta_2*B_final_gas))))

    return phi_fug_gas

def calculate_fugacity_liq(phi_fug_liq:np.ndarray, P: float, xi:np.ndarray, list_wi: np.ndarray) -> np.ndarray:

    fugacity_liq = np.zeros(len(list_wi))

    for i in range(len(list_wi)):

        fugacity_liq[i] = phi_fug_liq[i]*xi[i]*P

    return fugacity_liq

def calculate_fugacity_gas(phi_fug_gas:np.ndarray, P: float, yi:np.ndarray, list_wi: np.ndarray) -> np.ndarray:

    fugacity_gas = np.zeros(len(list_wi))

    for i in range(len(list_wi)):

        fugacity_gas[i] = phi_fug_gas[i]*yi[i]*P

    return fugacity_gas