import numpy as np

#2.
# a. Llenar y mostrar una NxM elementos. 
def llenarMatriz(m, N, M):
    for i in range(N):
        for j in range(M):
            print("Ingrese valor")
            m[i][j] = input()

# b. Encontrar la matriz transpuesta
def matrizTranspuesta(m ,mT, M, N):
    for i in range(M):
        for j in range(N):
            mT[i][j] = m[j][i]

if __name__ == '__main__':
    

    #Asegurarse que el tamanio es mayor que 0
    while True:
        #Pidiendo tamanio de la matriz
        N = int(input("Ingrese el tamanio de las filas: "))
        M = int(input("Ingrese el tamanio de las columnas: "))

        if (N > 0) and (M > 0):
            break
    
    #Matriz de ceros con tamanio NxM
    m = np.zeros((N,M))
    print("\nMatriz de ceros tamanio ", N, "x", M, ": ")
    print(m)
    llenarMatriz(m, N, M)
    print("\nMatriz llena tamanio ", N, "x", M, ": ")
    print(m)

    #Matriz transpuesta de tamanio MxN
    mT = np.zeros((M,N))
    matrizTranspuesta(m, mT, M, N)
    print("\nMatriz transpuesta de tamanio ", M, "x", N, ": ")
    print(mT)

    

