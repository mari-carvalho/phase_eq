# Importando Bibliotecas:
import numpy as np
import scipy
import math as mt
import matplotlib.pyplot as plt

# Z novo
def calculate_Z_liq(delta_1:float, delta_2:float, B_final_liq:float, A_final_liq:float) -> float:
    
    C1 = 1.
    C2 = ((delta_1 + delta_2 -1)*B_final_liq-1)
    C3 = (A_final_liq + delta_1*delta_2*B_final_liq**2) - (delta_1+delta_2) *B_final_liq*(B_final_liq + 1)
    C4 = -(A_final_liq*B_final_liq + delta_1*delta_2*B_final_liq**2 * (B_final_liq+1))

    Z_liq = 0.11                              # primeiro valor de z a ser testado
    func_liq = C1*Z_liq**3 + C2*Z_liq**2 + C3*Z_liq + C4            # função de Newton-Raphson 

    itMax = 100
    for it in range(itMax):
        Dfunc_liqDZliq = 3.0*C1*Z_liq**2 + 2.0*C2*Z_liq + C3
        Z_liq = Z_liq - func_liq/Dfunc_liqDZliq
        func_liq = C1*Z_liq**3 + C2*Z_liq**2 + C3*Z_liq + C4            # função de Newton-Raphson
        print("iteration : ", it)
        print("func_liq : ", func_liq)
        print("Z_liq : ", Z_liq)
        if func_liq < 1.0e-6:
            return Z_liq
        
    print("Newton Raphson nao convergiu para calcilate_Z_liq")
    return


def calculate_Z_gas(delta_1: float, delta_2: float, B_final_gas: float, A_final_gas: float) -> float:
    C1 = 1.
    C2 = ((delta_1 + delta_2 - 1) * B_final_gas - 1)
    C3 = (A_final_gas + delta_1 * delta_2 * B_final_gas ** 2) - (delta_1 + delta_2) * B_final_gas * (B_final_gas + 1)
    C4 = -(B_final_gas * B_final_gas + delta_1 * delta_2 * B_final_gas ** 2 * (B_final_gas + 1))

    Z_gas = 0.6 # primeiro valor de z a ser testado
    func_gas = C1 * Z_gas ** 3 + C2 * Z_gas ** 2 + C3 * Z_gas + C4  # função de Newton-Raphson

    itMax = 100
    for it in range(itMax):
        Dfunc_gasDZgas = 3.0 * C1 * Z_gas ** 2 + 2.0 * C2 * Z_gas + C3
        Z_gas = Z_gas - func_gas / Dfunc_gasDZgas
        func_gas= C1 * Z_gas ** 3 + C2 * Z_gas ** 2 + C3 * Z_gas + C4  # função de Newton-Raphson
        print("iteration : ", it)
        print("func_liq : ", func_gas)
        print("Z_liq : ", Z_gas)
        if func_gas < 1.0e-6:
            return Z_gas

    print("Newton Raphson nao convergiu para calculate_Z_gas")
    return

