# Importando Bibliotecas:
import numpy as np
import math as mt
import matplotlib.pyplot as plt
from ki_est import calculate_Ki
from frac_mol import calculate_xi, calculate_yi
from rachford_rice import calculate_f, calculate_f_, calculate_RR
from newton_raphson import calculate_NR, calculate_L
from prop_red import calculate_ppr, calculate_tpr
from parametros_eec import calculate_mwi, calculate_alpha, calculate_Ai, calculate_Aij, calculate_A_gas, calculate_A_liq, calculate_B_gas, calculate_B_liq, calculate_Bi, calculate_A_final_gas, calculate_A_final_liq, calculate_B_final_gas, calculate_B_final_liq
from factor_Z import calculate_Z_liq
from factor_Z import calculate_Z_gas
from fugacity import calculate_Delta, calculate_phi_gas, calculate_phi_liq, calculate_phi_fug_gas, calculate_phi_fug_liq, calculate_fugacity_gas, calculate_fugacity_liq
from eq_phase import calculate_eq_phase
from massa_especific import calculate_M_liq, calculate_M_gas, calculate_rho_o, calculate_rho_g
from Ki_est_novo import calculate_Ki_novo

def calculate_avalia_final(list_wi:np.ndarray, P:float, T:float, list_Pc:np.ndarray, list_Tc:np.ndarray, ohm_b:float, ohm_a:float, list_Zi:np.ndarray, eec:str, R:float, delta_1:float, delta_2:float, M:np.ndarray, V:np.ndarray) -> np.ndarray:
    # Estimativa do valor de Ki inicial:
    Ki = calculate_Ki(P, T, list_Pc, list_Tc, list_wi)
    print('Ki', Ki)

    for i in range(len(list_wi)):
        # Propriedades Pseudo-Reduzidas:
        ppr = calculate_ppr(P, list_Pc)
        print('ppr', ppr)

        tpr = calculate_tpr(T, list_Tc)
        print('tpr', tpr)

        # Parâmetros da eec:
        # Cálculo dos Parâmetros Bi:
        Bi = calculate_Bi(list_Tc, list_Pc, R, list_wi, ohm_b)
        print('Bi', Bi)

        # Cálculo de Vr/RR: vai retornar Vr e L
        Vr = calculate_NR(list_wi, list_Zi, Ki)
        print('O valor de Vr é:', Vr)

        L = calculate_L(Vr)
        print('L', L)

        # Cálculo de frações molares:
        # Cálculo de yi:
        yi = calculate_yi(list_Zi, Ki, Vr, list_wi)
        print('yi', yi)

        # Cálculo de xi:
        xi = calculate_xi(list_Zi, Ki, Vr, list_wi)
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

        alpha = calculate_alpha(mwi, list_Tc, T, list_wi)
        print('alpha', alpha)

        # Cálculo de Ai:
        Ai = calculate_Ai(list_Tc, list_Pc, R, list_wi, ohm_a)
        print('Ai', Ai)

        # Cálculo de Aij:
        Aij = calculate_Aij(Ai, list_wi)
        print('Aij', Aij)
        
        # Cálculo de A_gas:
        A_gas = calculate_A_gas(yi, Aij, alpha, Ki)
        print('A_gas', A_gas)

        # Cálculo de A_liq:
        A_liq = calculate_A_liq(xi, Aij, alpha, Ki)
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

        phi_fug_gas = calculate_phi_fug_gas(Bi, B_final_gas, A_final_gas, delta_1, delta_2, list_wi, Z_gas, Delta, phi_gas)
        print('phi_fug_gas', phi_fug_gas)

        fugacity_liq = calculate_fugacity_liq(phi_fug_liq, P, xi, list_wi)
        print('fugacity_liq', fugacity_liq)

        fugacity_gas = calculate_fugacity_gas(phi_fug_gas, P, yi, list_wi)
        print('fugacity_gas', fugacity_gas)

        # Cálculo das Massas Específicas:
        M_liq = calculate_M_liq(xi, list_wi, M)
        print('M_liq', M_liq)

        M_gas= calculate_M_gas(yi, list_wi, M)
        print('M_gas', M_gas)

        rho_o = calculate_rho_o(M_liq, P, R, T, Z_liq)
        print('rgo_o', rho_o)

        rho_g = calculate_rho_g(M_gas, P, R, T, Z_gas)
        print('rgo_g', rho_g)

        eq_phase = calculate_eq_phase(fugacity_liq, fugacity_gas, list_wi)

        if eq_phase < 10**-8:
            for i in range(len(list_wi)):
                Ki[i] = yi[i]/xi[i]
            avalia = [Vr, L, xi, yi, Z_liq, Z_gas, Ki]
            print('avalia', avalia)
        else:
            print(Ki)
            Ki = calculate_Ki_novo(list_wi, fugacity_liq, fugacity_gas, Ki)

    return avalia





