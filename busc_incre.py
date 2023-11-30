# Importando Bibliotecas:
import numpy as np
import math as mt
import matplotlib.pyplot as plt
import ki_est as ki

def calculate_busc_incr(V:np.ndarray, RR:np.ndarray) -> np.ndarray:

  nb = 0 # número de vezes que ocorre a troc de sinais ao longo de todo o intervalo de chutes escolhido (vetor V)
  xb = np.zeros((len(V), 2)) # vetor para valores de extremidade superior e inferior de cada mudança de sinal

  for k in range(len(V)-1):
    if np.sign(RR[k])  != np.sign(RR[k+1]):
      nb = nb + 1
      xb[nb, 0] = RR[k]
      xb[nb, 1] = RR[k+1]

  return xb
