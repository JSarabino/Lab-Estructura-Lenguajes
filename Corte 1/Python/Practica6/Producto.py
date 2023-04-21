from abc import ABC, abstractmethod

class Producto(ABC):
    #Atributos
    _idProducto: int
    _nombre: str
    _precio: float
    _descripcion: str
    _cantidad: int

    #Constructor
    def __init__(self, idProducto, nombre, precio, descripcion, cantidad):
        self._idProducto = idProducto
        self._nombre = nombre
        self._precio = precio
        self._descripcion = descripcion
        self._cantidad = cantidad
    
    #Getters and Setters
    def get_IdProducto(self):
        return self._idProducto

    def set_IdProducto(self, idProducto):
        self._idProducto = idProducto
    
    def get_Nombre(self):
        return self._nombre

    def set_Nombre(self, nombre):
        self._nombre = nombre

    def get_Precio(self):
        return self._precio

    def set_Precio(self, precio):
        self._precio = precio

    def get_Descripcion(self):
        return self._descripcion

    def set_Descripcion(self, descripcion):
        self._descripcion = descripcion
    
    def get_Cantidad(self):
        return self._cantidad
    
    def set_Cantidad(self, cantidad):
        self._cantidad = cantidad
    
    #Definir metodo abstracto
    @abstractmethod
    def mostrarProducto(self):
        pass