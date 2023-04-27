from Pedido import Pedido
from Producto import Producto

class DetallePedido:

    #Atributos
    __cantidad: int
    __pedido: Pedido
    __producto: Producto

    #Constructor
    def __init__(self, cantidad, pedido, producto):
        self.__cantidad = cantidad
        self.__pedido = pedido
        self.__producto = producto
    
    #Getters and Setters
    def get_Cantidad(self):
        return self.__cantidad
    
    def set_Cantidad(self, cantidad):
        self.__cantidad = cantidad

    def get_Pedido(self):
        return self.__pedido
    
    def set_Pedido(self, pedido):
        self.__pedido = pedido

    def get_Producto(self):
        return self.__producto
    
    def set_Producto(self, producto):
        self.__producto = producto

    def get_montoDetalle(self):
        return self.__cantidad * self.__producto.get_Precio()
    
    def mostrarDetalle(self):
        print(
            f"Cantidad: {self.__cantidad}, Total detalle: {self.get_montoDetalle()}, pedido id: {self.__pedido.get_IdPedido()}")