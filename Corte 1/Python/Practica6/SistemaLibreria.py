from Persona import Persona
from Narrador import Narrador
from Autor import Autor
from Producto import Producto
from Libro import Libro
from AudioLibro import AudioLibro
from Periodico import Periodico

class SistemaLibreria:
    personas = []
    catalogoProductos = []

    # metodos adicionales
    def adicionarPersonas(self):
        autor1 = Autor(111, "Mario", "Piatini", "España")
        autor2 = Autor(222, "Oscar Felis", "Garcia", "España")
        autor3 = Autor(333, "Francisco", "Pino", "Colombia")
        narrador1 = Narrador(444, "Javier", "Fernandes")
        narrador1.set_Idioma("Ingles")
        narrador1.set_Idioma("Aleman")

        # adicionar los objetos a la lista de personas[]
        self.personas.append(autor1)
        self.personas.append(autor2)
        self.personas.append(autor3)
        self.personas.append(narrador1)

    def mostrarPersonas(self):
        p: Persona
        for p in self.personas:
            p.mostrarPersona()

    def personaPorTipo(self, tipo):
        # 1 es para autor y 2 para narrador
        if tipo == 1:
            for pA in self.personas:
                if isinstance(pA, Autor):
                    pA.mostrarPersona()
        elif tipo == 2:
            for pN in self.personas:
                if isinstance(pN, Narrador):
                    pN.mostrarPersona()
        else:
            print("Error!. El tipo persona no existe.")


# programa principal
if __name__ == "__main__":
    obj = SistemaLibreria()
    obj.adicionarPersonas()
    obj.mostrarPersonas()

    tipo = int(
        input("Consulta personas: \nDigite 1 para Autor, o 2 para Narrador.\n"))
    obj.personaPorTipo(tipo)
