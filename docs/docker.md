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