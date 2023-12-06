# Importando Bibliotecas:
import numpy as np
import scipy
import math as mt
import matplotlib.pyplot as plt
from main import eec


def func_Z(Z: float, B: float, A: float, eos_type: str) -> float:

    delta_1 = 0
    delta_2 = 1

    if eos_type == 'PR':
        delta_1 = 1 + np.sqrt(2)
        delta_2 = 1 - np.sqrt(2)

    C1 = 1.
    C2 = ((delta_1 + delta_2 -1)*B-1)
    C3 = (A + delta_1*delta_2*B**2) - (delta_1+delta_2) *B*(B + 1)
    C4 = -(A*B + delta_1*delta_2*B**2 * (B+1))

    return C1*Z**3 + C2*Z**2 + C3*Z + C4


def calculate_Z():



    # Z = scipy.optimize.newton(z, 0.5, fprime=None, args=(), tol=1.48e-08, maxiter=50, fprime2=None, x1=None, rtol=0.0, full_output=False, disp=True)


