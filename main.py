# Importando Bibliotecas:
import numpy as np
import math as mt
import matplotlib.pyplot as plt
import scipy 

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

eq_phase = calculate_eq_phase(fugacity_liq, fugacity_gas, list_wi)




