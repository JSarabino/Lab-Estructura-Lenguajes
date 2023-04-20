from Persona import Persona


class Narrador(Persona):
    __idiomas = []

    def __init__(self, identificacion, nombre, apellidos):
        self._identificacion = identificacion
        self._nombre = nombre
        self._apellidos = apellidos

    # Getters and Setters
    def get_Idiomas(self):
        return self.__idiomas

    def set_Idioma(self, idioma):
        self.__idiomas.append(idioma)

     # implementar el metodo abstracto
    def mostrarPersona(self):
        print(
            f"Identificacion: {self._identificacion}, Nombre: {self._nombre}, Apellidos: {self._apellidos}")
        print("Idiomas: ", len(self.__idiomas))

        for i in self.__idiomas:
            print(i)
