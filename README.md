### Introduccion
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


### Installation
Git clone: nuestro link al git repositoruy
Executar: pip install -r requirements.txt


### Uso
1. Generar HTML: main.py
2. Tkinter: run_admin.py


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


## Requisitos
- El usuario puede ver un listado con todas las bicicletas
- El ussuario puede iniciar la navegación desde una página principal para poder visitar las páginas web
- El usuario puede listar las biciceltas según su marca
- El usuario puede ver una página con los detalles de cada bicicleta
- El usuario puede navegar hasta la página principal para acceder a las diferentes páginas
- El usuario puede listar las bicicletas según su tipo para poder acceder a un tipo deseado
- El usuario debe poder administrar la base de datos

# Descripcion tecnica

### Esquema Base Datos (no hace falte)

### Estructura del Programa

![Diagrama de componentes](/readme_images/image.png)
#### Marcado rojo(Creación de la interfaz web)
Con el marcado rojo queremos indicar las relaciones que hay en los módulos con sus diferentes funciones de la creación de la interfaz web

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
- Poner foto del gráfico
- En que hemos invertido el tiempo

### Conclusion
- Puntos fuertes de programa
- Possibles mejores

### Dificultades

- Organización del tiempo