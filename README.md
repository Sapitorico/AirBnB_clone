<div><h1 align="center">AirBnB clone</h1> <!-- titulo -->

El objetivo del proyecto es desplegar en tu servidor una copia simple del sitio web de AirBnB.
La primera parte de este proyecto es crear un intérprete de comandos para manipular datos sin una interfaz visual, como en un Shell (perfecto para desarrollo y depuración)
</div>

<h2 align="center">The console</h2>

## Primer paso

Escribir un intérprete de comandos para gestionar tus objetos AirBnB.
Cada tarea está vinculada y te ayudará a: poner en marcha una clase padre que se encargue de la inicialización, serialización y deserialización de tus futuras instancias crear un flujo simple de serialización/deserialización: Diccionario de instancias Archivo de cadenas JSON crear todas las clases utilizadas para AirBnB que heredan de BaseModel crear el primer motor de almacenamiento abstracto del proyecto: Almacenamiento de archivos.
Segundo paso: Escribir un comando de consola para manipular los objetos de tu aplicación.
Cada tarea está vinculada y te ayudará a: crear un comando de consola para manipular tus objetos de la aplicación crear los métodos de creación, actualización y destrucción de los objetos de tu aplicación crear los métodos de consulta de tus objetos de tu aplicación

-----

<table align="center"> <!-- tabla de clases -->

<tr> <!-- columnas de la tabla -->

<th>Class</th>
<th>Description</th>
<th>Tests Files</th>

</tr>

<tr> <!-- fila 1  -->

<td><a href="">BaseModel</a></td> <!-- Class columna 1-->

<td> <!-- description -->

<details>
<summary><h2>BaseModel</h2></summary>

Es la clase base de todos los modelos de AirBnB. Esta clase es la encargada de manejar la serialización/deserialización de los atributos de los otros modelos, y de guardar en un archivo JSON todos los objetos instanciados. También es la clase base de todos los otros modelos de AirBnB, por lo que hereda de ella.

<h3>Modulos</h3>

* uuid:
    El módulo uuid en Python proporciona objetos UUID inmutables (la clase UUID) y las funciones uuid1(), uuid3(), uuid4(), uuid5() para generar identificadores universalmente únicos. Los valores de UUID versión 1 se calculan utilizando la dirección MAC((MAC address) es un identificador único asignado a un controlador de interfaz de red (NIC) para su uso como dirección de red) del host, mientras que la versión 4 usa pseudo-random number generators para generar UUIDs. El módulo también ofrece una herramienta para acortar los UUIDs para su uso en URLs

* datetime:
    El módulo datetime en Python proporciona clases para manipular fechas y horas, permitiendo operaciones aritméticas con fechas y horas. Se puede crear un datetime manualmente pasando los parámetros (year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None). Para trabajar con fechas en Python se debe importar el módulo datetime que incorpora los tipos de datos date, time y datetime para representar fechas y horas.

* storage:
    La variable storage proporciona las funcionalidades de almacenamiento y recuperación de datos. Se utiliza la función new() del módulo storage para registrar una nueva instancia de clase en la aplicación. Además, el método save() utiliza el módulo storage para guardar los cambios en la instancia

</details>
</td>

<td><a href="">test_base_model</a></td>



</tr> <!-- fin de fila 1-->

<td><a href="">FileStorage</a></td>


<td>

<details>
<summary><h2>FileStorage</h2></summary>

FileStorage es una clase que se utiliza para manejar el almacenamiento persistente de objetos en una aplicación web. Se enfoca en el almacenamiento de archivos y se utiliza para separar la gestión de almacenamiento de la lógica del modelo, lo que permite que los modelos sean modulares e independientes. Al utilizar atributos de clase en lugar de atributos de instancia, se proporciona una descripción clara y un valor predeterminado de cualquier atributo, lo que permite un comportamiento consistente del modelo en cualquier sistema de almacenamiento utilizado. En resumen, FileStorage es una implementación de un sistema de almacenamiento en archivo utilizando el formato JSON para almacenar información sobre instancias de clases.


<h3>Modulos</h3>

* json:
    proporciona una forma de codificar y decodificar datos JSON. Se utiliza para convertir objetos Python en una representación serializada que puede almacenarse en un archivo o transmitirse a través de la red. El operador módulo (%) en Python se utiliza para obtener el resto de una división.

* os.path:
    en Python se utiliza para diferentes propósitos, tales como la fusión, la normalización y la recuperación de los nombres de ruta en Python.

</details>
</td>
<td><a href="">test file_storage</a></td>


<tr>

<td><a href="">Console</a></td>

<td>
<details>
<summary><h2>Console</h2></summary>

La consola , HBNBCommand, es un intérprete de comandos que permite al usuario crear, actualizar, eliminar y buscar objetos utilizando comandos específicos. En otras palabras, esta consola es una interfaz de línea de comandos que interactúa con objetos del programa.

<h3>Modulos</h3>

El módulo cmd es una biblioteca estándar de Python que proporciona una clase base para crear consolas interactivas. Este módulo facilita la definición de comandos personalizados, la administración de argumentos y la personalización de la apariencia de la consola. Es una herramienta útil para crear interfaces de línea de comandos interactivas en Python.

<h3>commands:</h3>

## create:
    Crea una nueva instancia, la guarda en un archivo JSON y muestra su id.

