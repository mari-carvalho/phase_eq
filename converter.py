# Importando Bibliotecas:
import numpy as np
import math as mt
import matplotlib.pyplot as plt

def calculate_converter_ppr(ppr:np.ndarray) -> np.ndarray:

    ppr_converter =  np.zeros(len(ppr))

    for i in range(len(ppr)):
        ppr_converter = ppr[i]