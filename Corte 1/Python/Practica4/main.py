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

# 2. Inicio de sesion
def pantallaInicio():
    while True:
        print("\nBienvenido")
        print("1. Iniciar sesion. \n2. Salir.")
        opInicio = int(input("\nDigite la opcion a realizar: "))
        if opInicio > 0 and opInicio < 3:
            opcionInicio(opInicio)

def opcionInicio(opInicio):
    match opInicio:
        case 1:
            comprobarSesion()
        case 2: 
            salir()

def comprobarSesion():
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

# Menu para los prestamos
def menuPrestamos(op, listaVideoBeans, listaProfesores):
    match op:
        case 1:
            listaVideoBeans = actualizarvideoBeans()
            consultarVideoBeans(listaVideoBeans)
        case 2: 
            listaPrestamos = actualizarPrestamos()
            consultarPrestamos(listaPrestamos)
        case 3: 
            listaVideoBeans = actualizarvideoBeans()
            realizarPrestamo(listaVideoBeans, listaProfesores)
        case 4: 
            listaVideoBeans = actualizarvideoBeans()
            listaPrestamos = actualizarPrestamos()
            finalizarPrestamo(listaVideoBeans, listaPrestamos, listaProfesores)
        case 5: pantallaInicio()

# 2. i. Permite consultar los video beans
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

# 2. ii. Permite consultar los prestamos
def consultarPrestamos(listaPrestamos):

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
        print("\nTotal activos: ", cantActivos, "\n")

        #imprimir los terminados
        for i in range(len(listaPrestamos)):
            if listaPrestamos[i][5] == "Terminado":
                print(listaPrestamos[i])
                cantTerminados += 1
        print("Total terminados: ", cantTerminados, "\n")

# 2. iii. Permite realizar un prestamo
def realizarPrestamo(listaVideoBeans, listaProfesores):
    #cant sirve para comprobar si hay video beans disponibles
    cant = videosDisponibles(listaVideoBeans)

    if cant > 0:
        #encontrado sirve para saber si la cedula del profesor existe
        cedula = input("\nIngrese la cedula: ")
        encontrado = comprobarCedula(listaProfesores, cedula)
        if encontrado == True:
            while True:
                codVideo = input("Ingrese el codigo del video bean: ")
                if comprobarCodAdd(listaVideoBeans, codVideo) == True:
                    break
            
            agregarPrestamo(cedula, codVideo)

        else:
            print("\nLa cedula ingresada no existe.")
    else:
        print("\nNo hay video beans disponibles.")

# 2. iV. Finalizar préstamos.

def finalizarPrestamo(listaVideoBeans, listaPrestamos, listaProfesores):
    codVideo = input("\nIngrese el codigo del video bean prestado: ")
    if comprobarCodRemove(listaPrestamos, codVideo) == True:
        print("Terminado con exito!")
    else:
        print("No se encontro el prestamo.")


#-------------Funciones extras-------------
#Comprueba que el codigo del video bean sea de un video bean prestado
def comprobarCodRemove(listaPrestamos, codVideo):
    for i in range(len(listaPrestamos)):
        if listaPrestamos[i][3] == codVideo and listaPrestamos[i][5] == "Activo":
            estado = "Disponible"
            filas = [i]
            modEstadoVideoBean(localizadorVideoBeans, estado, filas)
            estadoPrestamo = "Terminado"
            modEstadoPrestamo(localizadorPrestamos, estadoPrestamo, filas)
            return True
    return False

#Comprueba que el codigo del video bean sea de un video bean disponible
def comprobarCodAdd(listaVideoBeans, codVideo):
    for i in range(len(listaVideoBeans)):
        if listaVideoBeans[i][0] == codVideo and listaVideoBeans[i][3] == "Disponible":
            estado = "Prestado"
            filas = [i]
            modEstadoVideoBean(localizadorVideoBeans, estado, filas)
            return True
    return False

#Modifica el estado de los video beans en el archivo .txt
def modEstadoVideoBean(localizadorVideoBeans, estado, filas):
    contenido = list()
    with open(localizadorVideoBeans, 'r+') as archivo:
        contenido = archivo.readlines()
        for fila in filas:
            columnas = contenido[fila].split(', ')
            columnas[3] = estado
            contenido[fila] = ', '.join(columnas) + '\n'          
    with open(localizadorVideoBeans, 'w') as archivo:
        archivo.writelines(contenido)

#Modifica el estado del prestamos en el archivo .txt
def modEstadoPrestamo(localizadorPrestamos, estadoPrestamo, filas):
    contenido = list()
    with open(localizadorPrestamos, 'r+') as archivo:
        contenido = archivo.readlines()
        for fila in filas:
            columnas = contenido[fila].split(', ')
            columnas[5] = estadoPrestamo
            contenido[fila] = ', '.join(columnas) + '\n'          
    with open(localizadorPrestamos, 'w') as archivo:
        archivo.writelines(contenido)

#Ingresa un prestamo
def agregarPrestamo(cedula, codVideo):
    
    fecha = input("Ingrese la fecha: ")
    horaInicio = input("Ingrese la hora inicial: ")
    horaFin = input("Ingrese la hora final: ")
    estado = "Activo"

    #Creamos el formato que tienen los prestamos en el archivo
    linea = "\n" + str(fecha) + ", " + str(horaInicio) + ", " + str(horaFin) + ", " + str(codVideo) + ", " + str(cedula) + ", " + str(estado)
    #Abrimos el archivo en modo append(a) para agregar una linea al final del contenido existente
    archivo = open (localizadorPrestamos, 'a')  
    #Llamamos al metodo write pasando la linea con el formato deseado  
    archivo.write(linea)
    archivo.close()

#Imprmir los video beans disponibles
def videosDisponibles(listaVideoBeans):
    cant = 0
    print("\nVideo beans disponibles:")
    for i in range(len(listaVideoBeans)):
        if listaVideoBeans[i][3] == "Disponible":
            codigo = listaVideoBeans[i][0]
            marca = listaVideoBeans[i][1]
            referencia = listaVideoBeans[i][2]
            estado = listaVideoBeans[i][3]
            print(codigo, "   ", marca, "    ", referencia, "  ", estado)    
            cant += 1
    return cant

#Comprueba un numero de cedula de un profesor
def comprobarCedula(listaProfesores, cedula):
    encontrado = False
    for i in range(len(listaProfesores)):
        if listaProfesores[i][0] == cedula:
            encontrado = True
    return encontrado

#Actualizar datos
def actualizarvideoBeans():
    listaVideoBeans = []
    listaVideoBeans = cargarDatosLG(localizadorVideoBeans, 4)
    return listaVideoBeans

def actualizarPrestamos():
    listaPrestamos = []
    listaPrestamos = cargarDatosLG(localizadorPrestamos,6)
    return listaPrestamos

#Borrar pantalla segun sistema
def borrarPantalla():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

# 2. V. Salir del programa
def salir():
    print("\nHasta luego!")
    sys.exit(0)

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
        print("\nCarga de datos completa.")
        pantallaInicio()
    
