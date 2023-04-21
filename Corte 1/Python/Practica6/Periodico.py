from Producto import Producto

class Periodico(Producto):
    #Atributos
    __numeroPaginas: int
    __ciudad: str
    __idioma: str

    #Constructor
    def __init__(self, idProducto, nombre, precio, descripcion, cantidad, numeroPaginas, ciudad, idioma):
        self._idProducto = idProducto
        self._nombre = nombre
        self._precio = precio
        self._descripcion = descripcion
        self._cantidad = cantidad
        self.__numeroPaginas = numeroPaginas
        self.__ciudad = ciudad
        self.__idioma = idioma
    
    #Getters and Setters
    def get_NumeroPaginas(self):
        return self.__numeroPaginas
    
    def set_NumeroPaginas(self, numeroPaginas):
        self.__numeroPaginas = numeroPaginas
    
    def get_Ciudad(self):
        return self.__ciudad
    
    def set_Ciudad(self, ciudad):
        self.__ciudad = ciudad
    
    def get_Idioma(self):
        return self.__idioma
    
    def set_Idioma(self, idioma):
        self.__idioma = idioma

    #implementar el metodo abstracto
    def mostrarProducto(self):
        #Datos del Audio libro
        print(
            f"\nId del producto: {self._idProducto}, Nombre: {self._nombre}, Precio: {self._precio} \nDescripcion: {self._descripcion}, Cantidad: {self._cantidad}, Numero de paginas: {self.__numeroPaginas}, \nCiudad: {self.__ciudad}, Idioma: {self.__idioma}")