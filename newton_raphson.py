# Importando Bibliotecas:
import numpy as np
import math as mt
import matplotlib.pyplot as plt

# Newton-Raphson:
# Newton-Rapshon: sem busca incremental
def calculate_NR(list_wi:np.ndarray, list_Zi:np.ndarray, Ki:np.ndarray) -> float:

  inter = 0
  Vr = 0.5
  f = 0
  f_ = 0
  while (1):
    V_old = Vr
    for n in range(len(list_wi)):
      f = f + (list_Zi[n]*(Ki[n]-1))/(1 - Vr + Vr*(Ki[j]))
      f_ = f_ - (list_Zi[n]*((Ki[n]-1)**2))/((1 + Vr*(Ki[n])-1)**2)
    Vr = Vr - f/f_
    err = abs(Vr-V_old)/100
    inter = inter + 1
    if err < (1*10**-6) or inter == 1000:
      break

  return Vr

def calculate_L(Vr: float) -> float:

  L = 1- Vr

  return L
