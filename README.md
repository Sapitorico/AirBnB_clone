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

<table align="center" width="900"s> <!-- tabla de clases -->

<tr> <!-- columnas de la tabla -->

<th>Class</th>
<th>Description</th>
<th>File</th>

</tr>

<tr> <!-- fila 1  -->

<td>BaseModel</td> <!-- Class -->

<td> <!-- description -->

<details>
<summary><h2>BaseModel</h2></summary>

    Es la clase base de todos los modelos de AirBnB. Esta clase es la encargada de manejar la serialización/deserialización de los atributos de los otros modelos, y de guardar en un archivo JSON todos los objetos instanciados. También es la clase base de todos los otros modelos de AirBnB, por lo que hereda de ella.

<h3>Modulos</h3>

* uuid:
    El módulo uuid en Python proporciona objetos UUID inmutables (la clase UUID) y las funciones uuid1(), uuid3(), uuid4(), uuid5() para generar identificadores universalmente únicos. Los valores de UUID versión 1 se calculan utilizando la dirección MAC((MAC address) es un identificador único asignado a un controlador de interfaz de red (NIC) para su uso como dirección de red) del host, mientras que la versión 4 usa pseudo-random number generators para generar UUIDs. El módulo también ofrece una herramienta para acortar los UUIDs para su uso en URLs

* datetime:
    El módulo datetime en Python proporciona clases para manipular fechas y horas, permitiendo operaciones aritméticas con fechas y horas. Se puede crear un datetime manualmente pasando los parámetros (year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None). Para trabajar con fechas en Python se debe importar el módulo datetime que incorpora los tipos de datos date, time y datetime para representar fechas y horas.

</details>
</td>

<td><a href="">base_model.py</a></td> <!-- file -->

</tr> <!-- fin de fila 1-->

</table>

-----


<details>
<summary><h2 align="center">Recursos</h2></summary>



</details>


<footer>
<p align="center"><h3>Authors:</h3><p>
<p align="center"><a href="https://github.com/Sapitorico" target="blank">Sapitorico</a></p>
<p align="center"><a href="https://github.com/NeoDau" target="blank">NeoDau</a></p>
</footer>