## show:
    Muestra la representación en cadena de una instancia basada en el nombre de la clase y el id.

## destroy:
    Elimina una instancia basada en el nombre de la clase y el id (guarda el cambio en el archivo JSON)

## all:
    Muestra la representación en cadena de todas las instancias basadas o no en el nombre de la clase

## update:
    Actualiza una instancia basada en el nombre de la clase y el id agregando o actualizando un atributo (guarda el cambio en el archivo JSON). Solo se puede actualizar un atributo a la vez. Se puede asumir que el nombre del atributo es válido (existe para este modelo) y que el valor del atributo se convierte al tipo de atributo adecuado.

</details>

<td><a href="">tests</a></a></td>

</td>

</tr>  <!-- fin de la fila 3 -->

<tr>
<td>wqewqe</td>
</tr>

</table>



-----


<details>
<summary><h2 align="center">Recursos</h2></summary>

# *args and **kwargs in python explained

En Python, "args" y "kwargs" son dos parámetros especiales que se pueden utilizar en las definiciones de las funciones para recibir argumentos variables.

"Args" es un parámetro que permite a una función recibir un número variable de argumentos no nombrados. Esto significa que se puede pasar cualquier cantidad de argumentos a la función y Python los empacará todos en una tupla. Veamos un ejemplo:

```py
def my_function(*args):
    for arg in args:
        print(arg)

my_function(1, 2, 3)
```

En este ejemplo, definimos una función llamada my_function con un parámetro *args. Luego llamamos a la función con tres argumentos: 1, 2 y 3. Al imprimir los valores de args en el cuerpo de la función, obtenemos:

```
1
2
3
```

Esto significa que Python empacó los argumentos en una tupla y los pasó a la función.

"Kwargs" es un parámetro que permite a una función recibir un número variable de argumentos nombrados. Esto significa que se puede pasar cualquier cantidad de argumentos con un nombre específico a la función y Python los empacará en un diccionario. Veamos un ejemplo:

```py
def my_function(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

my_function(name='Alice', age=30, city='New York')
```

En este ejemplo, definimos una función llamada my_function con un parámetro **kwargs. Luego llamamos a la función con tres argumentos nombrados: name, age y city. Al imprimir los valores de kwargs en el cuerpo de la función, obtenemos:

```py
name Alice
age 30
city New York
```

Esto significa que Python empacó los argumentos nombrados en un diccionario y los pasó a la función.

En resumen, "args" y "kwargs" son parámetros especiales que permiten a las funciones de Python recibir argumentos variables. "Args" se utiliza para recibir argumentos no nombrados, mientras que "kwargs" se utiliza para recibir argumentos nombrados. Estos parámetros pueden ayudar a hacer que las funciones sean más flexibles y fáciles de usar.

# JSON encoder and decoder

La librería "json" de Python permite codificar y decodificar datos en formato JSON. JSON es un formato de datos ligero y fácil de leer que se utiliza comúnmente en aplicaciones web y móviles para enviar y recibir datos.
Una vez que hemos importado la librería, podemos usar sus funciones para codificar y decodificar datos en formato JSON. Por ejemplo, para codificar un diccionario Python en formato JSON, podemos usar la función json.dumps():

```py
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
json_str = json.dumps(my_dict)
print(json_str)
```

En este ejemplo, creamos un diccionario llamado my_dict y luego lo codificamos en formato JSON utilizando la función json.dumps(). Luego imprimimos la cadena JSON resultante en la consola.

Para decodificar una cadena JSON en un objeto Python, podemos usar la función json.loads():

```py
json_str = '{"name": "Alice", "age": 30, "city": "New York"}'
my_dict = json.loads(json_str)
print(my_dict)
```

En este ejemplo, creamos una cadena JSON llamada json_str y luego la decodificamos en un diccionario Python utilizando la función json.loads(). Luego imprimimos el diccionario resultante en la consola.

La librería "json" también proporciona opciones avanzadas para personalizar el proceso de codificación y decodificación. Por ejemplo, podemos proporcionar una función personalizada para codificar un objeto en formato JSON utilizando el parámetro default de la función json.dumps():

```py
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

def encode_person(obj):
    if isinstance(obj, Person):
        return {'name': obj.name, 'age': obj.age, 'city': obj.city}
    else:
        raise TypeError('Object of type Person is not JSON serializable')

my_person = Person('Alice', 30, 'New York')
json_str = json.dumps(my_person, default=encode_person)
print(json_str)
```

En este ejemplo, definimos una clase Person que representa una persona con un nombre, una edad y una ciudad. Luego definimos una función encode_person() que se utiliza para codificar objetos de la clase Person en formato JSON. Finalmente, creamos un objeto my_person de la clase Person y lo codificamos en formato JSON utilizando la función json.dumps() y el parámetro default.

En resumen, la librería "json" de Python permite codificar y decodificar datos en formato JSON. Esto es útil para enviar y recibir datos en aplicaciones web y móviles. La librería proporciona funciones simples para codificar y decodificar datos, así como opciones avanzadas para personalizar el proceso de codificación y decodificación.

</details>

---

<footer align="center">
<p align="center"><h3>Authors:</h3><p>
<p align="center"><a href="https://github.com/Sapitorico" target="blank">Sapitorico</a></p>
<p align="center"><a href="https://github.com/NeoDau" target="blank">NeoDau</a></p>
</footer>