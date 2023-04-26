from Persona import Persona

class Narrador(Persona):
    #Atributos
    __idiomas = []
    __audioLibros = []

    #Constructor
    def __init__(self, identificacion, nombre, apellidos):
        self._identificacion = identificacion
        self._nombre = nombre
        self._apellidos = apellidos

    # Getters and Setters
    def get_Idiomas(self):
        return self.__idiomas

    def set_Idioma(self, idioma):
        self.__idiomas.append(idioma)

    def get_AudioLibros(self):
        return self.__audioLibros

    def set_AudioLibros(self, audioLibro):
        self.__audioLibros.append(audioLibro)

     #implementar el metodo abstracto
    def mostrarPersona(self):
        #Datos de persona
        print(
            f"\nIdentificacion: {self._identificacion}, Nombre: {self._nombre}, Apellidos: {self._apellidos}")
        #Datos de los idiomas
        print("Idiomas: ", len(self.__idiomas))
        for i in self.__idiomas:
            print(i)