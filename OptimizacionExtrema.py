import numpy as np 
import pandas as pd
import sys  

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

def funcionCosto(solucion,peso,capacidad,precio):
    peso_total = np.sum(solucion*peso)
    costo_total = np.sum(solucion*precio)
    if(peso_total <= capacidad):
        return solucion, costo_total
    else:
        solucion = np.zeros_like(solucion)
        return solucion,0

def Calcular_Fitness(solucion,peso,precio,capacidad,probabilidades):
    peso_total = np.sum(solucion * peso)
    fitness = precio/peso
    if(peso_total<=capacidad):
        indices = np.where(solucion == 0)[0]
        elegido = ruleta(probabilidades[:np.shape(indices)[0]])
        fitness_0=[fitness[i] for i in indices]
        for i in range(np.shape(fitness_0)[0]):
            for j in range(np.shape(fitness_0)[0]):
                if(fitness_0[j] > fitness_0[i]):
                    aux_index = indices[i]
                    aux_fitness = fitness_0[i]
                    indices[i] = indices[j]
                    fitness_0[i]=fitness_0[j]
                    indices[j]= aux_index
                    fitness_0[j] = aux_fitness
        solucion[indices[elegido]] = 1                
    else:
        indices = np.where(solucion == 1)[0]
        elegido = ruleta(probabilidades[:np.shape(indices)[0]])
        fitness_1=[fitness[i] for i in indices]
        for i in range(np.shape(fitness_1)[0]):
            for j in range(np.shape(fitness_1)[0]):
                if(fitness_1[j] < fitness_1[i]):
                    aux_index = indices[i]
                    aux_fitness = fitness_1[i]
                    indices[i] = indices[j]
                    fitness_1[i]=fitness_1[j]
                    indices[j]= aux_index
                    fitness[j] = aux_fitness
        solucion[indices[elegido]] = 0
    #costo = np.sum(solucion*precio)
    return solucion




def ruleta(probabilidades):
    random = np.random.rand()
    acumulada = np.cumsum(probabilidades)
    dividendo = np.sum(probabilidades)
    acumulada = acumulada/dividendo
    for i, acumulada in enumerate(acumulada) :
        if acumulada >= random:
            return i



def VectorProbabilidad(n, tau):
    probabilidades = np.array([i**(-tau) for i in range(1,n+1)]) #usando la expresion Pi = i^(-tau) #efinir bien i
    probabilidades /= np.sum(probabilidades) #aqui se normaliza para que la suma de los valores sea 1
    return probabilidades

    
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
precio= datos[:,1]
peso = datos[:,2]
solucionInicial = np.random.randint(0,2,n)
mejor_solucion,mejor_costo = funcionCosto(solucionInicial,peso,c,precio)
probabilidades = VectorProbabilidad(n,tau)

for i in range(ite):
    prueba_solucion = Calcular_Fitness(mejor_solucion,peso,precio,c,probabilidades)
    nueva_solucion,nuevo_costo = funcionCosto(prueba_solucion,peso,c,precio)
    if(nuevo_costo>mejor_costo):
        mejor_solucion = nueva_solucion
        mejor_costo = nuevo_costo
        capacidad = np.sum(peso*nueva_solucion)
        print(mejor_solucion, mejor_costo, capacidad)
        


