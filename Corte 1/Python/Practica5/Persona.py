class Persona:

    #Atributos
    __identificacion = int
    __nombres = str
    __apellidos = str
    
    #Constructor
    def __init__(self, identificacion, nombres, apellidos):
        self.__identificacion = identificacion
        self.__nombres = nombres
        self.__apellidos = apellidos
    
    #Getters and setters of class
    def get_Identificacion(self):
        return self.__identificacion
    def set_Identificacion(self, identificacion):
        self.__identificacion = identificacion
    
    def get_Nombres(self):
        return self.__nombres
    def set_Nombres(self, nombres):
        self.__nombres = nombres

    def get_Apellidos(self):
        return self.__apellidos
    def set_Apellidos(self, apellidos):
        self.__apellidos = apellidos

    def __repr__(self):
        i = self.__identificacion
        n = self.__nombres
        a = self.__apellidos

        return f"Identificacion: {i} Nombres: {n} y Apellidos: {a}"