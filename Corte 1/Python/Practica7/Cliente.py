
class Cliente:

    #Atributos
    __ident: int
    __nombreCompleto: str
    __direccion: str
    __pedidos = []

    #Constructor
    def __init__(self, ident, nombreCompleto, direccion):
        self.__ident = ident
        self.__nombreCompleto = nombreCompleto
        self.__direccion = direccion

    #Getters and Setters
    def get_Identificacion(self):
        return self.__ident

    def set_Identificacion(self, ident):
        self.__ident = ident

    def get_NombreCompleto(self):
        return self.__nombreCompleto

    def set_NombreCompleto(self, nombreCompleto):
        self.__nombreCompleto = nombreCompleto

    def get_Direccion(self):
        return self.__direccion

    def set_Direccion(self, direccion):
        self.__direccion = direccion

    def get_Pedidos(self):
        return self.__pedidos
    
    def set_Pedidos(self, pedido):
        self.__pedidos.append(pedido)

    def mostrarCliente(self):
        print(
            f"\nIdentificacion: {self.__ident}, Nombre completo: {self.__nombreCompleto}, Direccion: {self.__direccion}")