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


def funcionCosto(solucion,costo,capacidad):
    pos_solucion = solucion*costo
    suma_pos_solucion = np.sum(pos_solucion)
    if(suma_pos_solucion <= capacidad):
        return pos_solucion, suma_pos_solucion
    else:
        pos_solucion = np.ones_like(solucion)*-1
        return pos_solucion,-1
#esta parte la hice yo (Matito)
def calculofitness(solucion, pesos, precio, capacidad):
    peso_total = np.sum(solucion * pesos)
    valor_total = np.sum(solucion * precio)
    factible = peso_total <= capacidad #se ve si se excede el peso maximo
    if factible:
       return valor_total
    else: 
       return -1
    
    
def ruleta(probabilidades):
    random = np.random.rand()
    acumulada = np.cumsum(probabilidades)
    for i, acumulada in enumerate(acumulada):
        if random <= acumulada:
            return i


def VectorProbabilidad(n, tau):
    probabilidades = np.array([i**(-tau) for i in range(1,n+1)]) #usando la expresion Pi = i^(-tau)
    probabilidades /= np.sum(probabilidades) #aqui se normaliza para que la suma de los valores sea 1
    return probabilidades
#yo hice esta funcion que hace que se ajuste la solucion en caso ser infactible, volviendola factible(Matito)
def Ajustarsolucion(solucion, pesos, capacidad):
    peso_total = np.sum(solucion * peso)
    while peso_total > capacidad #mientras el peso exceda su capacidad tenemos que sacar un elemento de la mochila
        indice = np.where(solucion == 1)[0] #se selecciona los indices
        if len(indice == 0)
    #falta
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
mejor_fitness = calculofitness(solucionInicial,peso,precio,c)
print(mejor_solucion,mejor_costo)
vector_probabilidades = VectorProbabilidad(n,tau)
print(vector_probabilidades)

#Yo hice esto de acuerdo a la diapo del algoritmo del pdf de la linea 6 al 8(Matito)
for iteracion in range(ite):
    j = ruleta(vector_probabilidades)
    nueva_solucion = solucionInicial.copy()
    nueva_solucion[j] = 1 - nueva_solucion[j]
    fitness_nueva = calculofitness(solucionInicial, peso, precio, c)

    if fitness_nueva > mejor_fitness:
        mejor_solucion = nueva_solucion.copy()
        mejor_fitness = fitness_nueva

    print(f"iteracion {iteracion + 1 }: Mejor fitness = {mejor_fitness}")

print(mejor_solucion)
print(mejor_fitness)

#guardar mejor solucion
#crear de probabilidades
#funcion crear ruleta
#funcion calculo fitness
#funcion selecciona item a reemplazar

#lo que falta
#como es infactible hay que ajustar la solucion eliminando objetos de la mochila
#contar los elementos que estan dentro de la mochila
