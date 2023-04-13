from GrupoInvestigacion import GrupoInvestiacion
from Persona import Persona
import sys

#Elegir opcion del menu principal
def opMenuPrincipal():
    while True:
        print("\nMenu Principal.")
        print("1. Crear Personas \n2. Crear grupos de investigacion \n3. Asignar miembros a un grupo de investigacion \n4. Consultas \n5. Salir")
        op = int(input("\nDigite la opcion a realizar: "))
        if op > 0 and op < 6:
            menuPrincipal(op)

#Menu Principal
def menuPrincipal(op):
    match op:
        case 1: 
            while True:
                cantP = int(input("\nDigite la cantidad de personas a crear: "))
                if cantP > 0:
                    crearPersonas(cantP)
                    
        case 2: 
            while True:
                cantG = int(input("\nDigite la cantidad de grupos a crear: "))
                if cantG > 0:
                    crearGrupos(cantG)

        case 3: asignarMiembros()
        case 4: 
            while True:
                print("\nMenu consultas.")
                print("1. Buscar director de un grupo de investigacion \n2. Miembros de un grupo de investigacion \n3. Verificar membresia a un grupo de investigacion \n4. Grupo de investigacion con mas miembros \n5. Atras")
                op = int(input("\nDigite la opcion a realizar: "))
                if op > 0 and op < 6:
                    menuConsultas(op)
        case 5: salir()

#Menu consultas
def menuConsultas(op):
    match op:
        case 1: buscarDirector()
        case 2: miembrosGrupo()
        case 3: verificarGrupo()
        case 4: mayorCantGrupo()
        case 5: opMenuPrincipal()

# A. Crear Personas
def crearPersonas(cantP):
    for i in range(cantP):
        #Pedir datos
        while True:
            id = int(input("\nDigite la identificacion: "))
            if id > 0:
                break    
        nombres = input("Digite los nombres: ")
        apellidos = input("Digite los apellidos: ")
        #Crear objeto Persona y agregar a la lista lsPersonas
        objPersona = Persona(id,nombres,apellidos)
        lsPersonas.append(objPersona)
    
    opMenuPrincipal()
    
# B. Crear Grupos de Investigación.
def crearGrupos(cantG):
    for i in range(cantG):
        #Pedir datos 
        nombre = input("\nDigite el nombre: ")
        ubicacion = input("Digite la ubicacion: ")
        director = asignarDirector()
        #Crear objeto Persona y agregar a la lista lsPersonas
        objGrupo = GrupoInvestiacion(nombre,ubicacion,director)
        lsGrupos.append(objGrupo)
    
    opMenuPrincipal()

def asignarDirector():
    while True:
        id = int(input("Digite la identificacion del director: "))
        if id > 0:
            break 
    director =  buscarPersona(id)

    if director == None:
        nombres = input("Digite los nombres del director: ")
        apellidos = input("Digite los apellidos del director: ")
        objPersona = Persona(id,nombres,apellidos)
        lsPersonas.append(objPersona)
        director = objPersona

    return director

def buscarPersona(id):
    persona = None
    for i in range(len(lsPersonas)):
        if lsPersonas[i].get_Identificacion() == id:
            persona = lsPersonas[i]
            break
    return persona

# C. Asignar miembros a un grupo de investigación.
def asignarMiembros():
    nombreG = input("\nDigite el nombre del grupo a agregar miembro: ")
    grupo = buscarGrupo(nombreG)

    if grupo != None:
        #POST: el grupo existe
        print("\nIngresar miembro a " + nombreG)
        id = int(input("Digite la identificacion miembro a agregar: "))
        nuevoMiembro =  buscarPersona(id)

        if nuevoMiembro != None:
            #POST: la persona existe

            if len(grupo.get_Miembros()) > 0:
                #POST: La cantidad de miembros en el grupo es mayor a 0
                pertenece = perteneceAGrupo(id,nombreG)

                if pertenece != False:
                    #POST: la persona no es parte de los miembros del grupo
                    for i in range(len(lsGrupos)):
                        if lsGrupos[i].get_Nombre() == nombreG:
                            lsGrupos[i].add_Miembro(nuevoMiembro)
                else:
                    print("\nLa persona ya pertenece al grupo.")

            else:
                for i in range(len(lsGrupos)):
                    if lsGrupos[i].get_Nombre() == nombreG:
                        lsGrupos[i].add_Miembro(nuevoMiembro)            
        else:
            print("\nLa persona no existe.")
            
    else:
        print("\nEl grupo no existe.")

