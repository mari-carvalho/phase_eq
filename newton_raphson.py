# Importando Bibliotecas:
import numpy as np
import math as mt
import matplotlib.pyplot as plt
import main as m

# Newton-Raphson:
# Newton-Rapshon: sem busca incremental
def calculate_NR(list_wi:float, list_Zi:float, list_Ki:float) -> float:

  inter = 0
  Vr = 0.5
  f = 0
  f_ = 0
  while (1):
    V_old = Vr
    for n in range(len(list_wi)):
      f = f + (list_Zi[n]*(list_Ki[n]-1))/(1 - Vr + Vr*(list_Ki[j]))
      f_ = f_ - (list_Zi[n]*((list_Ki[n]-1)**2))/((1 + Vr*(list_Ki[n])-1)**2)
    Vr = Vr - f/f_
    err = abs(Vr-V_old)/100
    inter = inter + 1
    if err < (1*10**-6) or inter == 1000:
      break

  return Vr

Vr = calculate_NR(m.list_wi, m.list_Zi, m.list_Ki)
print('O valor de V é:', Vr)