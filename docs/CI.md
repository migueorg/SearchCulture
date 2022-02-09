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

***
### Opciones Existentes que se van a analizar 
Siguiendo los criterios de búsqueda establecidos previamente, algunos sistemas que se ajustan a lo necesario son:
- [Github Action](https://github.com/features/actions)
- [TravisCI](https://www.travis-ci.com/)
- [Azure Pipelines](https://azure.microsoft.com/es-es/services/devops/pipelines/)
- [Semaphore CI](https://semaphoreci.com/)

**Bonus:** Otras opciones que se han revisiones y pintaban bien pero finalmente no cumplían algunos criterios de búsqueda y por tanto no han llegado al análisis:
- [CircleCI](https://circleci.com/): Además de no poder usarlo porque lo ha usado la mayoría de la gente, [tiene una disponibilidad malísima](https://status.circleci.com/uptime), en comparación con todos los que he comparado, es el peor parado. Todos los meses tiene como mínimo 1 o 2 caídas.
- [codemagic](https://codemagic.io/start/): Pintaba bien y con buenos asistentes, además las imágenes incorporan Docker y Python, pero es un CI/CD demasiado enfocado a desarrollo móvil (Flutter, Swift, React Native, etc), llegando a puntos que es complicado empezar un proyecto que no sea para desarrollo móvil, por lo que es una herramienta que se cierra mucho a un solo sector, lo cual nos puede traer problemas en el futuro.
- [Gitlab CI/CD](https://docs.gitlab.com/ee/ci/): Para poder conectarlo con Github [tienes que ser premium en Gitlab](https://docs.gitlab.com/ee/ci/ci_cd_for_external_repos/github_integration.html).
