# Dockerización
***
## Elección de imagen base
***
### Requisitos (Criterios de búsqueda)
- Imágenes oficiales o de comunidades relevantes y/o verificadas ya nos dará ciertas garantías de que lo que lleva es mantenido por un equipo con cierta experiencia y relevancia. (básicamente, nos asegura que la imagen del contenedor no la ha hecho un solo chaval de 16 años como hobby)

- Se priorizará el open source, por lo que si alguna organización que se dedica al software privativo tiene su propia imagen (como IBM), no se tendrá en cuenta. Así como las imágenes de contenedores basados en Windows serán ignorados.

- Debe ser una versión específica y no una latest para asegurarnos de que en dichas versiones todo funciona y que no vayan a sufrir algún fallo debido a algún cambio de alguna dependencia externa. Por lo que se usarán inmutable tags. Además de buscar siempre imágenes estables, descartando las beta o similares.

- Dado que actualmente el proyecto no tiene ninguna dependencia fuerte de funciones exclusivas de versiones concretas de Python, en busca de evitar conflictos o posibles errores, se utilizará la misma versión de Python que la empleada en el equipo de desarrollo. En concreto, Python 3.9.10 o subversiones de 3.9 (3.9, 3.9.7, 3.9.10, etc).

### Requisitos (Criterios de selección) en orden de prioridad
1.  Menor tamaño posible

2.  Tiempos de construcción mínimos 

3.  Menor número de vulnerabilidades posible

***
### Opciones Existentes

Una vez establecidos los criterios de búsqueda, las opciones que encontramos y que analizaremos usando los criterios de selección son las siguientes:

