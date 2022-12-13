# Tabla de contenidos

- [Introducción](#introduccion)
- [Tecnología](#tecnologia)
- [Instalación](#instalacion)
- [Uso](#uso)
- [Metodología](#metodologia)
- [Implementación](#implementacion)
  - [Python](#python)
  - [MongoDB](#mongodb)
  - [HTML y CSS](#html)
-[Requisitos](#requisitos)
- [Descripción técnica](#descripcion-tecnica)
  - [Arquitectura del programa](#arquitectura)
  - [Estructura del programa](#estructura)
  - [Componentes](#componentes)
- [Test](#test)
- [Clockify](#clockify)
- [Conclusión](#conclusion)
  - [Puntos fuertes](#puntos-fuertes)
  - [Posibles mejoras](#posibles-mejoras)
- [Dificultades](#dificultades)

<div id="introduccion">

### Introduccion
El gobierno quiere reducir el número de coches en las calles de Mallorca, y para eso han pensado en crear una red de alquiler de bicicletas.
Hablar de porque haceis este projecto. Cuál es la finalidad.
Explicar generar html y que hay una interfaz admin para CRUD bicycles.

<div id="tecnologia">

### Tecnologia
- Python
- HTML
- CSS
- GitHubPages
- Mongo DB
- GIT

<div id="instalacion">

### Instalación
Git clone: nuestro link al git repository
Executar: pip install -r requirements.txt

<div id="uso">

### Uso

- Para generar HTML se debe utilizar main.py, solo debes ejecutar este archivo y se generarán todos los archivos html.
- Para llevar a cabo las operaciones CRUD debes ejecutar el archivo run_admin.
  1. Una vez ejecutado, saldrá una pequeña ventana que nos pedirá usuario y contraseña. El usuario es Admin y la contraseña 1234.
  2. Una vez dentro, nos dará a elejir entre las opciones: ***Actualizar, Eliminar, Crear y Leer.***

<div id="metodologia">

## Metodología

Hemos utilizado el marco de trabajo SCRUM, nos hemos planificado en dos SPRINTS.

En el primero hicimos lo más relevante para el cliente, que era mostrar todas las bicicletas en una página, otra página
que las muestre según su marca y otra que las muestre según su tipo. En este sprint también añadimos CSS a las páginas web

En el segundo sprint hicimos el CRUD, lo que permite al usuario poder administrar la base de datos desde el programa, hicimos
el CSS Responsive

Hemos utilizado validadores para HTML y CSS.

Links de los validadores:

- CSS: https://jigsaw.w3.org/css-validator/
- HTML: https://validator.w3.org/

<div id="implementacion">

## Implementación


<div id="python">

- Python
  - **Pytest** es un marco de trabajo que permite realizar pruebas unitarias para un software en Python. Lo hemos utilizado para comprobar el correcto funcionamiento de las funciones y librerías
  - **Coverage** con **pytest** es lo que utilizamos para medir el código que cubre un programa. Crea informes en una gran variedad de formatos.
  - **Tkinter** es la interfaz gráfica por defecto de Python. Es un módulo que envuelve la impelentación de widgets como clases. Es un módulo interno.

<div id="mongodb">

- MongoDB
  - **MongoAtlas** es un servicio de Cloud Database. Esto nos permite administrar la BBDD Mongo desde cualquier lugar.
  - **MongoCompass** es la versión de escritorio de MongoAtlas. Se puede utilizar en sustitución de MongoAtlas.
  - **MongoShell** es el shell de MongoDB, desde este nos podemos conectar directamente a nuestra base de datos y llevar un control más exacto de las acciones que hacemos sobre ella sin interfaz gráfica.
  - **Pymongo** Es la librería que contiene las herramientas que utlizamos para trabajar con MongoDB en Python.
  
<div id="html">

- **HTML5 y CSS**
  - Flex y Grid con CSS.
  - Media queries para hacer la parte responsive para tablets.
- Git para llevar a cabo el control de versiones.
- Markdown
- GitHub Pages como servidor web para alojar nuestra página estática.

<div id="requisitos">

## Requisitos

En este apartado explicamos los requisitos mínimos que tenía que cumplir este proyecto.
- El usuario puede ver un listado con todas las bicicletas
- El usuario puede iniciar la navegación desde una página principal para poder visitar las páginas web
- El usuario puede listar las biciceltas según su marca
- El usuario puede ver una página con los detalles de cada bicicleta
- El usuario puede navegar hasta la página principal para acceder a las diferentes páginas
- El usuario puede listar las bicicletas según su tipo para poder acceder a un tipo deseado
- El usuario debe poder administrar la base de datos

<div id="descripcion-tecnica">

# Descripción técnica

<div id="arquitectura">

## Arquitectura del programa

![Arquitectura del programa](/readme_images/arquitectura.PNG)

<div id="estructura">

## Estructura del Programa

![Diagrama de componentes](/readme_images/image.png)
### Marcado rojo (Creación de la interfaz web)
Con el marcado rojo indicamos las relaciones que hay en los módulos con sus diferentes funciones de la creación de la interfaz web.

### Marcado azul (Realización CRUD Tkinter)
Con el marcado azul indicamos las relaciones que hay entre los módulos de la interfaz CRUD creada con Tkinter.
### Marcado negro (Relación de paquetes y módulos)
Con el marcado negro indicamos las relaciones entre paquetes y módulos.

<div id="componentes">

### Componentes

`logic` package que contiene page_builder, es el archivo encargado de crear los diferentes archivos, coordina todas las funciones que están dentro de /presentation/view.  

`presentation` package que contiene los packages `view` y `tkinter`.  

`view` package que contiene las diferentes plantillas que son llamada.

`tkinter` package que contiene la interfaz gráfica que se relaciona con el CRUD.

`db` package que contiene los packages `connection`, `create`, `delete`, `read`, `update`.

- `connection` package que contiene el módulo encargado de conectarse con la base de datos.

- `create` package que contiene el módulo encargado de crear los documentos en la base de datos.

- `delete` package que contiene el módulo encargado de eliminar documentos en la base de datos.

- `read` package que contiene los módulos encargados de leer la información en la base de datos. 

- `update` package que contiene el módulo encargado de actualizar documentos en la base de datos.

`docs` fichero donde se encuentran los diferentes archivos html y css.


<div id="test">

### TEST 
- cuanto coverage
- que se ha testeado
- que no se ha podido testear y porque


<div id="clockify">

### CLOCKIFY

Hemos utilizado Clockify para tener bajo control el tiempo que dedicábamos a cada cosa.

- **Creating DB:** Diseñar la arquitectura de la base de datos e imputar los datos necesarios para realizar las pruebas lo más realistas posibles.
- **Creating tests:** Crear las pruebas necesarias para asegurarnos de que el código hace lo que queremos que haga y que se encuentren el mínimo de bugs posibles.
- **Documentation:** Crear Readme y diagramas.
- **Git-Hub Pages:** Arreglar todos los problemas ocasionados por rutas y entender GitHub Pages.
- **HTML and CSS:** En este apartado no solo contamos la creación de los archivos CSS, también contamos la creación de los archivos HTML desde Python, ya que hemos realizado un script de Python para que escriba todo el HTML y cree los archivos necesarios.
- **Refactoring:** Aquí reflejamos el tiempo que hemos dedicado a hacer más entendible el código y quitar partes que no eran necesarias del mismo.
- **Tkinter:** Hacer la interfaz gráfica del CRUD.

***En todos estos apartados no ha sido incluido el tiempo de aprendizaje como tal, solo el de implementación.***

![Gráfico Clockify](/readme_images/Clockify.PNG)

Nuestra predicción era de un tiempo mucho menor. En el apartado de dificultades explicamos por qué no pudimos cumplir con las expectativas.

<div id="conclusion">

### Conclusión

<div id="puntos-fuertes">

- Puntos fuertes del programa

  - Rápido y fiable: Hemos puesto muchas horas para que la aplicación sea lo más eficiente posible
  - Variable de entorno: En vez de tener toda la información sensible de la conexión a la base de datos, hemos creado una variable de entorno y la llamamos desde la URI de MongoAtlas.
  - Actualización y despliegue facil de los archivos html.
  - Creemos tener un código bien organizado.
  
<div id="posibles-mejoras">

- Posibles mejoras

  - Creación de funciones: Nos hemos dado cuenta de que podríamos haber creado más funciones para introducirlas en nuestros archivos HTML, ya que utilizamos las mismas partes en diferentes páginas y hubiera quedado un codigo más limpio, como por ejemplo el footer. 
  - Realizar la colección de tiendas: Nuestro plan era realizar en la base de datos una colección llamada tiendas, con diferentes tiendas en Mallorca, pero por falta de tiempo, hemos decidido no incluirla.
  - Administración de tiempo: Empezamos con el proyecto enseguida que se nos comunicó y decidimos hacerlo con librerías y modulos de python. Al explicarnos por completo el proyecto, se nos dijo que no podíamos utilizar dichas librerías y tuvimos que refactorizar todo el proyecto.
  - Invertir más tiempo en el diseño: Nos viera gustado realizar nuestro front-end de mejor manera, pero al final hemos querido cumplir con los requisitos que se pedían y invertir más tiempo en el back-end, documentación, etc.
  - Commits: Empezamos haciendo muy pocos commits.
  - CSS se podría organizar mejor: Tenemos código CSS que lo usamos en todos varias páginas, pero lo hemos escrito varias veces en archivos diferentes de css. El CSS que comparten varias páginas, se podrían guardar en un único archivo css y usar este archivo en todas las páginas en las que se usan las mismas clases.

<div id="dificultades">

### Dificultades

- Tkinter: Hemos tenido que estudiar cómo funciona Tkinter con Python y saber elaborar la interfaz gráfica para realizar el CRUD.
- Pymongo: Hemos tenido que estudiar cómo funciona pymongo para poder extraer los datos que tenemos en nuestra base de datos.
- Realización de tests
- Git y github: git nos ha dado bastantes problemas, ya que no sabíamos exactamente cómo trabajar con ello y al principio cometimos bastantes errores, por ejemplo trabajamos en los mismos directorios y archivos y eso nos creaba conflictos a la hora de hacer un push. Con GitHub hemos tenido más facilidades ya que lo estuvimos tocando en el FP medio para subir los proyectos que realizábamos.
- Problemas con las rutas del entorno local y el entorno prod: Las mismas rutas no nos iban bien en los dos entornos. Hemos tenido que simular un entorno prod con un servidor web local. Para ello hemos usado el servidor http que viene por defecto con python: https://developer.mozilla.org/en-US/docs/Learn/Common_questions/set_up_a_local_testing_server 
- Github pages: Hemos tenido que reorganizar algunas carpetas para hacer un deploy correcto en Github Pages. Aparte de esto, hemos tenido que corregir los link en la página porque estaban rotos.
- Organización del tiempo: Al ser el primer proyecto grande que hacíamos, consideramos que podríamos haber tenido una mejor organización del tiempo.
- Encoder UTF-8: Dedicamos más del tiempo esperado para esto, ya que no era un problema de HTML y era un trozo de codigo que teníamos que añadir en el page_builder al crear nuestras páginas HTML.
