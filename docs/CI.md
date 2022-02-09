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

**Bonus:** Otras opciones que se han revisado y pintaban bien pero finalmente no cumplían algunos criterios de búsqueda y por tanto no han llegado al análisis:
- [CircleCI](https://circleci.com/): Además de no poder usarlo porque lo ha usado la mayoría de la gente, [tiene una disponibilidad malísima](https://status.circleci.com/uptime), en comparación con todos los que he comparado, es el peor parado. Todos los meses tiene como mínimo 1 o 2 caídas.
- [codemagic](https://codemagic.io/start/): Pintaba bien y con buenos asistentes, además las imágenes incorporan Docker y Python, pero es un CI/CD demasiado enfocado a desarrollo móvil (Flutter, Swift, React Native, etc), llegando a puntos que es complicado empezar un proyecto que no sea para desarrollo móvil, por lo que es una herramienta que se cierra mucho a un solo sector, lo cual nos puede traer problemas en el futuro.
- [Gitlab CI/CD](https://docs.gitlab.com/ee/ci/): Para poder conectarlo con Github [tienes que ser premium en Gitlab](https://docs.gitlab.com/ee/ci/ci_cd_for_external_repos/github_integration.html).

***
### Proceso de selección y estudio
A continuación tras haber encontrado varios servicios (y haber descartado bastantes) que se ajustan a los criterios de búsqueda establecidos, voy a pasar a hacer un análisis y comparativa según los criterios de aceptación también previamente establecidos. 

- Github Action
  - [ ] No cumple el requisito de disponibilidad, pues aunque no está a la altura de los malos resultados de CircleCI, todos los meses [tienen varias incidencias con Github Actions](https://www.githubstatus.com/history), si bien es verdad que la mayoría no son graves, y que los suelen resolver rápido, me ha parecido excesivo el número de incidencias que tienen. Se entiende que es debido al gran volumen de tráfico que manejan.
  - [x] Cuenta con [2.000 minutos gratis](https://docs.github.com/en/billing/managing-billing-for-github-actions/about-billing-for-github-actions#included-storage-and-minutes) al mes para cuentas Free. Por lo que cumple este requisito.
  - [ ] A pesar de tener muy buena documentación y muchísimos ejemplos, en cuanto a asistente de iniciación podría ser mejorable (de hecho en el objetivo anterior la lie un poco para añadir la Action al PR pues andaba algo perdido). Si bien es cierto que al venir incorporado en Github, beneficia la curva de dificultad, de primeras te ves algo saturado y perdido en cuanto a como empezar.
- Travis CI
  - [x] Cumple con creces este requisito, pues [tienen un uptime del 100%](https://www.traviscistatus.com/uptime?page=1) en todo 2021 (de hecho me ha sorprendido ese 100%). [La incidencia más grande y reciente](https://www.traviscistatus.com/incidents/813z61sk317x) que han tenido fue en junio de 2021 en la que **algunas** builds dieron problemas.
  - [ ] No cumple este requisito pues ofrece solo 30 días de prueba, una vez pasan, tienes que pagar para seguir usándolo.
  - [ ] Tiene una documentación muy buena y concreta, de hecho me ha sorprendido gratamente, pero no cuenta con asistentes y ayudas para principiantes tan directos como el resto, que es lo que se busca en este requisito. 
- Azure Pipelines
  - [x] Al igual que Travis, cumple con creces este requisito, pues en el último año [no han tenido ninguna caída](https://status.dev.azure.com/_history), y la incidencia menor más reciente fue en octubre y afectaba solo a creación de imágenes de Windows nuevas.
  - [x] Ofrecen 1800 minutos al mes, por lo que cumple el requisito.
  - [x] Satisface el requisito, ya que tiene unos asistentes de bienvenida muy completos y acertados, haciendo que la curva inicial sea lo más baja posible. 
- [Semaphore CI](https://semaphoreci.com/)
  - [x] Cumple este requisito pues a pesar de no tener un uptime del 100% como Travis, [se acerca mucho](https://status.semaphoreci.com/uptime?page=1), y las incidencias que han tenido han sido en su mayoría ralentizaciones. 
  - [ ] No cumple este requisito pues ofrece un crédito inicial de 10$ y una vez los agotas tienes que pagar para poder seguir usándolo.
  - [x] Tiene una interfaz bastante agradable y sencilla, guiándote a través de un tutorial bastante efectivo y con un montón de opciones y ejemplos concretos, muchos de ellos muy acertados, por lo que cumple el requisito. 

Tras el análisis vemos que Azure Pipeline se ajusta perfectamente a lo que buscamos pero tiene un gran problema que no aprecias hasta que ejecutas la primera tarea. Para empezar a usarlo con servidores hosteados por ellos mismos, tienes que rellenar un formulario, el cual tardan 2 a 3 días en aceptar, de lo contrario solo puedes usar entornos self-hosted. Así que tras haber creado las tareas y haber configurado todo para que funcione con Azure Pipelines, tengo que descartarla puesto que no dispongo de esos 2-3 días que tardan en aceptar la solicitud.

***
### Conclusión

> Tras haber analizado las principales alternativas planteadas, siguiendo ambos criterios, tanto búsqueda como aceptación, y teniendo en cuenta la limitación temporal de activación de Azure Pipelines, se han elegido **Travis CI** y **Semaphore CI** como sistemas de CI a implementar en este proyecto.

***
## Elección versiones de Python a testear
***
Para seleccionar que versiones se van a testear, primeramente se analizó el código del proyecto en busca de alguna dependencia en cuanto a estructura o método concreto, que dependa de alguna versión reciente, pero no existía ninguna así.

Lo siguiente que se tuvo en cuenta fue el [estado del mantenimiento y soporte actual](https://endoflife.date/python) de manera oficial. De lo cual pude obtener que a día de hoy son mantenidas las versiones 3.7 (a la cual le queda 1 año y 4 meses de soporte) en adelante. Por lo que ahora mismo tendría como versiones a testear las siguientes: [3.7, 3.8, 3.9, 3.10]

Con el fin de acotar más aún las versiones de python compatibles, se analizó también la compatibilidad de las dependencias externas del proyecto, en este caso, pypyr, assertpy y pytest. De lo cual obtuve:

- pypyr: Compatible con Python [3.7, 3.8, 3.9, 3.10], o más que compatible, son en las versiones en las que ellos lo testean y aseguran que va a funcionar.
- assertpy: Compatible con Python [3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 3.10]
- pytest: Compatible con Python [3.6, 3.7, 3.8, 3.9, 3.10]

>Con todo esto en cuenta, siendo los limitantes el soporte y la compatibilidad con pypyr, las versiones compatibles con mi proyecto y por tanto las que testearé son [3.7, 3.8, 3.9, 3.10]

>Sin embargo con la imagen Docker creada en el Objetivo 5, ya se está testeando la versión de Python 3.9, por lo que en uno de los sistemas de CI se testearán Python [3.7, 3.8 y 3.10]