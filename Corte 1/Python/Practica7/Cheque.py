from Pago import Pago

class Cheque(Pago):

    #Atributos
    __entidad: str
    __titular: str
    __chequeNro: str

    #Constructor
    def __init__(self, entidad, titular, chequeNro):
        self.__entidad = entidad
        self.__titular = titular
        self.__chequeNro = chequeNro

    #Getters and Setters
    def get_Entidad(self):
        return self.__entidad

    def set_Entidad(self, entidad):
        self.__entidad = entidad

    def get_Titular(self):
        return self.__titular

    def set_Titular(self, titular):
        self.__titular = titular

    def get_ChequeNro(self):
        return self.__chequeNro

    def set_ChequeNro(self, chequeNro):
        self.__chequeNro = chequeNro

    def mostrarCheque(self):
        print(
            f"\Entidad: {self.__entidad}, Titular: {self.__titular}, ChequeNro: {self.__chequeNro}")