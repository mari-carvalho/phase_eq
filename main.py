# Importando Bibliotecas:
import numpy as np
import math as mt
import matplotlib.pyplot as plt
import ki_est as ki
import rachford_rice as rr
import busc_incre as b_i
import prop_red as pr
import parametros_eec as p_eec

# Dados - Iniciando as Listas:
list_Zi = np.array([0.4, 0.1, 0.05, 0.1, 0.05, 0.05, 0.05, 0.1, 0.05, 0.05])
print('Zi', list_Zi)
list_Pc = np.array([667.0286, 706.6239, 616.1203, 550.5633, 1069.5, 488.7772, 492.8382, 306.0296, 287.1747, 263.9687])
print('Pc', list_Pc)
list_Tc = np.array([343.008, 549.576, 665.694, 765.216, 547.416, 845.46, 227.16, 1111.9, 1150.2, 1184.4])
print('Tc', list_Tc)
list_wi = np.array([0.011, 0.099, 0.152, 0.2, 0.225, 0.252, 0.037, 0.49, 0.537, 0.576])
print('wi', list_wi)
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
Ki = ki.calculate_Ki(P, T, list_Pc, list_Tc, list_wi)
print(list_Ki)

# Rachford-Rice:
f = rr.calculate_f(V, list_Zi, list_Ki, list_wi)
print('f', f)

f_ = rr.calculate_f_(V, list_Zi, list_Ki, list_wi)
print('f_', f_)

RR = rr.calculate_RR(V, f)
print('RR', RR)

# Busca Incremental:
busc_incr = b_i.calculate_busc_incr(V, RR)
print('xb', xb)

# Propriedades Pseudo-Reduzidas:
ppr = pr.calculate_ppr(P, list_Pc)
print('ppr', ppr)

tpr = pr.calculate_tpr(T, list_Tc)
print('tpr', tpr)

# Parâmetros da eec:
# Cálculo dos Parâmetros Bi:
Bi = p_eec.calculate_Bi(ppr, tpr, list_wi)
print('Bi', Bi)

# Cálculo de B:
B = p_eec.calculate_B(Bi, list_Zi, list_wi)
print('B', B)

# Cálculo de Ai:
Ai = p_eec.calculate_Ai(ppr, tpr, mwi, list_wi)
print('Ai', Ai)

# Cálculo de Aij:
Aij = p_eec.calculate_Aij(Ai, list_Ki, list_wi)
print(Aij)