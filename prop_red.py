# Importando Bibliotecas:
import numpy as np
import math as mt
import matplotlib.pyplot as plt
import main as m

# Cálculo das Pressões Temperaturas Pseudo-Reduzidas:
def calculate_ppr(P:float, list_Pc:np.ndarray) -> np.ndarray:

  ppr = np.zeros(len(list_Pc))

  for i in range(len(list_Pc)):
    ppr[i] = P/list_Pc[i]

  return ppr

def calculate_tpr(T:float, list_Tc:np.ndarray) -> np.ndarray:

  tpr = np.zeros(len(list_Tc))

  for i in range(len(list_Tc)):
    tpr[i] = T/list_Tc[i]

  return tpr
