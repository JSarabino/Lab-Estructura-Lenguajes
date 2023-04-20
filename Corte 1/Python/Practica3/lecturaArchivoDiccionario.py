#funcion para realizar la carga de datos como un diccionario normal
def cargarDatos(localizadorArchivo):
   try:
        with open(localizadorArchivo) as archivo:
            separador = ', '
            diccionario = {}
            for linea in archivo:
                linea = linea.rstrip("\n")  # Quitar salto de línea
                columnas = linea.split(separador)
                codigo = int(columnas[0])
                nombre = columnas[1]
                notas=[]
                notas.append(float(columnas[2]))
                notas.append(float(columnas[3]))
                notas.append(float(columnas[4]))
                diccionario [codigo]={#definicion del diccionario dentro de la lista
                    "codigo": codigo,
                    "nombre": nombre,
                    "notas": notas
                }
        return diccionario
   except IOError:
        mensaje = "Error!, el archivo no esta en "+ localizadorArchivo + ", o no existe."
        print(mensaje) 

#funcion para realizar la carga de datos como un diccionario de tuplas
def cargarDatos(localizadorArchivo):
   try:
        with open(localizadorArchivo) as archivo:
            separador = ', '
            diccionario = {}
            for linea in archivo:
                linea = linea.rstrip("\n")  # Quitar salto de línea
                columnas = linea.split(separador)
                codigo = int(columnas[0])
                nombre = columnas[1]
                notas=[]
                notas.append(float(columnas[2]))
                notas.append(float(columnas[3]))
                notas.append(float(columnas[4]))
                diccionario [codigo]=[('nombre',nombre),('notas',notas)]
        archivo.close()
        return diccionario
   except IOError:
        mensaje = "Error!, el archivo no esta en "+ localizadorArchivo + ", o no existe."
        print(mensaje) 

#funcion para realizar la carga de datos y lectura como lista de diccionarios
def cargarDatos(localizadorArchivo):
   try:
        with open(localizadorArchivo,'r') as archivo:
            separador = ', '
            lista = []
            for linea in archivo:
                linea = linea.rstrip("\n")  # Quitar salto de línea
                columnas = linea.split(separador)
                codigo = int(columnas[0])
                nombre = columnas[1]
                notas=[]
                notas.append(float(columnas[2]))
                notas.append(float(columnas[3]))
                notas.append(float(columnas[4]))
                lista.append({#definicion del diccionario dentro de la lista
                    "codigo": codigo,
                    "nombre": nombre,
                    "notas": notas
                })       
        archivo.close()
        return lista
   except IOError:
        mensaje = "Error!, el archivo no esta en "+ localizadorArchivo + ", o no existe."
        print(mensaje) 