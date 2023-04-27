from Pago import Pago

class Efectivo(Pago):

    #Atributos
    __idPago: int
    __monto: float
    __idPedido: int

    #Constructor
    def __init__(self, idPago, monto, idPedido):
        self.__idPago = idPago
        self.__monto = monto
        self.__idPedido = idPedido