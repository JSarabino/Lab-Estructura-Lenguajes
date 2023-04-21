from Persona import Persona

class Autor(Persona):
    #Atributos
    __pais: str
    __libros = []

    #Constructor
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
    
    def get_Libros(self):
        return self.__libros

    def set_Libros(self, libro):
        self.__libros.append(libro)

    # implementar el metodo abstracto
    def mostrarPersona(self):
        print(
            f"\nIdentificacion: {self._identificacion}, Nombre: {self._nombre}, Apellidos: {self._apellidos}, Pais: {self.__pais}")
        #Datos de los libros
        print("Libros: ", len(self.__libros))
        for i in self.__libros:
            print(i)