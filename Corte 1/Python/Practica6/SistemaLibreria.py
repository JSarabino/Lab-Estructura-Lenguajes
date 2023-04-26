from Persona import Persona
from Narrador import Narrador
from Autor import Autor
from Producto import Producto
from Libro import Libro
from AudioLibro import AudioLibro
from Periodico import Periodico
import sys

class SistemaLibreria:
    personas = []
    catalogoProductos = []

    # Metodos adicionales

    # Adicionar personas
    def adicionarPersonas(self, op):

        # Crear Productos para prueba
        libro1 = Libro(111,"Libro1",2300,"Descripcion libro1",23,"J123K13")
        libro2 = Libro(222,"Libro2",7300,"Descripcion libro2",12,"2AD3I60")

        audoLibro1 = AudioLibro(333,"audoLibro1",6700,"Descripcion audoLibro1",65,"dwd1d1",40)
        audoLibro2 = AudioLibro(444,"audoLibro2",15300,"Descripcion audoLibro2",18,"awd43t34y",20)

        periodico1 = Periodico(555,"periodico1",8500,"Descripcion periodico1",93,"12d312d","Cali","Ingles")
        periodico2 = Periodico(666,"periodico2",90300,"Descripcion periodico2",54,"J123Kh56","Popayan","Espaniol")

        # Adicionar los objetos a la lista de productos[]
        self.catalogoProductos.append(libro1)
        self.catalogoProductos.append(libro2)
        self.catalogoProductos.append(audoLibro1)
        self.catalogoProductos.append(audoLibro2)
        self.catalogoProductos.append(periodico1)
        self.catalogoProductos.append(periodico2)

        # Crear Personas
        autor1 = Autor(111, "Mario", "Piatini", "España")
        autor1.set_Libros(libro1)

        autor2 = Autor(222, "Oscar Felis", "Garcia", "España")
        autor2.set_Libros(libro2)

        autor3 = Autor(333, "Francisco", "Pino", "Colombia")
        autor3.set_Libros(libro1)

        narrador1 = Narrador(444, "Javier", "Fernandes")
        narrador1.set_Idioma("Ingles")
        narrador1.set_Idioma("Aleman")
        narrador1.set_AudioLibros(audoLibro1)
        narrador1.set_AudioLibros(audoLibro2)

        # Adicionar los objetos a la lista de personas[]
        self.personas.append(autor1)
        self.personas.append(autor2)
        self.personas.append(autor3)
        self.personas.append(narrador1)



        #Datos generales
        id = int(input("\nIngrese la identificacion: "))
        nombres = input("Ingrese los nombres: ")
        apellidos = input("Ingrese los apellidos: ")
        
        #Datos especificos
        if op == 1:
            pais = input("Ingrese el pais: ")
            autor = Autor(id,nombres,apellidos,pais)
            self.personas.append(autor)
        else:
            idioma = input("Ingrese el idioma: ")
            narrador = Narrador(id,nombres,apellidos)
            narrador.set_Idioma(idioma)
            self.personas.append(narrador)

    # Adicionar productos
    def adicionarProductos(self, op):

        #Datos generales
        id = int(input("\nIngrese el id del producto: "))
        nombre = input("Ingrese el nombre: ")
        precio = float(input("Ingrese el precio: "))
        descripcion = input("Ingrese una descripcion: ")
        cantidad = int(input("Ingrese la cantiodad: "))

        #Datos especificos
        if op == 1:
            isbn = input("Ingrese el ISBN: ")
            libro = Libro(id,nombre,precio,descripcion,cantidad,isbn)
            self.catalogoProductos.append(libro)
        elif op == 2:
            numPaginas = int(input("Ingrese el numero de paginas: "))
            ciudad = input("Ingrese la ciudad: ")
            idioma = input("Ingrese el idioma: ")
            periodico = Periodico(id,nombre,precio,descripcion,cantidad,numPaginas,ciudad,idioma)
            self.catalogoProductos.append(periodico)
        else:
            idioma = input("Ingrese el idioma: ")
            duracion = int(input("Ingrese la duracion: "))
            audioLibro = AudioLibro(id,nombre,precio,descripcion,cantidad,idioma,duracion)
            self.catalogoProductos.append(audioLibro)

    # Mostrar catalogo de productos
    def consultarCatalogoProductos(self):
        producto: Producto
        for producto in self.catalogoProductos:
            producto.mostrarProducto()

    # Consultar un producto
    def consultarProducto(self, id):
        producto = None
        for i in range(len(self.catalogoProductos)):
            if self.catalogoProductos[i].get_IdProducto() == id:
                producto = self.catalogoProductos[i]

        if producto != None:
            producto.mostrarProducto()
        else:
            print("\nProducto no encontrado.")

    # Consultar producto por tipo
    def consultarProductoPorTipo(self, tipo):
        # 1 es para libro, 2 para periodico y 3 para audio libro
        if tipo == 1:
            for pL in self.catalogoProductos:
                if isinstance(pL, Libro) and isinstance(pL, AudioLibro) == False:
                    pL.mostrarProducto()
        elif tipo == 2:
            for pP in self.catalogoProductos:
                if isinstance(pP, Periodico):
                    pP.mostrarProducto()
        elif tipo == 3:
            for pA in self.catalogoProductos:
                if isinstance(pA, AudioLibro):
                    pA.mostrarProducto()
        else:
            print("Error!. El tipo de producto no existe.")

    # Consultar libro por autor
    def librosPorAutor(self, ident):
        autor = None
        for i in range(len(self.personas)):
            if self.personas[i].get_Identificacion() == ident:
                autor = self.personas[i]
                break
        
        #Datos de los libros
        print("Libros: ", len(autor.get_Libros()))
        for i in autor.get_Libros():
            print(i.get_Nombre())

    # Consultar audio libro por narrador
    def audioLibrosPorNarrador(self, ident):
        narrador = None
        for i in range(len(self.personas)):
            if self.personas[i].get_Identificacion() == ident:
                narrador = self.personas[i]
                break

        #Datos de los audio libros
        print("Libros: ", len(narrador.get_AudioLibros()))
        for i in narrador.get_AudioLibros():
            print(i.get_Nombre())

    ##OTROS
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

    