- Imagen SO base (Ubuntu, Debian, CentOS, etc) + instalación manual Python.
- [Imágenes de Bitnami](https://hub.docker.com/r/bitnami/python), en concreto la que se ajusta a mis criterios de búsqueda es **bitnami/python:3.9.10 (174.85 MB)**. Tienen también bitnami/python:3.9.10-debian-10-r16 pero es la misma solo que renombrada pues tienen exactamente los mismos Image Layers (líneas que componen el Dockerfile que muestra Docker Hub). Esta organización no tiene distinción de imágenes según su tamaño por lo que no hay más que elegir.
- [Imágenes de CircleCI](https://hub.docker.com/r/cimg/python), en concreto **cimg/python:3.9.10 (629.73 MB)**. Esta organización tiene otras variantes como 3.9.10-node y 3.9.10-browsers, las cuales quedan descartadas y no entran a esta valoración pues son imágenes que añaden contenido a la 3.9.10 de base, la de 3.9.10-node añade Node.js (innecesario para este proyecto) y la de 3.9.10-browsers añade todo lo mencionado anteriormente (incluido Node.js) y además Java y Selenium, también innecesarios.
- [Imágenes oficiales de Python](https://hub.docker.com/_/python), las cuales se dividen a su vez en las siguientes variantes:
  - **python:3.9.10 (324.21 MB)**
  - **python:3.9.10-bullseye (324.21 MB)**
  - **python:3.9.10-buster (315.23 MB)**
  - **python:3.9.10-slim (43.97 MB)**
  - **python:3.9.10-slim-bullseye (43.97 MB)**
  - **python:3.9.10-slim-buster (41.56 MB)**
  - **python:3.9.10-alpine3.15 (17.96 MB)**
- Se han encontrado también las [imágenes de PyPy](https://hub.docker.com/_/pypy?tab=description), las cuales no sabía lo que eran pero tras una investigación he visto que PyPy es otro intérprete para Python, el cual presume de ser más rápido. Al no haber usado PyPy en el entorno de desarrollo del proyecto, no me he querido arriesgar a usarlo ahora por lo que las imágenes de PyPy han sido descartadas. 

***
### Proceso de selección y estudio

Para el estudio primero me centraré en las que vienen ya hechas, y más tarde valoraré frente a una hecha manualmente.

Una vez vistas todas las opciones, y tras un vistazo a la diferencia entre todas los variantes diferentes de las oficiales de Python, lo primero que haré será descartar las bullseye ya que estas no son más que una especie de pseudo betas, es decir, son las siguientes versiones que van a salir, pero que aún no han salido porque todavía no son stable, así que siguiendo los criterios de búsqueda, las dos bullseye que aparecen en la lista (python:3.9.10-bullseye y python:3.9.10-slim-bullseye) son descartadas. 

A continuación, viendo los tamaños de cada una de las imágenes, siguiendo el criterio del menor tamaño posible podemos descartar varias de ellas, en concreto: la de CicleCI cimg/python:3.9.10 (629.73 MB), así como las siguientes oficiales de python: python:3.9.10 (324.21 MB) y python:3.9.10-buster (315.23 MB) ya que en un primer vistazo y a falta de comparar más criterios, ya vemos alternativas mejores en cuanto a espacio ocupado, siendo este uno de los puntos más importantes en mi criterio de selección.

Como siguiente paso voy a comparar los tiempos de ejecución necesarios para cada una, creando un Dockerfile con las mismas tareas para cada una de ellas. El Dockerfile será el siguiente para todas las imágenes a excepción de la alpine. (El motivo por el que el de alpine usará otro Dockerfile lo explicaré más adelante.) Variando únicamente la línea del FROM XXXXXX/xxxxx:xxxx entre las diferentes alternátivas. (La justificación por la que se usa este Dockerfile también está redactada a continuación)

 ```md
FROM XXXXXX/xxxxx:xxxx

#Creo el grupo y usuario testeo
RUN groupadd testeo && useradd -ms /bin/bash -g testeo testeo

#Cambia al usuario testeo
USER testeo

#Establezco un directorio en el que haré las instalaciones y copiaré el task.yaml
WORKDIR /home/testeo

#Actualizo pip pues es el instalador de paquetes que voy a usar
RUN python -m pip install --upgrade pip

#Instalo el task runner
RUN pip3 install --user pypyr

#Copio el código con las tareas del task runner
COPY task.yaml ./

#Configuro path para que encuentre pypyr
ENV PATH=$PATH:/home/testeo/.local/bin

#Instalo dependencias del proyecto
RUN pypyr task installdeps

#Cambio a un directorio exclusivo para pasar los test
WORKDIR /app/test

ENTRYPOINT ["pypyr","task","test"]

 ```

Sin embargo para la imagen de python:3.9.10-alpine3.15 he necesitado hacer un par de modificaciones, entre ellas, cambiar el comando `groupadd` y `useradd` por `addgroup` y `adduser` respectivamente. Así como la necesidad de instalar gcc pues al ser la versión tan mínima, no lleva gcc y en mi caso es necesario para usar pypyr. Por lo que he tenido que añadir la orden `RUN apk add build-base` según la [Alpine Linux Wiki](https://wiki.alpinelinux.org/wiki/GCC) para instalar gcc. Quedando el Dockerfile de alpine de la siguiente manera:

```md
FROM python:3.9.10-alpine3.15

#Como estoy en alpine, no trae gcc y lo necesito, por tanto
RUN apk add build-base

#Creo el grupo y usuario testeo
RUN addgroup -S testeo && adduser -S testeo -G testeo

#Cambia al usuario testeo
USER testeo

#Establezco un directorio en el que haré las instalaciones y copiaré el task.yaml
WORKDIR /home/testeo

#Actualizo pip pues es el instalador de paquetes que voy a usar
RUN python -m pip install --upgrade pip

#Instalo el task runner
RUN pip3 install --user pypyr

#Copio el código con las tareas del task runner
COPY task.yaml ./

#Configuro path para que encuentre pypyr
ENV PATH=$PATH:/home/testeo/.local/bin

#Instalo dependencias del proyecto
RUN pypyr task installdeps

#Cambio a un directorio exclusivo para pasar los test
WORKDIR /app/test

ENTRYPOINT ["pypyr","task","test"]

```

Una vez construidas correctamente todas las imágenes, he obtenido los siguientes resultados:

| REPOSITORY            |  IMAGE ID     | SIZE  | Building Time | Building Time (Cached) |
|-----------------------|---------------|-------|---------------|------------------------|
| python_bitnami        |  9561c56f4203 | 526MB | 32.5s (14/14) | 0.8s (13/13) |
| python_alpine         |  3473a9b4006b | 268MB | 39.1s (16/16) | 1.4s (15/15) |
| python_slim_buster    |  73fbf2d98f4f | 139MB | 18.2s (14/14) | 0.7s (13/13) |
| python_slim           |  92b29a2b3753 | 147MB | 22.5s (14/14) | 0.8s (13/13) |

Tras esto saco varias conclusiones. Para empezar me llama la atención que la alpine, pese a ser la más ligera y mínima de primeras, tras instalar las dependencias necesarias, pasa a ocupar más que las slim, y que debido a la necesidad de instalar dependencias externas, el tiempo de construcción aumenta considerablemente en comparación con las slim que sí traen más paquetes necesarios, por lo que tras esto descarto la versión alpine. 

Siguiendo por la de bitnami, al ser una imagen más pesada que las slim, también se refleja en el tiempo de construcción, consiguiendo tiempos notáblemente peores, por lo que viendo que pesa más y que tarda más en construirse, también es descartada.

Y a la hora de optar entre `python:3.9.10-slim` y `python:3.9.10-slim-buster`, viendo el análisis hecho hasta ahora, el sentido común diría que use python_slim_buster pues es la que menos ocupa y menos tarda en construir de las dos, pero al ser diferencias tan pequeñas, quiero tener en cuenta otro criterio más para decidirme, en este caso, el de seguridad, por lo que usando la herramienta incluida por defecto `docker scan` la cual analiza las vulnerabilidades de los contenedores, analizaré ambas imágenes, de la cual obtengo lo siguiente:

- Para `python:3.9.10-slim-buster`

![docker scan python:3.9.10-slim-buster](/docs/imgs/vulnerabilidad_slim_buster.png)

- Para `python:3.9.10-slim`

![docker scan python:3.9.10-slim](/docs/imgs/vulnerabilidad_slim.png)

Este resultado me sorprendió porque indica que la slim usa como imagen base slim-bullseye, por lo que volví a generar la slim por si me había equivocado al hacer el Dockerfile, pero efectivamente estaba bien y volvió a dar el mismo resultado.

**Por lo que teniendo en cuenta las vulnerabilidades y la seguridad, me quedo con la `python:3.9.10-slim` ya que en tamaño y tiempos estaban muy a la par.**
***
**Bonus:** Tras esto por curiosidad también analicé la de `python:3.9.10-alpine3.15`, ya que al ser una imagen tan reducida y tan recortada en cuanto a dependencias, debería notarse en cuanto a vulnerabilidades, la cual me dió el siguiente resultado:

![docker scan python:3.9.10-alpine3.15](/docs/imgs/vulnerabilidad_alpine.png)

Efectivamente al tener tan pocas dependencias, las vulnerabilidades son mucho menores que en el resto. Por lo que saco como conclusión que si mi principal criterio fuese usar una imagen segura, sin importar tiempos de construcción ni tamaño, me quedaría con python:3.9.10-alpine3.15.
***
#### Segunda fase comparativa
Llegados a este punto he comparado las imagénes ya hechas y me he quedado con la que mejor se ajusta a mis criterios, pero todavía me queda compararla con la opción de coger una imagen base de un SO e instalarle Python manualmente.

A estas alturas deduzco que el resultado no será mejor que el de la elegida hasta ahora, pues al empezar a instalar módulos y herramientas, seguramente pase algo similar a lo que ha pasado con alpine, pero partiendo de una imagen más pesada... Aún así de forma simbólica lo realizaré para contrastar más este estudio.

Para elegir el SO de base cabría la opción de hacer otro estudio como el realizado hasta ahora pero cogiendo cada una de las imágenes disponibles, pero dado que no voy sobrado de tiempo, y que la opción elegida actualmente ya de por si satisface los requisitos, y que llegados a este punto estoy haciendo esta comparativa más a modo de ilustración que como alternativa real, utilizaré una cualquiera, en este caso Ubuntu por ser la distribución más usada. En concreto Ubuntu 22.04 ya que es de las más recientes y cuenta con bastante soporte y mantenimiento.

El Dockerfile quedaría de la siguiente manera:

```python
FROM ubuntu:22.04

#Para que el gestor de paquetes apt no espere que interacción y se quede hasta el infinito esperando una entrada por teclado
ENV DEBIAN_FRONTEND noninteractive

#Actualizo los repositorios e instalo python3 y pip3
RUN apt update && apt install python3 python3-pip -y

#Creo el grupo y usuario testeo
RUN groupadd testeo && useradd -ms /bin/bash -g testeo testeo

#Cambia al usuario testeo
USER testeo

#Establezco un directorio en el que haré las instalaciones y copiaré el task.yaml
WORKDIR /home/testeo

#Configuro path para que encuentre pypyr y python3
ENV PATH=$PATH:/home/testeo/.local/bin

#Actualizo pip pues es el instalador de paquetes que voy a usar ahora
RUN python3 -m pip install --upgrade pip

#Instalo el task runner
RUN pip3 install --user pypyr

#Copio el código con las tareas del task runner
COPY task.yaml ./

#Instalo dependencias del proyecto
RUN pypyr task installdeps

#Cambio a un directorio exclusivo para pasar los test
WORKDIR /app/test

ENTRYPOINT ["pypyr","task","test"]

```

Y tras contruirlo para obtener sus tiempos y tamaño, obtengo los siguientes resultados en comparación con `python:3.9.10-slim`:

| REPOSITORY            |  IMAGE ID     | SIZE  | Building Time | Building Time (Cached) |
|-----------------------|---------------|-------|---------------|------------------------|
| python_slim           |  92b29a2b3753 | 147MB | 22.5s (14/14) | 0.8s (13/13) |
| ubuntu                |  f771ef13c25d | 481MB | 42.3s (16/16) | 1.6s (15/15) |

En cunto al analisis de seguridad, de forma sorprendente encontramos lo siguiente:

![docker scan ubuntu manual](/docs/imgs/vulnerabilidad_ubuntu.png)

Este resultado me sorprende bastante y en cierta parte me extraña que sea tan buen, pero deduzco que al ser una de las últimas versiones de Ubuntu, aún no haya demasiados reportes de fallos conocidos para ella, sumado a que es la que tiene más soporte, resulte en que no tienen ninguna vulnerabilidad conocida.

Pero a pesar de tener tan buen resultado en vulnerabilidades, el tamaño y tiempo de construcción es significativamente mayor al de `python:3.9.10-slim`, por lo que sigo manteniendo la elección que hice anteriormente. Llegando a la conclusión final de que cualquier imagen a la que haya que instalarle dependencias extra, como puede ser python, o gcc, van a provocar que su tamaño y tiempo de construcción suban considerablemente en comparación con las imágenes oficiales de python.

Remarcar que si lo que se busca es a toda costa una imagen segura sin importar tiempo de construcción ni tamaño, la mejor opción será una alpine o un SO base + python manual, viendo los resultados de este análisis.

> Concusión final: Tras todas las pruebas realizadas y siguiendo los requisitos perviamente establecidos, la imagen elegida ha sido `python:3.9.10-slim`.


***
## Elección de Dockerfile
***

La creación del Dockerfile se ha ido siguiendo a la vez que el análisis realizado anteriormente según las necesidades que han sido requeridas a medida que el desarrollo del análisis iba avanzando, pero las explicaciones de elección de cada línea serán detalladas a continuación. Para empezar el Dockerfile final se puede encontrar [aquí](../Dockerfile) y tiene el siguiente aspecto:

```md
FROM python:3.9.10-slim

#Creo el grupo y usuario testeo
RUN groupadd testeo && useradd -ms /bin/bash -g testeo testeo

#Cambia al usuario testeo
USER testeo

#Establezco un directorio en el que haré las instalaciones y copiaré el task.yaml
WORKDIR /home/testeo

#Actualizo pip pues es el instalador de paquetes que voy a usar
RUN python -m pip install --upgrade pip

#Instalo el task runner
RUN pip3 install --user pypyr

#Copio el código con las tareas del task runner
COPY task.yaml ./

#Configuro path para que encuentre pypyr
ENV PATH=$PATH:/home/testeo/.local/bin

#Instalo dependencias del proyecto
RUN pypyr task installdeps

#Cambio a un directorio exclusivo para pasar los test
WORKDIR /app/test

ENTRYPOINT ["pypyr","task","test"]

```

- `RUN groupadd testeo && useradd -ms /bin/bash -g testeo testeo` se hace para crear un usuario llamado testeo junto con un grupo llamado igual, (al que se le asigna después), para que sea el usuario bajo el que instalar pypyr y ejecutar python
  
- `USER testeo` se cambia de usuario en el Dockerfile para que a partir de ahora las instrucciones se hagan por ese usuario
  
- `WORKDIR /home/testeo` se establece un directorio actual sobre el que se trabaja. Realmente en todo momento hay un WORKDIR establecido, aunque no se ejecute esa orden, pues por defecto  ya se trabaja sobre uno. Además, si la ruta que le he indicado no existe, la crea, y como el usuario activo es testeo, se crearía con dicho propietario, por lo que no es necesario ni un mkdir ni un chown cuando se usa WORKDIR. Sobre esta ruta es sobre la que se harán todas las instalaciones además de ser donde se copiará el task.yaml de pypyr necesario para la tarea installdeps

- `RUN python -m pip install --upgrade pip` se actualiza la versión de pip instalada, sería un similar a ejecutar apt update si fuésemos a trabajar con apt. Solo que en este caso la versión de pip también se actualiza. Esto se hace para asegurar que no nos de problemas ni warnings cuando vayamos a instalar pypyr.

- `RUN pip3 install --user pypyr` se instala pypyr para poder usar la tarea de instalar dependencias y no tener que instalarlas todas a mano de esta forma. Se usa el flag --user para que se instale en el home del usuario en vez de en el directorio del sistema.

- `COPY task.yaml ./` se copia adentro del contenedor el fichero task.yaml que contiene las tareas a ejecutar por el task runner, para que lo encuentre al ejecutarlo más adelante.

- `ENV PATH=$PATH:/home/testeo/.local/bin` se establece el path adecuado para que al ejecutar el comando pypyr, encuentre el binario y no nos salte el mensaje de error de comando no encontrado.

- `RUN pypyr task installdeps` ejecuta el task runner con la tarea de instalar las dependencias del proyecto.

- `WORKDIR /app/test` se cambia el directorio con el fin de utilizarlo exclusivamente como rootdir para cuando se pasen los test

- `ENTRYPOINT ["pypyr","task","test"]` la orden que se ejecutará cuando se lance el contenedor.

***
## Github Action
***
En este caso, las condiciones que deseo que se den para que se actualice la imagen en DockerHub son o bien un **push**, o bien un **pull request**. Pero ambos siempre y cuando se haya **modificado el Dockerfile** ya que será el archivo que afecta a la imagen. 