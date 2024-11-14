import numpy as np 
import pandas as pd
import sys 
import os 

def costo_factibilidad(solucion, elementos, peso_max):
    #iniciamos los valores del peso y costo a 0
    peso_total = 0
    costo_total = 0
    # realizamos listado de elementos en la mochila
    for i, contiene in enumerate(solucion):
        if contiene == 1 #en el caso si el elemento se encuentra en la mochila
            peso_total += elementos[i]['peso']
            costo_total += elementos[i]['valor']

    factible = peso_total <= peso_max
    return costo_total, factible