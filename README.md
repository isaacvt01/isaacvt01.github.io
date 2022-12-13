### Introduccion
El gobierno quiere reducir el número de coches en las calles de Mallorca, y para eso han pensado en crear una red de alquiler de bicicletas.
Hablar de porque haceis este projecto. Cuál es la finalidad.
Explicar generar html y que hay una interfaz admin para CRUD bicycles.

### Tecnologia
- Python
- HTML
- CSS
- GitHubPages
- Mongo DB
- GIT

### Modulos Python
Modules de python, estan en requirements.txt

Python: Tkinter, pytest


### Installation
Git clone: nuestro link al git repository
Executar: pip install -r requirements.txt

### Uso
1. Generar HTML: main.py
2. Tkinter: run_admin.py

En main.py todas las funciones para crear los archivos:
index.html
En run_admin

## Metodología

Hemos utilizado la metodología SCRUM, nos hemos planificado en dos SPRINTS.

En el primero hicimos lo más relevante para el cliente, que era mostrar todas las bicicletas en una página, otra página
que las muestre según su marca y otra que las muestre según su tipo. En este sprint también añadimos CSS a las páginas web

En el segundo sprint hicimos el CRUD, lo que permite al usuario poder administrar la base de datos desde el programa, hicimos
el CSS Responsive

Hemos utilizado validadores para HTML y CSS.

Links de los validadores:

- CSS: https://jigsaw.w3.org/css-validator/
- HTML: https://validator.w3.org/


## Implementación

Lo que se ha instalado y utlizado de Python y MongoDb

- Python
  - **Pytest** es un marco de trabajo que permite realizar pruebas unitarias para un software en Python. Lo hemos utilizado para comprobar el correcto funcionamiento de las funciones y librerías
  - **Coverage** con **pytest** es lo que utilizamos para medir el código que cubre un programa. Crea informes en una gran variedad de formatos.
  - **Tkinter** es la interfaz gráfica por defecto de Python. Es un módulo que envuelve la impelentación de widgets como clases. Es un módulo interno.
- MongoDB
  - **MongoAtlas** es un servicio de Cloud Database. Esto nos permite administrar la BBDD Mongo desde cualquier lugar.
  - **MongoCompass** es la versión de escritorio de MongoAtlas. Se puede utilizar en sustitución de MongoAtlas.
  - **MongoShell** es el shell de MongoDB, desde este nos podemos conectar directamente a nuestra base de datos y llevar un control más exacto de las acciones que hacemos sobre ella sin interfaz gráfica.
  - **Pymongo** Es la librería que contiene las herramientas que utlizamos para trabajar con MongoDB en Python.
- **HTML5 y CSS**
  - Flex y Grid con CSS.
  - Media queries para hacer la parte responsive para tablets.
- Git para llevar a cabo el control de versiones.
- Markdown

## Requisitos
- El usuario puede ver un listado con todas las bicicletas
- El ussuario puede iniciar la navegación desde una página principal para poder visitar las páginas web
- El usuario puede listar las biciceltas según su marca
- El usuario puede ver una página con los detalles de cada bicicleta
- El usuario puede navegar hasta la página principal para acceder a las diferentes páginas
- El usuario puede listar las bicicletas según su tipo para poder acceder a un tipo deseado
- El usuario debe poder administrar la base de datos

# Descripcion tecnica


### Estructura del Programa

![Diagrama de componentes](/readme_images/image.png)
#### Marcado rojo (Creación de la interfaz web)
Con el marcado rojo indicamos las relaciones que hay en los módulos con sus diferentes funciones de la creación de la interfaz web.

#### Marcado azul
Con el marcado azul indicamos las relaciones que hay entre los módulos de la interfaz CRUD creada con Tkinter.
#### Marcado negro
Con el marcado negro indicamos las relaciones entre paquetes y módulos.


- db, logic, presentasion
    - que rol tiene cada folder
    - como estan relacionados

### TEST 
- cuanto coverage
- que se ha testeado
- que no se ha podido testear y porque


### CLOCKIFY

Como se puede ver en el gráfico, hemos invertido 112h, es una aproximación, ya que cuando empezamos a hacer el proyecto, no teníamos esta herramienta.

- **Creating DB:** Diseñar la arquitectura de la base de datos e imputar los datos necesarios para realizar las pruebas lo más realistas posibles.
- **Creating tests:** Crear las pruebas necesarias para asegurarnos de que el código hace lo que queremos que haga y que se encuentren el mínimo de bugs posibles.
- **Documentation:** Crear Readme y diagramas.
- **Git-Hub Pages:** Arreglar todos los problemas ocasionados por rutas y entender GitHub Pages.

![Gráfico Clockify](/readme_images/Clockify.PNG)
- En que hemos invertido el tiempo

### Conclusion

