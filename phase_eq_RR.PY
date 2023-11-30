# Importando Bibliotecas:
import numpy as np
import math as mt
import matplotlib.pyplot as plt

# Dados - Iniciando as Listas:
list_Zi = np.array([0.4, 0.1, 0.05, 0.1, 0.05, 0.05, 0.05, 0.1, 0.05, 0.05])
print('Zi', list_Zi)
list_Pc = np.array([667.0286, 706.6239, 616.1203, 550.5633, 1069.5, 488.7772, 492.8382, 306.0296, 287.1747, 263.9687])
print('Pc', list_Pc)
list_Tc = np.array([343.008, 549.576, 665.694, 765.216, 547.416, 845.46, 227.16, 1111.9, 1150.2, 1184.4])
print('Tc', list_Tc)
list_wi = np.array([0.011, 0.099, 0.152, 0.2, 0.225, 0.252, 0.037, 0.49, 0.537, 0.576])
print('wi', list_wi)
list_Ki = []
P = 800
T = 365
V = np.linspace(0,5, num=10)
print(V)
f = np.zeros((len(V), len(list_wi))) # cria-se uma matriz com o número de linhas correspondente ao tamanho do vetor V (quão grande é o intervalo de chutes) e o número de colunas correspondente ao número de propriedades estimadas
print(f)
f_ = np.zeros((len(V), len(list_wi)))
print(f_)

# Escolha da Equação de Estado Cúbica a ser utilizada para Cálculo:
eec = input('Escolha a EEC a ser usada para Cálculo: SRK ou PR:')


# Estimativa do valor de Ki:
def calculate_Ki(P:float, T:float, list_Pc:float, list_Tc:float, list_wi:float) -> float:

  Ki = (list_Pc[i]/P)*np.exp(5.37*(1+list_wi[i])*(1-(list_wi[i]/T)))

  return Ki

for i in range(len(list_wi)):

  Ki = calculate_Ki(P, T, list_Pc, list_Tc, list_wi)
  list_Ki.append(Ki)

print(list_Ki)


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

def calculate_busc_incr(V:np.ndarray, RR:np.ndarray) -> np.ndarray:

  nb = 0 # número de vezes que ocorre a troc de sinais ao longo de todo o intervalo de chutes escolhido (vetor V)
  xb = np.zeros((len(V), 2)) # vetor para valores de extremidade superior e inferior de cada mudança de sinal

  for k in range(len(V)-1):
    if np.sign(RR[k])  != np.sign(RR[k+1]):
      nb = nb + 1
      xb[nb, 0] = RR[k]
      xb[nb, 1] = RR[k+1]

  return xb

f = calculate_f(V, list_Zi, list_Ki, list_wi)
print('f', f)

f_ = calculate_f_(V, list_Zi, list_Ki, list_wi)
print('f_', f_)

RR = calculate_RR(V, f)
print('RR', RR)

busc_incr = calculate_busc_incr(V, RR)
print('xb', xb)


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

Vr = calculate_NR(list_wi, list_Zi, list_Ki)
print('O valor de V é:', Vr)


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

xi = calculate_xi(V, list_Zi, list_Ki, Vr, list_wi)
print(xi)

yi = calculate_yi(V, list_Zi, list_Ki, Vr, list_wi)
print(yi)


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

ppr = calculate_ppr(P, list_Pc)
print('ppr', ppr)

tpr = calculate_tpr(T, list_Tc)
print('tpr', tpr)


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

Bi = calculate_Bi(ppr, tpr, list_wi)
print('Bi', Bi)


# Cálculo de B:
def calculate_B(Bi:np.ndarray, list_Zi:np.ndarray, list_wi:np.ndarray) -> np.ndarray:

  B = np.zeros(len(list_wi))

  for i in range(len(list_wi)):
    B[i] = Bi[i]*list_Zi[i]

  return B

B = calculate_B(Bi, list_Zi, list_wi)
print('B', B)


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

Ai = calculate_Ai(ppr, tpr, mwi, list_wi)
print('Ai', Ai)


# Cálculo de Aij:
def calculate_Aij(Ai:np.ndarray, list_Ki:np.ndarray, list_wi:np.ndarray) -> np.ndarray:

  Aij = np.zeros((len(list_wi), len(list_wi)))

  for i in range(len(list_wi)):
    for j in range(len(list_wi)):
      Aij[i,j] = (mt.sqrt(Ai[i]*Ai[j]))*(1-list_Ki[j])

  return Aij

Aij = calculate_Aij(Ai, list_Ki, list_wi)
print(Aij)