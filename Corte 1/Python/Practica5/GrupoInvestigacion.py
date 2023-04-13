from Persona import Persona
class GrupoInvestiacion:

    #Atributos
    # _atr1: int #Atributo entero de tipo protected
    # _atr2: float #Atributo float de tipo publico

    __nombre = str #Atributo nombre de tipo String y privado
    __ubicacion = str 
    __director = Persona
    __miembros = []

    #Constructor
    def __init__(self, nombre, ubicacion, director):
        self.__nombre = nombre
        self.__ubicacion = ubicacion
        self.__director = director

    #Getters and setters of class
    def get_Nombre(self):
        return self.__nombre
    def set_Nombre(self, nombre):
        self.__nombre = nombre

    def get_Ubicacion(self):
        return self.__ubicacion
    def set_Ubicacion(self, ubicacion):
        self.__ubicacion = ubicacion
    
    def get_Director(self):
        return self.__director
    def set_Director(self, director):
        self.__director = director

    def get_Miembros(self):
        return self.__miembros
    def add_Miembro(self, objPersona):
        self.__miembros.append(objPersona)
    
    def __repr__(self):
        n = self.__nombre
        u = self.__ubicacion
        d = self.__director.get_Nombres() + " " + self.__director.get_Apellidos()

        return f"Nombre grupo: {n} Ubicacion: {u} Director: {d}"
