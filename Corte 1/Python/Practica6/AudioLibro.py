from Libro import Libro
from Narrador import Narrador
class AudioLibro(Libro):
    #Atributos
    __idioma: str
    __duracion: int

    #Constructor
    def __init__(self, idProducto, nombre, precio, descripcion, cantidad, idioma, duracion):
        self._idProducto = idProducto
        self._nombre = nombre
        self._precio = precio
        self._descripcion = descripcion
        self._cantidad = cantidad
        self.__idioma = idioma
        self.__duracion = duracion
    
    #Getters and Setters
    def get_Idioma(self):
        return self.__idioma
    
    def set_Idioma(self, idioma):
        self.__idioma = idioma
    
    def get_Duracion(self):
        return self.__duracion
    
    def set_Duracion(self, duracion):
        self.__duracion = duracion
    
    #implementar el metodo abstracto
    def mostrarProducto(self):
        #Datos del Audio libro
        print(
            f"\nId del producto: {self._idProducto}, Nombre: {self._nombre}, Precio: {self._precio} \nDescripcion: {self._descripcion}, Cantidad: {self._cantidad}, \nIdioma: {self.__idioma}, Duracion: {self.__duracion}")