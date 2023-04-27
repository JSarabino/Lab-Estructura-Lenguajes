from Estatus import Estatus

class Pedido:

    #Atributos
    __idPedido: int
    __fechaPedido: str
    __montoTotal: str
    __montoPagado: float
    __estatus: Estatus
    __idCliente: int
    __pagos = []
    __detalles = []

    #Constructor
    def __init__(self, idPedido, fechaPedido,montoTotal, montoPagado,estatus,idCliente):
        self.__idPedido = idPedido
        self.__fechaPedido = fechaPedido
        self.__montoTotal = montoTotal
        self.__montoPagado = montoPagado
        self.__estatus = estatus
        self.__idCliente = idCliente
    
    #Getters and Setters
    def get_IdPedido(self):
        return self.__idPedido

    def set_IdPedido(self, idPedido):
        self.__idPedido = idPedido
    
    def get_FechaPedido(self):
        return self.__fechaPedido

    def get_FechaPedido(self, fechaPedido):
        self.__fechaPedido = fechaPedido

    def get_MontoTotal(self):
        return self.__montoTotal

    def set_MontoTotal(self, montoTotal):
        self.__montoTotal =  montoTotal

    def get_MontoPagado(self):
        return self.__montoPagado

    def set_MontoPagado(self, montoPagado):
        self.__montoPagado = montoPagado
    
    def get_Estatus(self):
        return self.__estatus
    
    def set_Estatus(self, estatus):
        self.__estatus = estatus

    def get_IdCliente(self):
        return self.__idCliente

    def set_IdCliente(self, idCliente):
        self.__idCliente = idCliente
        
    def get_Pagos(self):
        return self.__pagos
    
    def set_Pagos(self, pago):
        self.__pagos.append(pago)
    
    def get_Detalles(self):
        return self.__detalles
    
    def set_Detalles(self, detalle):
        self.__detalles.append(detalle)

    def mostrarPedido(self):
        print(
            f"Id del pedido: {self.__idPedido}, Fecha pedido: {self.__fechaPedido}, Monto total: {self.__montoTotal}, Monto pagado: {self.__montoPagado}, Estatus: {self.__estatus}, Id cliente: {self.__idCliente}")
        #Datos de los detalles
        print("Detalles del pedido " + str(self.__idPedido) + ": "+ str(len(self.__detalles)))
        for i in self.__detalles:
            print(i.mostrarDetalle())