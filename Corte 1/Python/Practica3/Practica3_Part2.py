#1. Realice un subprograma que permita imprimir todos sus componentes
def mostrarJugadores(Jugadores):
    print("----------------------------------------------------")
    print("\nInformacion de los jugadores")
    for clave, valores in Jugadores.items():
        for elemento in valores:
            print(clave,', ',elemento +',',valores[elemento], end=" ")
        print()
    print("\n----------------------------------------------------")

#Cree una función que permita encontrar cual es el jugador más alto. Se deberá mostrar: Nombre, equipo y nacionalidad.
def jugadorMasAlto(Jugadores):
    mayor = 0
    jugador = ""
    for i in Jugadores:
        if mayor < Jugadores[i]['Altura']:
            mayor = Jugadores[i]['Altura']
            jugador = Jugadores[i]
    
    print("\nEl jugador mas alto es: ")
    print(jugador['Nombre'])
    print(jugador['Club'])
    print(jugador['Nacionalidad'])

#2. Cree un diccionario de datos (dEstudiantes)

#Funcion para realizar la carga de datos como un diccionario normal
def cargarDatos(localizadorArchivo):
   try:
        with open(localizadorArchivo) as archivo:
            separador = ', '
            diccionario = {}
            for linea in archivo:
                linea = linea.rstrip("\n")  # Quitar salto de línea
                columnas = linea.split(separador)
                codigo = int(columnas[0])
                nombre = columnas[1]
                notas=[]
                notas.append(float(columnas[2]))
                notas.append(float(columnas[3]))
                notas.append(float(columnas[4]))
                diccionario [codigo]={#definicion del diccionario dentro de la lista
                    "codigo": codigo,
                    "nombre": nombre,
                    "notas": notas
                }
        return diccionario
   except IOError:
        mensaje = "Error!, el archivo no esta en "+ localizadorArchivo + ", o no existe."
        print(mensaje) 

#Cree una funcionalidad que permita mostrar el diccionario creado.
def mostrarEstudiantes(dEstudiantes):
    print("----------------------------------------------------")
    print("\nInformacion de los ",len(dEstudiantes)," estudiantes registrados")
    print("Codigo \t\tNombre \t\t\tNotas")
    for i in dEstudiantes:
            print(dEstudiantes[i]['codigo'],"\t\t",dEstudiantes[i]['nombre'],"\t\t",dEstudiantes[i]['notas'])

#Cree una funcionalidad que permita buscar un estudiante mediante el código. Se deberá mostrar toda la información.
def buscarEstudiante(dEstudiantes, cod):
    encontrado = False
    estudiante = ""
    for i in dEstudiantes:
        if dEstudiantes[i]['codigo'] == cod:
            encontrado = True
            estudiante = dEstudiantes[i]
    return encontrado, estudiante

def promEstudiante(dEstudiantes, cod):
    promedio = 0
    encontrado, estudiante = buscarEstudiante(dEstudiantes,cod)
    if encontrado != False:
        for i in estudiante['notas']:
            promedio += i
        promedio /= len(estudiante['notas'])
        print("\nEl promedio del " + str(estudiante['nombre']) + " es: " + str(promedio))
    else:
        print("\nEstudiante no encontrado.")

#Programa principal
if __name__ == '__main__':

    #Definimos el Diccionario jugadores
    Jugadores ={
    1001:{'Club':'Real Madrid','Nombre':"Karim Benzema",'Nacionalidad':"Francia",'Edad':34,'Altura':185},
    1002:{'Club':'Atlético de Madrid','Nombre':"Jan Oblak",'Nacionalidad':"Eslovenia",'Edad':29,'Altura':188},
    1003:{'Club':'Villareal FC','Nombre':"Parejo",'Nacionalidad':"España",'Edad':33,'Altura':182},
    1004:{'Club':'Sevilla FC','Nombre':"Fernando",'Nacionalidad':"Brasil",'Edad':35,'Altura':183}
    }
    #Mostrar los jugadores
    mostrarJugadores(Jugadores)
    
    #Jugador mas alto
    jugadorMasAlto(Jugadores)

    #Cargar estudiantes
    localizadorArchivo = "dEstudiantes.txt"
    dEstudiantes = {}
    dEstudiantes = cargarDatos(localizadorArchivo)
    mostrarEstudiantes(dEstudiantes)

    #Encontrar estudiante
    encontrado, estudiante = buscarEstudiante(dEstudiantes,1001)
    if encontrado != False:
        print("\nEstudiante encontrado:")
        print(estudiante)
    else:
        print("\nEstudiante no encontrado.")
    
    #Promedio de notas de un estudiante
    promEstudiante(dEstudiantes,1002)