from Producto import Producto

class Libro(Producto):
    #Atributos
    _ISBN: str
    __autores = []

    #Constructor
    def __init__(self, idProducto, nombre, precio, descripcion, cantidad, ISBN):
        self._idProducto = idProducto
        self._nombre = nombre
        self._precio = precio
        self._descripcion = descripcion
        self._cantidad = cantidad
        self._ISBN = ISBN
    
    #Getters and Setters
    def get_ISBN(self):
        return self._ISBN
    
    def set_ISBN(self, ISBN):
        self._ISBN = ISBN
    
    def get_Autores(self):
        return self.__autores
    
    def set_Autores(self, autor):
        self.__autores.append(autor)
    
    #implementar el metodo abstracto
    def mostrarProducto(self):
        #Datos del Libro
        print(
            f"\nId del producto: {self._idProducto}, Nombre: {self._nombre}, Precio: {self._precio}, Descripcion: {self._descripcion}, Cantidad: {self._cantidad}, ISBN: {self._ISBN}")
        #Datos de autores
        print("Autores: ", len(self.__autores))
        for i in self.__autores:
            print(i)