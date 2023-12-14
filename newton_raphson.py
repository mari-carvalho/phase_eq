# Importando Bibliotecas:
import numpy as np
import math as mt
import matplotlib.pyplot as plt

# Newton-Raphson:
# Newton-Rapshon: sem busca incremental
def calculate_NR(list_wi:np.ndarray, list_Zi:np.ndarray, Ki:np.ndarray) -> float:

  itMax = 1000
  Vr = 0.5
  for it in range(itMax):
    V_old = Vr
    f = 0.0
    dfdV = 0.0
    for i in range(len(list_wi)):
      f += (list_Zi[i]*(Ki[i]-1.0))/(1.0 + Vr*(Ki[i]-1.0))
      dfdV += - ((list_Zi[i]*((Ki[i]-1.0)**2))/((1.0 + Vr*(Ki[i]-1.0))**2))
    Vr = Vr - f/dfdV
    err = abs(Vr-V_old)/100
    print("iteration : ", it)
    print("Vr : ", Vr)
    print("err : ", err)
    if err < (1e-6):
      return Vr
    
  print("RR nao convergiu")
  

def calculate_L(Vr:float) -> float:

  L = 1- Vr

  return L


