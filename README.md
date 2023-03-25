# Lab-Estructura-Lenguajes
## Trabajos hechos en el laboratorio de estructura de lenguajes

### Práctica 1 - Programación imperativa: 

El propósito de esta práctica es la utilización de un lenguaje de programación orientado a
soportar el paradigma imperativo. Para tal fin, haga uso de un lenguaje como C++ para crear
una Struct que permita el ingreso de N estudiantes, las cuales dispondrán de la siguiente
información: código, nombre, teléfono, edad. Finalmente, el programa deberá permitir hacer
las siguientes operaciones:

  1. Llenar la estructura de datos estudiante.
  2. Mostrar a todos los estudiantes registrados en la estructura.
  3. Validar si un estudiante se encuentra registrado en la estructura mediante el código.
  4. Consultar un estudiante mediante el código.
  5. Cúal (s) es el estudiante de mayor y menor edad de la estructura?.
  
Requerimientos
  * Use una struct llamada Estudiante.
  * Cree un vector de estructuras llamado vE con el número de estudiantes que serán ingresadas por un usuario.
  * Cree las funciones requeridas haciendo uso de funciones o procedimientos.
  * Puede realizar el programa en Visual Studio Code (VSC) o Sublime Text o DevC++. Esquema general de la Struct
  
Estudiante
```Python
  int codigo
  string nombre
  int telefono
  int edad
```
### Práctica 2 - Programación en Python:

  1. Cree en Python un programa que permita:
      - a. Implementar una función que determine si un número es par o impar.
      - b. Implementar una función que permita determinar cuál es el mayor de dos números enteros ingresados por un usuario.
      - c. Llenar y mostrar un vector de n elementos.
      - d. Crear un menú que permita realizar las siguientes funcionalidades respecto al punto c:
        - I. Encontrar el máximo elemento del vector.
        - II. Buscar un elemento en el vector y determinar cuál es su posición.
        - III. Encontrar la desviación estándar de una muestra de valores almacenados en un vector.
  
          En estadística, la desviación estándar es la medida de la dispersión de los valores respecto a la media (valor promedio) y viene calculada por la siguiente formula:

                    sqrt(∑(x − xm) ** 2 / n - 1)                 

           Donde x equivale a cada uno de los elementos del vector, xm la media o valor promedio del vector y n el número de elementos del vector.

  2. Cree en Python un programa que permita:
    a. Llenar y mostrar una NxM elementos.
    b. Encontrar la matriz transpuesta.
    Recuerde, la transpuesta de una matriz se obtiene a través de la conversión de cada una de las
    filas a las columnas.
  
### Práctica 3 - Programación en Python:
#### Parte I: Manejo de listas:
1. Cree una lista (listaProductos) a partir de un archivo denominado “producto.txt” que contiene la siguiente información:

    Ejemplo:
    ```
    1001, disco duro 1tb, 215000, 10
    1002, mouse inalambrico logitech, 42900, 5
    1003, Teclado Logitech K380, 159900, 3
    1004, Monitor Samsung Ips De 24 Full Hd, 663900, 2
    1005, cable hdmi 5 metros, 15000, 7
    ```
2. Cree una función que permita adicionar un producto a la lista.
3. Cree una función que permita modificar un producto de la lista. Por ejemplo: el nombre, o el precio o la cantidad.
4. Cree una función que permita eliminar un producto por medio del código.

#### Parte II: Manejo de Diccionarios:
1. Defina el siguiente diccionario y realice un subprograma que permita     imprimir todos sus componentes.
    ```Python
      Jugadores ={

      1001:{'Club':'Real Madrid','Nombre':"Karim Benzema",'Nacionalidad':"Francia",'Edad':34,'Altura':185},
      1002:{'Club':'Atlético de Madrid','Nombre':"Jan Oblak",'Nacionalidad':"Eslovenia",'Edad':29,'Altura':188},
      1003:{'Club':'Villareal FC','Nombre':"Parejo",'Nacionalidad':"España",'Edad':33,'Altura':182},
      1004:{'Club':'Sevilla FC','Nombre':"Fernando",'Nacionalidad':"Brasil",'Edad':35,'Altura':183}

      }
    ```
    Finalmente, cree una función que permita encontrar cual es el jugador más alto. Se deberá mostrar: Nombre, equipo y nacionalidad.

2. Cree un diccionario de datos (dEstudiantes) mediante un archivo que contiene la siguiente información:

    Ejemplo:
    ```
    1001, estudiante 1, 4.0, 3.5, 2.8
    1002, estudiante 2, 3.0, 2.5, 3.8
    1003, estudiante 3, 1.0, 3.5, 1.8
    1004, estudiante 4, 5.0, 4.5, 3.0
    ```
    * Cree una funcionalidad que permita mostrar el diccionario creado.
    * Cree una funcionalidad que permita buscar un estudiante mediante el código. Se deberá mostrar toda la información.
    * Cree una funcionalidad que permita calcular el promedio de las notas de un   estudiante mediante el código.
