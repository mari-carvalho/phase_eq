# Importando Bibliotecas:
import numpy as np
import math as mt
import matplotlib.pyplot as plt

# Cálculo das Frações Molares:
def calculate_xi(V:np.ndarray, list_Zi:np.ndarray, Ki:np.ndarray, Vr:float, list_wi:np.ndarray) -> np.ndarray:

  xi = np.zeros(len(list_wi))

  for i in range(len(list_wi)):
    xi[i] = list_Zi[i]/(1 +Vr*(Ki[i]-1))

  return xi

def calculate_yi(V:np.ndarray, list_Zi:np.ndarray, Ki:np.ndarray, Vr:float, list_wi:np.ndarray) -> np.ndarray:

  yi = np.zeros(len(list_wi))

  for i in range(len(list_wi)):
    yi[i] = (Ki[i]*list_Zi[i])/(1 + Vr*(Ki[i]-1))

  return yi

