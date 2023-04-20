def mostrarJugadores(Jugadores):
    print("----------------------------------------------------")
    print("\nInformacion de los jugadores")
    for clave, valores in Jugadores.items():
        for elemento in valores:
            print(clave,', ',elemento +',',valores[elemento], end=" ")
        print()
    print("\n----------------------------------------------------")

#funcion para realizar la carga de datos como un diccionario normal
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

#mostrar el diccionario
def mostrar(dEstudiantes):
    print("----------------------------------------------------")
    print("\nInformacion de los estudiantes",len(dEstudiantes)," registrados")
    print("Codigo \t\tNombre \tNotas")
    for i in dEstudiantes:
            print(dEstudiantes[i]['codigo'],"\t\t",dEstudiantes[i]['nombre'],"\t\t",dEstudiantes[i]['notas'])

def mostrarNotasEstudiante(dEstudiantes, codigo):
    for cod, infoEst in dEstudiantes.items():
        if cod == codigo:
            codigo = infoEst['codigo']
            nombre = infoEst['nombre']
            notas = infoEst['notas']
            break
    print(f"Codigo: {codigo}, Nombre: {nombre}, notas: {notas}")

#programa principal
if __name__ == "__main__":
   #definir el diccionario
   Jugadores ={
    1001:{'Club':'Real Madrid','Nombre':"Karim Benzema",'Nacionalidad':"Francia",'Edad':34,'Altura':185}, 
    1002:{'Club':'Atlético de Madrid','Nombre':"Jan Oblak",'Nacionalidad':"Eslovenia",'Edad':29,'Altura':188}, 
    1003:{'Club':'Villareal FC','Nombre':"Parejo",'Nacionalidad':"España",'Edad':33,'Altura':182},
    1004:{'Club':'Sevilla FC','Nombre':"Fernando",'Nacionalidad':"Brasil",'Edad':35,'Altura':183},
    }
   #mostrar el diccionario
   mostrarJugadores(Jugadores)
   
   print("Practica 5")
   localizadorArchivo="Practica3/datos.txt"
   dEstudiantes = {}
   dEstudiantes = cargarDatos(localizadorArchivo)
   print(dEstudiantes)
   mostrar(dEstudiantes)
   mostrarNotasEstudiante(dEstudiantes,1002)
   
