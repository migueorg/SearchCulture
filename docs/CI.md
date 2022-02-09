# Integración Continua
***
## Elección sistema de Integración Continua
***
### Requisitos (Criterios de búsqueda)
- Debe estar hospedado por ellos mismos, es decir ya implementado en la nube. A pesar de que personalmente soy defensor de fomentar el self-hosted y no tener que depender de terceros, actualmente no disponemos de infraestructura propia ni de la figura de un sysadmin que gestione nuestra infraestructura. Y otra solución como alquilar un VPS nos supondría un coste adicional además de igualmente tener que emplear recursos en gestión y mantenimiento de los mismos, por lo que se buscarán servicios que ya ofrezcan su herramienta lista para usar en la nube. 
- Debe disponer de al menos un plan básico gratuito, ya sea mediante sistema de créditos o minutos gratis al mes.
- Tiene que ser compatible con los [Github Checks](https://docs.github.com/en/rest/reference/checks) para poder integrarse en nuestro proyecto de forma continua y automática.
- Que no sea CircleCI, porque ya a estas alturas lo ha usado todo el mundo.
- Debe tener la posibilidad de trabajar con [Matrix Jobs](https://docs.travis-ci.com/user/build-matrix/) lo cual nos ahorrará mucho tiempo y vendrá bien a la hora de escribir las múltiples tareas a ejecutar en paralelo.
- Se buscará que sean conocidos, o de organizaciones importantes, o bastante usados, lo cual no quiere asegurar que sea mejor (véase Log4j), pero nos vendrá bien a la hora de buscar información, tutoriales y ejemplos externos a parte de la documentación oficial, en el caso de tener alguna duda con algo de la misma.

### Requisitos (Criterios de selección)
Dado que casi todos los servicios de CI/CD que se encuentran satisfacan los criterios de búsqueda anteriores, entre los seleccionados se evaluarán los siguientes criterios de selección para quedarnos con uno u otro.

- Alta disponibilidad. Se tendrá en cuenta el uptime de cada servicio de CI puesto que los buscamos ya implementados en la nube.
- Bondad del plan gratuito. Se valorará también para cada uno, cuales son las posibilidades del plan gratuito que incluyen, es decir, minutos que ofrece cada uno, usos, características, etc.
- Asistente y ayudas para su configuración. Puesto que es el primer contacto con este tipo de herramientas y sistemas, se tendrá en cuenta los asistentes iniciales para ayuda a los primeros pasos así como de configuración.
