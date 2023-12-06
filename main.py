# Importando Bibliotecas:
import numpy as np
import math as mt
import matplotlib.pyplot as plt
import scipy 
from ki_est import calculate_Ki
from frac_mol import calculate_xi, calculate_yi
from rachford_rice import calculate_f, calculate_f_, calculate_RR
from newton_raphson import calculate_NR
from prop_red import calculate_ppr, calculate_tpr
from parametros_eec import calculate_mwi, calculate_Ai, calculate_Aij, calculate_A_gas, calculate_A_liq, calculate_B_gas, calculate_B_liq, calculate_Bi, calculate_A_final_gas, calculate_A_final_liq, calculate_B_final_gas, calculate_B_final_liq
from factor_Z import calculate_Z_liq
from factor_Z import calculate_Z_gas

# Dados - Iniciando as Listas:
list_Zi = np.array([0.5, 0.5])
print('Zi', list_Zi)
list_Pc = np.array([45.99*10**5, 73.74*10**5])
print('Pc', list_Pc)
list_Tc = np.array([190.56, 304.12])
print('Tc', list_Tc)
list_wi = np.array([0.011, 0.225]) 
print('wi', list_wi)
P = 50*10**5
T = 220
V = np.linspace(0,5, num=10)
print(V)
f = np.zeros((len(V), len(list_wi))) # cria-se uma matriz com o número de linhas correspondente ao tamanho do vetor V (quão grande é o intervalo de chutes) e o número de colunas correspondente ao número de propriedades estimadas
print(f)
f_ = np.zeros((len(V), len(list_wi)))
print(f_)
R = 8.31

# Escolha da Equação de Estado Cúbica a ser utilizada para Cálculo:
eec = input('Escolha a equação de estado cúbica a ser utilizada, 1 para SRK e 2 para PR:')

# Parâmetros das Correlações:
if eec == 'SRK':
    ohm_b = 0.08664
elif eec == 'PR':
    ohm_b = 0.0778

if eec == 'SRK':
    ohm_a = 0.42748
elif eec == 'PR':
    ohm_a = 0.45724

if eec == 'PR':
    delta_1 = 1 + np.sqrt(2)
    delta_2 = 1 - np.sqrt(2)
elif eec == 'SRK':
    delta_1 = 0
    delta_2 = 1    

# Estimativa do valor de Ki:
Ki = calculate_Ki(P, T, list_Pc, list_Tc, list_wi)
print(Ki)

# Rachford-Rice:
f = calculate_f(V, list_Zi, Ki, list_wi)
print('f', f)

f_ = calculate_f_(V, list_Zi, Ki, list_wi)
print('f_', f_)

RR = calculate_RR(V, f)
print('RR', RR)

# Busca Incremental:
#busc_incr = calculate_busc_incr(V, RR)
#print('xb', xb)

# Propriedades Pseudo-Reduzidas:
ppr = calculate_ppr(P, list_Pc)
print('ppr', ppr)

tpr = calculate_tpr(T, list_Tc)
print('tpr', tpr)

# Parâmetros da eec:
# Cálculo dos Parâmetros Bi:
Bi = calculate_Bi(ppr, tpr, list_wi, eec)
print('Bi', Bi)

# Cálculo de Vr:
Vr = calculate_NR(list_wi, list_Zi, Ki)
print('O valor de Vr é:', Vr)

# Cálculo de frações molares:
# Cálculo de yi:
yi = calculate_yi(V, list_Zi, Ki, Vr, list_wi)
print('yi', yi)

# Cálculo de xi:
xi = calculate_xi(V, list_Zi, Ki, Vr, list_wi)
print('xi', xi)

# Cálculo de B_gas:
B_gas = calculate_B_gas(Bi, yi, list_wi)
print('B_gas', B_gas)

# Cálculo de B_liq:
B_liq = calculate_B_liq(Bi, xi, list_wi)
print('B_liq', B_liq)

# Cálculo de mwi:

mwi = calculate_mwi(list_wi)
print('mwi', mwi)

# Cálculo de Ai:
Ai = calculate_Ai(ppr, tpr, mwi, list_wi)
print('Ai', Ai)

# Cálculo de Aij:
Aij = calculate_Aij(Ai, Ki, list_wi)
print('Aij', Aij)

# Cálculo de A_gas:
A_gas = calculate_A_gas(yi, Aij)
print('A_gas', A_gas)

# Cálculo de A_liq:
A_liq = calculate_A_liq(xi, Aij)
print('A_liq', A_liq)

# Cálculo de A_final_gas:
A_final_gas = calculate_A_final_gas(A_gas, P, R, T)
print(A_final_gas)

# Cálculo de A_final_liq:
A_final_liq = calculate_A_final_liq(A_liq, P, R, T)
print(A_final_liq)

# Cálculo de B_final_gas:
B_final_gas = calculate_B_final_gas(B_gas, P, R, T)
print(B_final_gas)

# Cálculo de B_final_liq:
B_final_liq = calculate_B_final_liq(B_liq, P, R, T)
print(B_final_liq)

# Cálculo do fator Z do gás:
Z_liq = calculate_Z_liq(func_Z_liq)
print('Z_liq', Z_liq)

# Cálculo do fator Z do gás:
Z_gas = calculate_Z_gas(func_Z_gas)
print('Z_liq', Z_gas)


