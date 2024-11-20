import numpy as np 
import pandas as pd
import random
import sys 
import os 

def CostoFactibilidad(solucion, elementos, peso_max):
    peso_total = 0
    costo_total = 0
    for i, contiene in enumerate(solucion):
        if contiene == 1:
            peso_total += elementos[i]['peso']
            costo_total += elementos[i]['valor']

    factible = peso_total <= peso_max
    return costo_total, factible

def GenerarSoluciónInicial(n, peso, peso_max):
    Solucion = [0] * n
    peso_actual = 0
    indice = list(range(n))
    random.shuffle(indice)
    for i in indice:
        if peso_actual + peso[i] <= peso_max:
           Solucion[i] = 1
           peso_actual += peso[i]
    return Solucion


    