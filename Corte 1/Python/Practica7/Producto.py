 
class Producto:

    #Atributos
    __idProducto: int
    __nombre: str
    __marca: str
    __precio: float
    __cantidad: int

    #Constructor
    def __init__(self, idProducto, nombre,marca, precio, cantidad):
        self.__idProducto = idProducto
        self.__nombre = nombre
        self.__marca = marca
        self.__precio = precio
        self.__cantidad = cantidad
    
    #Getters and Setters
    def get_IdProducto(self):
        return self.__idProducto

    def set_IdProducto(self, idProducto):
        self.__idProducto = idProducto
    
    def get_Nombre(self):
        return self.__nombre

    def set_Nombre(self, nombre):
        self.__nombre = nombre

    def get_Marca(self):
        return self.__marca

    def set_Marca(self, marca):
        self.__marca = marca

    def get_Precio(self):
        return self.__precio

    def set_Precio(self, precio):
        self.__precio = precio
    
    def get_Cantidad(self):
        return self.__cantidad
    
    def set_Cantidad(self, cantidad):
        self.__cantidad = cantidad
    
    def mostrarProducto(self):
        print(
            f"\nId del producto: {self.__idProducto}, Nombre: {self.__nombre}, Marca: {self.__marca}, Precio: {self.__precio}, Cantidad: {self.__cantidad}")