# Elegir opcion del menu principal
def opMenuPrincipal():
    obj = SistemaLibreria()
    while True:
        print("\nMenu Principal.")
        print("1. Crear Autor/Narrador. \n2. Crear Libro/Periodico/Audio libro. \n3. Consultar catalogo de productos. \n4. Consultar producto. \n5. Consultar producto por tipo. \n6. Consultar libro por autor. \n7. Consultar audio libro por narrador. \n8. Salir")
        op = int(input("\nDigite la opcion a realizar: "))
        if op > 0 and op < 9:
            menuPrincipal(op,obj)

# Menu Principal
def menuPrincipal(op,obj):
    match op:
        case 1: 
            while True:
                print("\nMenu crear Autor/Narrador.")
                print("1. Crear autor. \n2. Crear narrador. \n3. Atras")
                op = int(input("\nDigite la opcion a realizar: "))
                if op > 0 and op < 4:
                    menuCrearPersona(op,obj)     
        case 2: 
            while True:
                print("\nMenu crear Libro/Periodico/Audio libro.")
                print("1. Crear libro. \n2. Crear periodico. \n3. Crear audio libro. \n4. Atras")
                op = int(input("\nDigite la opcion a realizar: "))
                if op > 0 and op < 5:
                    menuCrearProducto(op,obj)  

        case 3: obj.consultarCatalogoProductos()
        case 4: 
            id = int(input("\nIngrese el id del producto: "))
            obj.consultarProducto(id)
        case 5: 
            tipo = int(input("Consulta producto: \nDigite 1 para Libro, 2 para Periodico o 3 para Audio libro.\n"))
            obj.consultarProductoPorTipo(tipo)
        case 6: 
            ident = int(input("Ingrese la identificacion del autor: "))
            obj.librosPorAutor(ident)
        case 7: 
            ident = int(input("Ingrese la identificacion del narrador: "))
            obj.audioLibrosPorNarrador(ident)
        case 8: salir()

# Menu crear Autor/Narrador
def menuCrearPersona(op,obj):
    match op:
        case 1: obj.adicionarPersonas(op)
        case 2: obj.adicionarPersonas(op)
        case 3: opMenuPrincipal()

# Menu crear Libro/Periodico/Audio libro
def menuCrearProducto(op,obj):
    match op:
        case 1: obj.adicionarProductos(op)
        case 2: obj.adicionarProductos(op)
        case 3: obj.adicionarProductos(op)
        case 4: opMenuPrincipal()

# Salir del programa
def salir():
    print("\nHasta luego!")
    sys.exit(0)

# Programa principal
if __name__ == "__main__":
    opMenuPrincipal()
    