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
