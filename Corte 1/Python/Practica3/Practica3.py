# 1. Funcion que carga las lineas de un .txt cualquiera
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

# Funcion que carga los productos de producto.txt
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

# 2. Funcion que agrega un producto a la lista incluyendo al archivo producto.txt
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

# 3. Funcion que permite modificar un prodcuto de la lista
def modificarProducto(localizadorArchivo, op, filas):
    
    dato = input("Ingrese " + opcion(op) + " del producto: ")
    contenido = list()

    with open(localizadorArchivo, 'r+') as archivo:
        contenido = archivo.readlines()
        
        for fila in filas:
            columnas = contenido[fila-1].split(', ')
            columnas[op] = dato
            if op == 3:
                contenido[fila-1] = ', '.join(columnas) + '\n'
            else:
                contenido[fila-1] = ', '.join(columnas)
            
    with open(localizadorArchivo, 'w') as archivo:
        archivo.writelines(contenido)

    return True

# Funcion que comprueba que el producto existe y devuelve el numero de la fila
def buscarProducto(localizadorArchivo, codigo):
    separador = ', '
    contFilas = 0
    with open (localizadorArchivo, 'r') as archivo:
        for linea in archivo:
            linea = linea.rstrip("\n")
            columna = linea.split(separador)
            contFilas = contFilas + 1
            if codigo == int(columna[0]):
                return True, contFilas
        archivo.close()
    return False, contFilas

# Funcion que retorna el mensaje adecuado segun la opcion
def opcion(op):
    if op == 1:
        return "el nombre"
    elif op == 2:
        return " el precio"
    else:
        return "la cantidad"

# 4. Funcion que permite borrar un prodcuto por su codigo
def eliminarProducto(localizadorArchivo, filas):
    contenido = list()
    with open(localizadorArchivo, 'r+') as archivo:
        contenido = archivo.readlines()
        
        for fila in filas:
            columnas = contenido[fila-1].split(', ')
            if filas[0] == fila-1:
                contenido[fila-1] = ', '.join(columnas) + '\n'
            else: 
                contenido[fila-1] = ''
    with open(localizadorArchivo, 'w') as archivo:
        archivo.writelines(contenido)

    return True
        

# Funcion main
if __name__ == '__main__':
    
    # 1.
    localizadorArchivo = "Practica3/producto.txt"
    listaProductos = []
    listaProductos = cargaDatosEsp(localizadorArchivo)

    if not listaProductos:
        print("Lista vacia. Intente de nuevo")
    else:
        listaProductos = cargaDatosEsp(localizadorArchivo)
        print(listaProductos)
    
    # 2.
    addProducto(localizadorArchivo)
    listaProductos = cargaDatosEsp(localizadorArchivo)
    print(listaProductos)

    # 3.
    while True:
        codMod = int(input("\nDigite el codigo del producto a modificar: "))
        encontrado, fila = buscarProducto(localizadorArchivo, codMod)
        if encontrado == True:
            print("\nProducto a modificar:")
            print(listaProductos[fila-1])
            break
    
    while True:
        print("\n1. Cambiar nombre.")
        print("2. Cambiar precio.")
        print("3. Cambiar cantidad.\n")

        op = int(input("Ingrese la opcion: "))

        if op > 0 and op < 4:
            break
    #Indica las filas a modificar en el .txt
    filas = [fila]

    if modificarProducto(localizadorArchivo, op, filas) == True:
        listaProductos = cargaDatosEsp(localizadorArchivo)
        print("\nProducto modificado:")
        print(listaProductos[fila-1])
    
    # 4.
    productoEliminado = []
    while True:
        codBorrar = int(input("\nDigite el codigo del producto a borrar: "))
        encontrado, fila = buscarProducto(localizadorArchivo, codBorrar)
        if encontrado == True:
            productoEliminado = [listaProductos[fila-1]]
            break

    filas = [fila]

    if eliminarProducto(localizadorArchivo, filas) == True:
        print("\nProducto eliminado:")
        print(productoEliminado)