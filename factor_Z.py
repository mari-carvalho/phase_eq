# Importando Bibliotecas:
import numpy as np
import scipy
import math as mt
import matplotlib.pyplot as plt


'''def func_Z_liq(Z: float, B_final_liq: float, A_final_liq: float, delta_1: float, delta_2: float):

    C1 = 1.
    C2 = ((delta_1 + delta_2 -1)*B_final_liq-1)
    C3 = (A_final_liq + delta_1*delta_2*B_final_liq**2) - (delta_1+delta_2) *B_final_liq*(B_final_liq + 1)
    C4 = -(A_final_liq*B_final_liq + delta_1*delta_2*B_final_liq**2 * (B_final_liq+1))

    func_Z_liq = C1*Z**3 + C2*Z**2 + C3*Z + C4

    return func_Z_liq


def calculate_Z_liq(func_Z_liq) -> float:

    Z_liq = scipy.optimize.newton(func_Z_liq, 0.5, fprime=None, args=(), tol=1.48e-08, maxiter=50, fprime2=None, x1=None, rtol=0.0, full_output=False, disp=True)

    return Z_liq

def func_Z_gas(Z: float, B_final_gas:float, A_final_gas: float, delta_1:float, delta_2:float):

    C1 = 1.
    C2 = ((delta_1 + delta_2 -1)*B_final_gas-1)
    C3 = (A_final_gas + delta_1*delta_2*B_final_gas**2) - (delta_1+delta_2) *B_final_gas*(B_final_gas + 1)
    C4 = -(A_final_gas*B_final_gas + delta_1*delta_2*B_final_gas**2 * (B_final_gas+1))

    return C1*Z**3 + C2*Z**2 + C3*Z + C4


def calculate_Z_gas(func_Z_gas) -> float:

    Z_gas = scipy.optimize.newton(func_Z_gas, 0.5, fprime=None, args=(), tol=1.48e-08, maxiter=50, fprime2=None, x1=None, rtol=0.0, full_output=False, disp=True)

    return Z_gas'''

# Z novo
def calculate_Z_liq(delta_1:float, delta_2:float, B_final_liq:np.ndarray, A_final_liq: np.ndarray) -> float:
    
    C1 = 1.
    C2 = ((delta_1 + delta_2 -1)*B_final_liq-1)
    C3 = (A_final_liq + delta_1*delta_2*B_final_liq**2) - (delta_1+delta_2) *B_final_liq*(B_final_liq + 1)
    C4 = -(A_final_liq*B_final_liq + delta_1*delta_2*B_final_liq**2 * (B_final_liq+1))

    inter = 0                              # cálculo das interações 
    Z_liq = 0.5                                  # primeiro valor de z a ser testado 
    error = 1  
    tol = 1*10**-3                                               # tolerância para que o looping continue acontecendo 
    dz_liq = 1*10**-5                                     # valor da diferencial 
    func_liq = C1*Z_liq**3 + C2*Z_liq**2 + C3*Z_liq + C4            # função de Newton-Raphson 
    func2_liq = C1*(Z_liq+dz_liq )**3 + C2*(Z_liq+dz_liq )**2 + C3*(Z_liq+dz_liq ) + C4
    dfunc_liq = 0
    while 1:                               # enquanto o erro for menor que a tolerância (1e-3), o looping vai acontecer 
        Z_old = Z_liq                             # o novo valor de z a ser testado é inserido no lugar do z antigo (0.5 - primeiro)
        for i in range(0,9):
            dfunc_liq  = func2_liq - func_liq/dz_liq      # deriavada numérica, não analítica - onde dz não pode ser muito pequeno, pois é um denomidador 
            Z_liq = Z_liq - func_liq/dfunc_liq                        # um novo valor de z é calculado com base na função de z e em sua derivada
            error = abs(Z_liq - Z_old)        # cálculo do erro                                                            
            inter = inter + 1                
                                    
        if np.all(error < tol):
            break
    
    return Z_liq

def calculate_Z_gas(delta_1:float, delta_2:float, B_final_gas:np.ndarray, A_final_gas: np.ndarray) -> float:
    
    C1 = 1.
    C2 = ((delta_1 + delta_2 -1)*B_final_gas-1)
    C3 = (A_final_gas + delta_1*delta_2*B_final_gas**2) - (delta_1+delta_2) *B_final_gas*(B_final_gas + 1)
    C4 = -(A_final_gas*B_final_gas + delta_1*delta_2*B_final_gas**2 * (B_final_gas+1))

    inter = 0                              # cálculo das interações 
    Z_gas= 0.5                                  # primeiro valor de z a ser testado 
    error = 1  
    tol = 1*10**-3                                               # tolerância para que o looping continue acontecendo 
    dz_gas = 1*10**-5                                       # valor da diferencial 
    func_gas = C1*Z_gas**3 + C2*Z_gas**2 + C3*Z_gas + C4            # função de Newton-Raphson 
    func2_gas = C1*(Z_gas+dz_gas )**3 + C2*(Z_gas+dz_gas )**2 + C3*(Z_gas+dz_gas ) + C4
    dfunc_gas = 0
    while 1:                               # enquanto o erro for menor que a tolerância (1e-3), o looping vai acontecer 
        Z_old = Z_gas                             # o novo valor de z a ser testado é inserido no lugar do z antigo (0.5 - primeiro)
        dfunc_gas  = func2_gas - func_gas/dz_gas      # deriavada numérica, não analítica - onde dz não pode ser muito pequeno, pois é um denomidador 
        Z_gas = Z_gas - func_gas/dfunc_gas                        # um novo valor de z é calculado com base na função de z e em sua derivada
        error = abs(Z_gas - Z_old)        # cálculo do erro                                                            
        inter = inter + 1                
                                    
        if np.all(error < tol):
            break
    
    return Z_gas

