from Persona import Persona


class Autor(Persona):
    __pais: set
    __Libros = []

    def __init__(self, identificacion, nombre, apellidos, pais):
        self._identificacion = identificacion
        self._nombre = nombre
        self._apellidos = apellidos
        self.__pais = pais

    # Getters and Setters
    def get_Pais(self):
        return self.__pais

    def set_Pais(self, pais):
        self.__pais = pais

    # implementar el metodo abstracto
    def mostrarPersona(self):
        print(
            f"Identificacion: {self._identificacion}, Nombre: {self._nombre}, Apellidos: {self._apellidos}")