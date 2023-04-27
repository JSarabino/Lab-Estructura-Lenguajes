
class Pago:

    #Atributos
    __idPago: int
    __monto: float
    __idPedido: int

    #Constructor
    def __init__(self, idPago, monto, idPedido):
        self.__idPago = idPago
        self.__monto = monto
        self.__idPedido = idPedido

    #Getters and Setters
    def get_IdPago(self):
        return self.__idPago

    def set_IdPago(self, idPago):
        self.__idPago = idPago

    def get_Monto(self):
        return self.__monto

    def set_Monto(self, monto):
        self.__monto = monto

    def get_IdPedido(self):
        return self.__idPedido

    def set_IdPedido(self, idPedido):
        self.__idPedido = idPedido

    
    def mostrarPago(self):
        print(
            f"\nId pago: {self.__idPago}, Monto: {self.__monto}, Id pedido: {self.__idPedido}")