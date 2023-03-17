#librerias
import numpy as np
import math
import sys

#1.
# a. Procedimiento que determina si un número es par o impar.
def verificarNumero(n):
    if n % 2 == 0:
        print("\nEs par")
    else:
        print("\nEs impar")

# b. Función que permite determinar cuál es el mayor de dos números enteros ingresados por un usuario.
def mayorDosNumeros(a,b):
    if a != b:
        if a > b:
            return a
        else:
            return b
    else:
        return None

# C. Llenar y mostrar un vector de n elementos. 
def llenarVector(v):
    i = 0
    while i < len(v):
        print("")
        print ("Digite el elemento: ", (i+1))
        v[i] = int(input())
        i = i + 1

def mostrarVector(v):
    print("\nEl vector es:")
    for i in range(len(v)):
        print(v[i],end=", ")    
    print("")

# d. Crear un menú que permita realizar las siguientes funcionalidades respecto al punto c:
# Menu
def menuVectores(v,op):
    match op:
        case 1: llenarVector(v)
        case 2: mostrarVector(v)
        case 3: maxVector(v)
        case 4: 
            num = int(input("\nIngrese el numero: "))
            buscarIndex(v,num)
        case 5: 
            resultado = 0
            resultado = desviacionEstandar(v)
            print("\nLa desviacion estandar es: ", resultado)
        case 6: salir()

# I. Procedimiento que permite encontrar el máximo elemento del vector.
def maxVector(v):
    max = v[0]
    for i in range (len(v)):
        if max < v[i]:
            max = v[i]
    
    print("\nEl valor maximo es: ", max)

# II. Procedimiento que busca un elemento en el vector y determinar cuál es su posición.
def buscarIndex(v, num):
    index = -1
    for i in range(len(v)):
        if v[i] == num:
            index = i
            break
    
    if index == -1:
        print("\nEl numero ingresado no se encuentra en el vector")
    else:
        print("\nEL numero ", num, " tiene la posicion ", (index+1))


# III. funcion que permite encontrar la desviación estándar de una muestra de valores almacenados en un vector.
def desviacionEstandar(v):
    return math.sqrt( calcularSumatoria(v) / (len(v) - 1) )

# Funcion para calcular la sumatoria de (x - xm)^2
def calcularSumatoria(v):
    suma = 0
    media = calcularMedia(v)
    for i in range(len(v)):
        suma = suma + ((v[i] - media) ** 2)
    return suma

# Funcion para calcular la media de un vector de numeros
def calcularMedia(v):
    media = 0
    for i in range(len(v)):
        media = media + v[i]
    
    if media != 0:
        media = media / len(v)
    
    return media

# Salir del programa
def salir():
    print("\nHasta luego!")
    sys.exit(0)


#  Por organizar
def llenarMatriz(d):
    for i in range(3):
        for j in range(3):
            print("Ingrese valor")
            d[i][j] = input()

# Main
if __name__ == '__main__':
    #x = int(input("Ingrese un numero: "))
    #verificarNumero(x)
    
    #print("Digite numero 1: ")
    #n1 = int(input())
    #print("Digite numero 2: ")
    #n2 = int(input())

    #rta = mayorDosNumeros(n1,n2)

    #if (rta != None):
    #    print("El mayor es: ", rta)
    #else:
    #    print("Son numeros iguales.")

    
    #Simulando el do while
    while True:
        print("Digite el tamanio del vector a crear: ")
        t = int(input())
        if t > 0:
            break
    """
    #Declarando matriz vacia
    m = np.zeros((3,3))
    print("Matriz de ceros")
    print(m)
    llenarMatriz(m)
    print("Matriz creada")
    print(m)
    """
    #Declarar el vector
    a = np.empty(t)
    #Crear un menu
    while True:
        print("\nOpciones de gestion de vectores.")
        print("1. Llenar \n2. Mostrar \n3. Maximo numero del vector \n4. Buscar posicion de un numero \n5. Desviacion estandar \n6. Salir")
        op = int(input("Digite la opcion a realizar: "))
        if op > 0 and op < 7:
            menuVectores(a,op)


#Comando de windows para instalar numpy
# pip3 install --upgrade pip
# pip3 install numpy

#Segunda opcion
#py -m pip install numpy
