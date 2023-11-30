# Importando Bibliotecas:
import numpy as np
import math as mt
import matplotlib.pyplot as plt


# Cálculo dos Parâmetros Bi:
def calculate_Bi(ppr:np.ndarray, tpr:np.ndarray, list_wi:np.ndarray) -> np.ndarray:

  Bi = np.zeros(len(list_wi))

  if eec == 'SRK':
    ohm_b = 0.08664
  elif eec == 'PR':
    ohm_b = 0.0778

  for i in range(len(list_wi)):
    Bi[i] = ohm_b*(ppr[i]/tpr[i])

  return Bi


# Cálculo de B:
def calculate_B(Bi:np.ndarray, list_Zi:np.ndarray, list_wi:np.ndarray) -> np.ndarray:

  B = np.zeros(len(list_wi))

  for i in range(len(list_wi)):
    B[i] = Bi[i]*list_Zi[i]

  return B


# Cálculo de Ai:
def calculate_Ai(ppr:np.ndarray, tpr:np.ndarray, mwi:np.ndarray, list_wi:np.ndarray) -> np.ndarray:

  Ai = np.zeros(len(list_wi))

  if eec == 'SRK':
    ohm_a = 0.42748
  elif eec == 'PR':
    ohm_a = 0.45724

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

