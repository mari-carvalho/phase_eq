# Importando Bibliotecas:
import numpy as np
import math as mt
import matplotlib.pyplot as plt


# Cálculo dos Parâmetros Bi:
def calculate_Bi(ppr:np.ndarray, tpr:np.ndarray, list_wi:np.ndarray, ohm_b) -> np.ndarray:

  Bi = np.zeros(len(list_wi))

  for i in range(len(list_wi)):
    Bi[i] = ohm_b*(ppr[i]/tpr[i])

  return Bi

# Cálculo de B_gas:
def calculate_B_gas(Bi:np.ndarray, yi:np.ndarray, list_wi:np.ndarray) -> float:

  for i in range(len(yi)):
    B_gas = Bi[i]*yi[i] + B_gas[i-1]

  return B_gas

# Cálculo de B_liq:
def calculate_B_liq(Bi:np.ndarray, xi:np.ndarray, list_wi:np.ndarray) -> float:

  for i in range(len(xi)):
    B_liq = Bi[i]*xi[i] + B_liq[i-1]

  return B_liq

# Cálculo de mwi:
def calculate_mwi(list_wi:np.ndarray, eec: str) -> np.ndarray:

  mwi = np.zeros(len(list_wi))

  for i in range(len(list_wi)):
    if eec == 'SRK':
      mwi[i] = 0.480 + 1.574*list_wi[i] - (0.176*(list_wi[i]**2))
    elif eec == 'PR':
      if list_wi[i] <= 0.49:
        mwi[i] = 0.37464 + 1.5422*list_wi[i] - (0.26992*(list_wi[i]**2))
      elif list_wi[i] > 0.49:
        mwi[i] = 0.379642 + 1.48503*list_wi[i] - (0.1644236*(list_wi[i]**2))

  return mwi

# Cálculo de Ai:
def calculate_Ai(ppr:np.ndarray, tpr:np.ndarray, mwi:np.ndarray, list_wi:np.ndarray, ohm_a: float) -> np.ndarray:

  Ai = np.zeros(len(list_wi))

  for i in range(len(list_wi)):
    Ai[i] = ohm_a*(ppr[i]/(tpr[i]**2))*(1+mwi[i]*(1-mt.sqrt(tpr[i])))**2

  return Ai

# Cálculo de Aij:
def calculate_Aij(Ai:np.ndarray, list_Ki:np.ndarray, list_wi:np.ndarray) -> np.ndarray:

  Aij = np.zeros((len(list_wi), len(list_wi)))

  for i in range(len(list_wi)):
    for j in range(len(list_wi)):
      Aij[i,j] = (mt.sqrt(Ai[i]*Ai[j]))*(1-list_Ki[j])

  return Aij

# Cálculo de A_gas:
def calculate_A_gas(yi:np.ndarray, Aij:np.ndarray) -> float:

  for i in range(len(Aij)):
    for j in range(len(Aij)):
      A_gas = yi[i]*yi[j]*Aij[i] + A_gas[i-1]

  return A_gas

# Cálculo de A_liq:
def calculate_A_liq(xi:np.ndarray, Aij:np.ndarray) -> float:

  for i in range(len(Aij)):
    for j in range(len(Aij)):
      A_liq = xi[i]*xi[j]*Aij[i] + A_liq[i-1]

  return A_liq

# Parâmetros finais:
def calculate_A_final_gas(A_gas:float, P:float, R:float, T:float) -> float:

  A_final_gas = (A_gas*P)/((R**2)*(T**2))

  return A_final_gas 

def calculate_A_final_liq(A_liq:float, P:float, R:float, T:float) -> float:

  A_final_liq = (A_liq*P)/((R**2)*(T**2))

  return A_final_liq

def calculate_B_final_gas(B_gas:float, P:float, R:float, T:float) -> float:

  B_final_gas = (B_gas*P)/(R*T)

  return B_final_gas

def calculate_B_final_liq(B_liq:float, P:float, R:float, T:float) -> float:

  B_final_liq = (B_liq*P)/(R*T)

  return B_final_liq
