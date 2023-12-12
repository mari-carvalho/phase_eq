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
from fugacity import calculate_Delta, calculate_phi_gas, calculate_phi_liq, calculate_phi_fug_gas, calculate_phi_fug_liq, calculate_fugacity_gas, calculate_fugacity_liq
from eq_phase import calculate_eq_phase
from massa_especific import calculate_M_liq, calculate_M_gas, calculate_rho_o, calculate_rho_g
# Dados - Iniciando as Listas:
list_Zi = np.array([0.5, 0.5])
print('Zi', list_Zi)
list_Pc = np.array([45.99*10**5, 73.74*10**5]) # Pa
print('Pc', list_Pc)
list_Tc = np.array([190.56, 304.12]) # K
print('Tc', list_Tc)
list_wi = np.array([0.011, 0.225]) 
print('wi', list_wi)
M = np.array([12, 44.01])
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
print('Ki', Ki)

# Propriedades Pseudo-Reduzidas:
ppr = calculate_ppr(P, list_Pc)
print('ppr', ppr)

tpr = calculate_tpr(T, list_Tc)
print('tpr', tpr)

# Parâmetros da eec:
# Cálculo dos Parâmetros Bi:
Bi = calculate_Bi(ppr, tpr, list_wi, ohm_b)
print('Bi', Bi)

# Cálculo de Vr/RR: vai retornar Vr e L
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
mwi = calculate_mwi(list_wi, eec)
print('mwi', mwi)

# Cálculo de Ai:
Ai = calculate_Ai(ppr, tpr, mwi, list_wi, ohm_a)
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
Z_liq = calculate_Z_liq(delta_1, delta_2, B_final_liq, A_final_liq)
print('Z_liq', Z_liq)

# Cálculo do fator Z do gás:
Z_gas = calculate_Z_gas(delta_1, delta_2, B_final_gas, A_final_gas)
print('Z_gas', Z_gas)

# Cálculo da fugacidade:
Delta = calculate_Delta(delta_1, delta_2)
print('Delta', Delta)

phi_liq = calculate_phi_liq(Aij, xi, list_wi)
print('phi_liq', phi_liq)

phi_gas = calculate_phi_gas(Aij, yi, list_wi)
print('phi_gas', phi_gas)

phi_fug_liq = calculate_phi_fug_liq(Bi, B_final_liq, A_final_liq, delta_1, delta_2, list_wi, Z_liq, Delta, phi_liq)
print('phi_fug_liq', phi_fug_liq)

phi_fug_gas= calculate_phi_fug_gas(Bi, B_final_gas, Z_gas, A_final_gas, delta_1, delta_2, list_wi, Z_gas, Delta, phi_gas)
print('phi_fug_gas', phi_fug_gas)

fugacity_liq = calculate_fugacity_liq(phi_fug_liq, P, xi, list_wi)
print('fugacity_liq', fugacity_liq)

fugacity_gas = calculate_fugacity_gas(phi_fug_gas, P, yi, list_wi)
print('fugacity_gas', fugacity_gas)

# Equilíbrio de Fases:
eq_phase = calculate_eq_phase(list_wi)

# Cálculo das Massas Específicas:
M_liq = calculate_M_liq(xi, list_wi, M)
print('M_liq', M_liq)

M_gas= calculate_M_gas(yi, list_wi, M)
print('M_gas', M_gas)

rho_o = calculate_rho_o(M_liq, P, R, T, Z_liq)
print('rgo_o', rho_o)

rho_g = calculate_rho_g(M_gas, P, R, T, Z_gas)
print('rgo_g', rho_g)