def buscarGrupo(nombreG):
    grupo = None
    for i in range(len(lsGrupos)):
        if lsGrupos[i].get_Nombre() == nombreG:
            grupo = lsGrupos[i]
            break
    return grupo

def perteneceAGrupo(id, nombreG):
    pertenece = False
    persona = buscarPersona(id)
    grupo = buscarGrupo(nombreG)

    if persona != None and grupo != None:
        for i in range(len(grupo.get_Miembros())):
            if grupo.get_Miembros[i].get_Identificacion() == persona.get_Identificacion():
                pertenece = True
                break
    return pertenece

# D. Consultas:
# ¿Quién es el director de un grupo de investigación?
def buscarDirector():
    nombreG = input("\nDigite el nombre del grupo a buscar director: ")
    grupo = buscarGrupo(nombreG)

    if grupo != None:
        print("El director del grupo es: " + repr(grupo.get_Director))
    else:
        print("\nEl grupo no existe.")

# ¿Cuáles son los miembros de un grupo de investigación?
def miembrosGrupo():
    nombreG = input("\nDigite el nombre del grupo: ")
    grupo = buscarGrupo(nombreG)

    if grupo != None:
        print("\nLos miembros del grupo son: ")
        if len(grupo.get_Miembros()) > 0:
            lsMiembros = grupo.get_Miembros()
            for i in range(len(grupo.get_Miembros())):
                print(repr(lsMiembros[i]))
        else:
            print("El grupo no tiene miembros")
    else:
        print("\nEl grupo no existe.")

# ¿Verificar si una persona es miembro de un grupo de investigación?
def verificarGrupo():
    nombreG = input("\nDigite el nombre del grupo: ")
    grupo = buscarGrupo(nombreG)
    if grupo != None:
        #POST: el grupo existe
        if len(grupo.get_Miembros()) > 0:
            #POST: La cantidad de miembros en el grupo es mayor a 0
            print("Verificar persona en el grupo: " + nombreG)
            id = int(input("Digite la identificacion de la persona a verificar: "))
            verificarPersona =  buscarPersona(id)
            if verificarPersona != None:
                #POST: la persona existe
                pertenece = perteneceAGrupo(id,nombreG)
                if pertenece != False:
                    print("\nLa persona SI pertenece al grupo")
                else:
                    print("\nLa persona NO pertenece al grupo")                 
            else:
                print("\nLa persona no existe.")  
        else:
            print("\nLa persona no pertenece") 
    else:
        print("\nEl grupo no existe.")

# ¿Cuál es el grupo de investigación que tiene más miembros?
def mayorCantGrupo():
    if len(lsGrupos) > 0:
        mayor = len(lsGrupos[0].get_Miembros())
        grupoMayor = lsGrupos[0]
        for i in range(len(lsGrupos)-1):
            if mayor < len(lsGrupos[i+1].get_Miembros()):
                grupoMayor = lsGrupos[i+1]
        print("El grupo con mas miembros es: " + grupoMayor.get_Nombre())
    else:
        print("\nNo hay grupos")

# Salir del programa
def salir():
    print("\nHasta luego!")
    sys.exit(0)

# Main
if __name__ == '__main__':

    lsPersonas = []
    lsGrupos = []

    opMenuPrincipal()

    '''
    #Crear personas
    persona1 = Persona(111,"Mario","Piattini")
    persona2 = Persona(222,"Carlos Alberto","Cobos")

    print(repr(persona1))
    print(f"Persona1: {persona1}")

    grupo1 = GrupoInvestiacion("Alarcos","Ciudad real Espanya",persona1)
    grupo2 = GrupoInvestiacion("GTI","Popayan Cauca",persona2)

    print(repr(grupo1))
    print(f"Grupo1: {grupo1}")
    '''