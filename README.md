# SearchCulture
---
## Descripción: :page_with_curl:

Proyecto en la nube que será capaz de recomendar contenido (Películas, Series, Libros y Música) a los usuarios, en base a sus gustos (o a los gustos que deseen encontrar). El proyecto te hará una serie de preguntas con el fin de procesarlas para conocer un poco la personalidad adecuada, y dependiendo de las respuestas, generar unos resultados acordes. En resumidas cuentas, es un ___recomendador de contenido según gustos y personalidad.___

## Licencia: MIT :recycle:

## User Journey:airplane: e Historias de Usuario: Disponible en [docs/contexto.md](https://github.com/migueorg/SearchCulture/blob/Objetivo-1/docs/contexto.md) 

## Otra documentación secundaria: [docs/wiki.md](https://github.com/migueorg/SearchCulture/blob/Objetivo-1/docs/wiki.md) :file_folder:

## Automatización:

Como Task Runner se ha optado por usar [pypyr](https://github.com/pypyr/pypyr). Puedes ver su proceso de elección [aquí](https://github.com/migueorg/SearchCulture/blob/Objetivo-3/docs/taskrunner_choice.md).

### Instalación pypyr
Para poder usar pypyr es necesaria su instalación a traves de pip (por lo que Python y pip son necesarios y se da por hecho que están instalados).
> $ pip3 install --user pypyr

### Órdenes disponibles en pypyr

#### Listar Tareas
Mostrará una lista con las tareas programadas en 
> pypyr task list

#### Instala dependencias
Instalará las dependencias necesarias para ejecutar el proyecto
> pypyr task installdeps

#### Ejecuta el proyecto
Lanza todas las órdenes necesarias para que el proyecto se ejecute
> pypyr task run

#### Comprobar sintaxis
Comprueba si la sintaxis está correcta
> pypyr task check

#### Ejecutar los test (Soon...)
Ejecuta los test programados
> pypyr task test