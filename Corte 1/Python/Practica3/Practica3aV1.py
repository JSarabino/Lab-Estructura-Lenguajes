#lectura general de un archivo e ingresarlo en una lista
def cargarDatosLG(localizadorArchivo):
    try:
        listado_producto = []
        producto = ()
        with open(localizadorArchivo, 'r') as archivo:
            for linea in archivo:
                producto = linea.split(', ',4)
                #leer toda la linea y asignarla a producto
                producto = list(map(lambda l:l.rstrip('\n'),producto))#rstrip elimina los espacios en blanco
                listado_producto.append(producto)
        archivo.close()
        return listado_producto
    except IOError:
        mensaje = "Error!, el archivo no esta en "+ localizadorArchivo + ", o no existe."
        print(mensaje)

#lectura general de un archivo especificando cada una de las columna e ingresarlas en una lista        
def cargarDatosLE(localizadorArchivo):
    try:
        separador = ', '
        listado_producto = []
        with open(localizadorArchivo, 'r') as archivo:
            for linea in archivo:
                linea = linea.rstrip("\n")  # Quitar salto de línea
                columnas = linea.split(separador)
                codigo = int(columnas[0])
                nombre = columnas[1]
                precio = float(columnas[2])
                cantidad = int(columnas[3])
                listado_producto.append([codigo,nombre,precio,cantidad])
        archivo.close()
        return listado_producto
    except IOError:
        mensaje = "Error!, el archivo no esta en "+ localizadorArchivo + ", o no existe."
        print(mensaje)
def agregarProductos(listaProductos):
    print("Agregar productos a la lista:")
    print("Digite codigo del producto")
    cod = int(input())
    print("Digite nombre del producto")
    nombre = input()
    print("Digite precio del producto")
    precio = float(input())
    print("Digite la cantidad del producto")
    cantidad = int(input())
    listaProductos.append([cod,nombre,precio,cantidad])

#programa principal
if __name__ == '__main__':        
    localizadorArchivo="Practica3/productos.txt"
    listaProductos =[]
    listaProductos = cargarDatosLG(localizadorArchivo)
    if not listaProductos:
        print("Intente de nuevo.")
    else:
        print(listaProductos)
    agregarProductos(listaProductos)
    print(listaProductos)
#ayudas
#https://j2logo.com/python/tutorial/tipo-list-python/#list-update