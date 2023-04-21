from Libro import Libro
from Narrador import Narrador
class AudioLibro(Libro):
    #Atributos
    __idioma: str
    __duracion: int
    __narrador: Narrador

    #Constructor
    def __init__(self, idProducto, nombre, precio, descripcion, cantidad, ISBN, idioma, duracion, narrador):
        self._idProducto = idProducto
        self._nombre = nombre
        self._precio = precio
        self._descripcion = descripcion
        self._cantidad = cantidad
        self._ISBN = ISBN
        self.__idioma = idioma
        self.__duracion = duracion
        self.__narrador = narrador
    
    #Getters and Setters
    def get_Idioma(self):
        return self.__idioma
    
    def set_Idioma(self, idioma):
        self.__idioma = idioma
    
    def get_Duracion(self):
        return self.__duracion
    
    def set_Duracion(self, duracion):
        self.__duracion = duracion
    
    def get_Narrador(self):
        return self.__narrador
    
    def set_Narrador(self, narrador):
        self.__narrador = narrador
    
    #implementar el metodo abstracto
    def mostrarProducto(self):
        #Datos del Audio libro
        print(
            f"\nId del producto: {self._idProducto}, Nombre: {self._nombre}, Precio: {self._precio} \nDescripcion: {self._descripcion}, Cantidad: {self._cantidad}, ISBN: {self._ISBN}, \nIdioma: {self.__idioma}, Duracion: {self.__duracion}, Narrador: {self.__narrador}")