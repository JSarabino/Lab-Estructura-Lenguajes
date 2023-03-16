#librerias
import numpy as np
import sys

# pip3 install --upgrade pip
# pip3 install numpy

def verificarNumero(n):
    if n % 2 == 0:
        print("\nEs par")
    else:
        print("\nEs impar")

def mayorDosNumeros(a,b):
    if a != b:
        if a > b:
            return a
        else:
            return b
    else:
        return None

def llenarVector(v):
    i = 0
    while i < len(v):
        print ("Digite el elemento: ", (i+1))
        v[i] = int(input())
        i = i + 1

def mostrarVector(v):
    for i in range(len(v)):
        print(v[i],end=", ")    

def llenarMatriz(d):
    for i in range(3):
        for j in range(3):
            print("Ingrese valor")
            d[i][j] = input()

def salir():
    print("Hasta luego!")
    sys.exit(0)

#menu
def menuVectores(v,op):
    match op:
        case 1: llenarVector(v)
        case 2: mostrarVector(v)
        case 3: salir()

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
        print("Opciones de gestion de vectores.")
        print("1. Llenar \n2. Mostrar \n3. Salir")
        op = int(input("Digite la opcion a realizar: "))
        if op > 0 and op < 4:
            menuVectores(a,op)


#Comando de win para instalar numpy
#py -m pip install numpy
