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