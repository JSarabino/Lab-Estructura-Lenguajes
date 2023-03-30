import os
import sys

# 1. Funcion para cargar los datos de videoBeans.txt, profesores.txt y prestamos.txt 
def cargarDatosLG(localizadorArchivo, columnas):
    try:
        listado = []
        elemento = ()
        with open (localizadorArchivo, 'r') as archivo:
            for linea in archivo:
                elemento = linea.split(', ',columnas)
                elemento = list(map(lambda l:l.rstrip('\n'), elemento))
                listado.append(elemento)
        archivo.close()
        return listado
    except IOError:
        mensaje = "Error en la carga de datos."
        print(mensaje)

#Menu para los prestamos
def menuPrestamos(op, listaVideoBeans, listaProfesores):
    match op:
        case 1:
            borrarPantalla() 
            listaVideoBeans = actualizarvideoBeans()
            consultarVideoBeans(listaVideoBeans)
        case 2: 
            borrarPantalla() 
            consultarPrestamos()
        case 3: actualizarvideoBeans()
        case 4: 
            num = int(input("\nIngrese el numero: "))
        case 5: salir()

#Permite consultar los video beans
def consultarVideoBeans(listaVideoBeans):
    print("\nTotal: ", len(listaVideoBeans))
    print("Codigo   | Marca  |  Referencia   |   Estado")
    for i in range(len(listaVideoBeans)):
        codigo = listaVideoBeans[i][0]
        marca = listaVideoBeans[i][1]
        referencia = listaVideoBeans[i][2]
        estado = listaVideoBeans[i][3]
        print(codigo, "   ", marca, "    ", referencia, "  ", estado)    
    print("")

#Permite consultar los prestamos
def consultarPrestamos():
    #Cargar los datos de los prestamos
    listaPrestamos = []
    listaPrestamos = cargarDatosLG(localizadorPrestamos,6)

    #Manejo de la lista de prestamos
    if (not listaPrestamos):
        print("\nLista de prestamos vacia.")
    else:
        #Totales de prestamos activos y terminados
        cantActivos = 0
        cantTerminados = 0

        #Imprmir los activos
        for i in range(len(listaPrestamos)):
            if listaPrestamos[i][5] == "Activo":
                print(listaPrestamos[i])
                cantActivos += 1
        print("Total activos: ", cantActivos, "\n")

        #imprimir los terminados
        for i in range(len(listaPrestamos)):
            if listaPrestamos[i][5] == "Terminado":
                print(listaPrestamos[i])
                cantTerminados += 1
        print("Total terminados: ", cantTerminados, "\n")

#


#-------------Funciones extras-------------
#Actualizar datos
def actualizarvideoBeans():
    listaVideoBeans = []
    listaVideoBeans = cargarDatosLG(localizadorVideoBeans, 4)
    return listaVideoBeans

def actualizarPrestamos():
    listaPrestamos = []
    listaPrestamos = cargarDatosLG(localizadorPrestamos,6)
    return listaPrestamos

# Salir del programa
def salir():
    print("\nHasta luego!")
    sys.exit(0)

#Borrar pantalla segun sistema
def borrarPantalla():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


#-------------Programa principal-------------
if __name__ == '__main__':
    #Usuario y contrasenia
    usuario = "admin"
    password = "12345"

    #Direccion de los .txt
    localizadorVideoBeans ='Practica4/videoBeans.txt'
    localizadorProfesores ='Practica4/profesores.txt'
    localizadorPrestamos = 'Practica4/prestamos.txt'

    #Listas vacias
    listaVideoBeans = []
    listaProfesores = []

    #Llenando las listas
    listaVideoBeans = cargarDatosLG(localizadorVideoBeans, 4)
    listaProfesores = cargarDatosLG(localizadorProfesores, 3)

    #Manejo de las listas
    if (not listaVideoBeans):
        print("\nLista de video beans vacia.")
    elif (not listaProfesores):
        print("\nLista de profesores vacia.")
    else:
        #La carga de datos es exitosa
        listaVideoBeans = cargarDatosLG(localizadorVideoBeans, 4)
        listaProfesores = cargarDatosLG(localizadorProfesores, 3)
        print("Carga de datos completa.")
        
        #2. Comprobar el inicio de sesion
        while True:
            login = input("Digite el usuario: ")
            if login == usuario:
                borrarPantalla() 
                break

        while True:
            passw = input("Digite la clave: ")
            if passw == password:
                borrarPantalla() 
                break
        
        #Llamar al menu de prestamos
        while True:
            print("\nOpciones de gestion de prestamos.")
            print("1. Consultar Video Beans. \n2. Consultar préstamos. \n3. Realizar préstamos. \n4. Finalizar préstamos. \n5. Cerrar sesión.")
            op = int(input("\nDigite la opcion a realizar: "))
            if op > 0 and op < 6:
                menuPrestamos(op, listaVideoBeans, listaProfesores)
    
