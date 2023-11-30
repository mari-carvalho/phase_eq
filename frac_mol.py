# Importando Bibliotecas:
import numpy as np
import math as mt
import matplotlib.pyplot as plt
import main as m

# Cálculo das Frações Molares:
def calculate_xi(V:np.ndarray, list_Zi:np.ndarray, list_Ki:np.ndarray, Vr:float, list_wi:np.ndarray) -> np.ndarray:

  xi = np.zeros(len(V))

  for i in range(len(list_wi)):
    xi[i] = list_Zi[i]/(1 +Vr*(list_Ki[i]-1))

  return xi

def calculate_yi(V:np.ndarray, list_Zi:np.ndarray, list_Ki:np.ndarray, Vr:float, list_wi:np.ndarray) -> np.ndarray:

  yi = np.zeros(len(V))

  for i in range(len(list_wi)):
    yi[i] = (list_Ki[i]*list_Zi[i])/(1 + Vr*(list_Ki[i]-1))

  return yi

xi = calculate_xi(m.V, m.list_Zi, m.list_Ki, m.Vr, m.list_wi)
print(xi)

yi = calculate_yi(m.V, m.list_Zi, m.list_Ki, m.Vr, list_wi)
print(yi)
