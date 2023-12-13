# Importando Bibliotecas:
import numpy as np
import math as mt
import matplotlib.pyplot as plt

# Newton-Raphson:
# Newton-Rapshon: sem busca incremental
def calculate_NR(list_wi:np.ndarray, list_Zi:np.ndarray, Ki:np.ndarray) -> float:

  Ki = Ki
  iter = 0
  Vr = 0.5
  while True:
    V_old = Vr
    f = 0
    f_ = 0
    for i in range(len(list_wi)):
      f = f + (list_Zi[i]*(Ki[i]-1))/(1 - Vr + Vr*(Ki[i]))
      f_ = - (f_ + ((list_Zi[i]*((Ki[i]-1)**2))/((1 + Vr*(Ki[i])-1)**2)))
    Vr = Vr - f/f_
    err = abs(Vr-V_old)/100
    iter = iter + 1
    if err < (1e-6) or iter == 1000:
      break
  return Vr

def calculate_L(Vr:float) -> float:

  L = 1- Vr

  return L


