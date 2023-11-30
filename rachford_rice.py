# Importando Bibliotecas:
import numpy as np
import math as mt
import matplotlib.pyplot as plt

# Rachford-Rice:
# função:
def calculate_f(V: np.ndarray, list_Zi:np.ndarray, list_Ki:np.ndarray, list_wi:np.ndarray) -> np.ndarray:
  rows = len(V)
  cols = len(list_wi)

  f = np.zeros((rows, cols))

  for i in range(rows):
    for j in range(cols):
      f[i,j] = (list_Zi[j]*(list_Ki[j]-1))/(1 - V[i] + V[i]*(list_Ki[j]))

  return f
#derivada:
def calculate_f_(V:np.ndarray, list_Zi:np.ndarray, list_Ki:np.ndarray, list_wi:np.ndarray) -> np.ndarray:
  rows = len(V)
  cols = len(list_wi)

  f_ = np.zeros((rows, cols))

  for i in range(rows):
    for j in range(cols):
      f_[i,j] = (list_Zi[j]*((list_Ki[j]-1)**2))/((1 + V[i]*(list_Ki[j])-1)**2)

  return f_

def calculate_RR(V:np.ndarray, f:np.ndarray) -> np.ndarray:

  RR = np.zeros(len(V)) # cria-se um vetor do mesmo tamanho do vetor de valores de chutes iniciais, que servirá ára acumular possíveis valores para chute

  for k in range(len(V)):
    RR[k] = np.sum(f[k, :])

  return RR
