from abc import ABC, abstractmethod

class Persona(ABC):
    #Atributos
    _identificacion: int
    _nombre: str
    _apellidos: str

    #Constructor
    def __init__(self, identificacion, nombre, apellidos):
        self._identificacion = identificacion
        self._nombre = nombre
        self._apellidos = apellidos

    #Getters and Setters
    def get_Identificacion(self):
        return self._identificacion

    def set_Identificacion(self, identificacion):
        self._identificacion = identificacion

    def get_Nombre(self):
        return self._nombre

    def set_Nombre(self, nombre):
        self._nombre = nombre

    def get_Apellidos(self):
        return self._nombre

    def set_Apellidos(self, apellidos):
        self._apellidos = apellidos

    #Definir metodo abstracto
    @abstractmethod
    def mostrarPersona(self):
        pass