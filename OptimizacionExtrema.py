import numpy as np 
import pandas as pd
import sys 
import os 

def LeerArchivo(entrada):
    ArchivoEntrada = pd.read_table(entrada,header = None)
    nombre_problema = ArchivoEntrada[0][0]
    n = int(ArchivoEntrada[0][1].split()[1])
    c = int(ArchivoEntrada[0][2].split()[1])
    z = int(ArchivoEntrada[0][3].split()[1])
    ArchivoEntrada = ArchivoEntrada.drop(ArchivoEntrada.index[0:5],axis=0)
    datos = ArchivoEntrada[0].str.split(",", expand=True)
    datos = datos.astype('int32').to_numpy()
    return n,c,z,datos

def CostoFactibilidad(solucion, elementos, peso_max):
    peso_total = 0
    costo_total = 0
    for i, contiene in enumerate(solucion):
        if contiene == 1:
            peso_total += elementos[i]['peso']
            costo_total += elementos[i]['valor']

    factible = peso_total <= peso_max
    return costo_total, factible

def funcionCosto(solucion,costo,capacidad):
    pos_solucion = solucion*costo
    suma_pos_solucion = np.sum(pos_solucion)
    if(suma_pos_solucion <= capacidad):
        return pos_solucion, suma_pos_solucion
    else:
        pos_solucion = np.ones_like(solucion)*-1
        return pos_solucion,-1

if len(sys.argv)==5:
    semilla = int(sys.argv[1])
    ite = int(sys.argv[2]) #iteracion  
    tau = float(sys.argv[3]) #tasa de evaporacion
    entrada = sys.argv[4] #nombre del archivo a leer    #falta el archivo de salida
    print(semilla, ite, tau, entrada)
else:
    print("Error en la entrada de los parámetros")
    print("Los parámetros a ingresar son: Semilla TamañoColonia Iteraciones TasaDeEvaporacion Beta q0 nombreArchivo")
    sys.exit(0)

np.random.seed(semilla)
n,c,z,datos = LeerArchivo(entrada)
print(n)
print(c)
print(z)
precio= datos[:,1]
peso = datos[:,2]
solucionInicial = np.random.randint(0,2,n)
mejor_solucion,mejor_costo = funcionCosto(solucionInicial,precio,c)
print(mejor_solucion,mejor_costo)

#gurardar mejor solucion
#crear de probabilidades
#funcion crear ruleta
#funcion calculo fitness
#funcion selecciona item a reemplazar
