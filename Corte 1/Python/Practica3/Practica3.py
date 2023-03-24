def cargarDatosLG(localizadorArchivo):
    try:
        listado_productos = []
        producto = ()
        with open (localizadorArchivo, 'r') as archivo:
            for linea in archivo:
                producto = linea.split(', ',4)
                producto = list(map(lambda l:l.rstrip('\n'), producto))
                listado_productos.append(producto)
        archivo.close()
        return listado_productos
    except IOError:
        mensaje = "Error!, el archivo no esta en " + localizadorArchivo + " o no existe."
        print(mensaje)

def cargaDatosEsp(localizadorArchivo):
    try:
        separador = ', '
        listado_productos = []
        with open (localizadorArchivo, 'r') as archivo:
            for linea in archivo:
                linea = linea.rstrip("\n")
                columna = linea.split(separador)
                codigo = int(columna[0])
                nombre = columna[1]
                precio = float(columna[2])
                cantidad = int(columna[3])
                listado_productos.append([codigo,nombre,precio,cantidad])
        archivo.close()

        return listado_productos
    except IOError:
        mensaje = "Error!, el archivo no esta en " + localizadorArchivo + " o no existe."
        print(mensaje)

def addProducto(localizadorArchivo):
    print("\n---------Ingresar producto---------\n")
    codigo = int(input("Ingrese el codigo: "))
    nombre = input("Ingrese el nombre: ")
    precio = int(input("Ingrese el precio: "))
    cantidad = int(input("Ingrese la cantidad: "))

    #listaProductos.append([codigo,nombre,precio,cantidad]) //Agrega el producto a la impresion, no al archivo

    #Agregando el producto al archivo
    #Creamos el formato que tienen los productos en el archivo
    linea = "\n" + str(codigo) + ", " + str(nombre) + ", " + str(precio) + ", " + str(cantidad)
    #Abrimos el archivo en modo append(a) para agregar una linea al final del contenido existente
    archivo = open (localizadorArchivo, 'a')  
    #Llamamos al metodo write pasando la linea con el formato deseado  
    archivo.write(linea)
    archivo.close()


if __name__ == '__main__':
    localizadorArchivo = "Practica3/producto.txt"
    listaProductos = []
    listaProductos = cargaDatosEsp(localizadorArchivo)

    if not listaProductos:
        print("Lista vacia. Intente de nuevo")
    else:
        listaProductos = cargaDatosEsp(localizadorArchivo)
        print(listaProductos)
    
    addProducto(localizadorArchivo)
    print(listaProductos)
    