# Elección Test Unitarios
***
## Marco de Ejecución
***
### Requisitos (Criterios de búsqueda y selección)
- Comunidad Activa (se tendrá en cuenta la frecuencia con la que hacen commits, fecha de la última versión, cantidad de PR e issues abiertos, forma de contestar ante aportaciones de la comunidad, número de personas que mantienen el proyecto, etc)
- Claridad en los informes de los test (se valorará la salida que nos dé al finalizar los test, la facilidad para ver que ha salido bien y que ha salido mal, etc)
- Documentación concisa (se valorarán los ejemplos proporcionados en la documentación, organización de las secciones, la facilidad para buscar dudas o problemas, existencia de FAQ, así como utilidad de la misma)
- Facilidad de uso (se tendrá en cuenta la curva inicial de dificultad para usar el framework, simplicidad para desplegarlo así como la complejidad para añadir los test)
- Debe tener la posibilidad de usar fixtures, pues aunque no se vayan a usar de momento, es un añadido que en el futuro puede ser útil para poder simular contextos o situaciones específicas para testear comportamientos concretos de forma cómoda y rápida.


### Opciones Existentes
Los test runners que he encontrado para Python han sido los siguientes:
- [Pytest](https://github.com/pytest-dev/pytest) (antiguo [Testify](https://github.com/Yelp/Testify))
  - [x] Cumple con una comunidad activa. De hecho al ser uno de los más conocidos, tiene una gran actividad tanto en issues como en PR, y en medida de lo posible por el gran volumen, se ve como contestan con rapidez y los atienden. Además, también tienen una gran cantidad de commits, todos con bastante frecuencia, y el equipo de desarrollo no está compuesto o mantenido por una sola persona.
  - [x] Dispone de una salida bastante fácil de comprender y rápida de detectar el error, resaltando la línea que provoca el fallo y el motivo de una forma ordenada e intuitiva, por lo que sí que cumple este requisito.
  - [ ] A pesar de tener una documentación correcta, no tiene ejemplos concretos ni una forma organizada de mostrarla, así como explicaciones suficientes que acompañen a algunos de los ejemplos. Por tanto, no cumple este criterio.
  - [x] Los pasos iniciales son bastante simples y rápidos, por tanto, tiene una curva inicial bastante simple a pesar de una documentación que deja que desear, por lo que si cumple este requisito.
  - [x] [Soporta el uso de fixtures](https://docs.pytest.org/en/latest/explanation/fixtures.html), por lo que si cumple este requsito. 
- [Nose2](https://github.com/nose-devs/nose2) (antiguo Nose)
  - [ ] No cumple con mis criterios de tener una comunidad activa, a pesar de que su commit más reciente es de hace 2 días y no tienen muchos issues ni PR abiertos, pero realmente sus commits son de muy cuando en cuando, por lo que se aprecia que el desarrollo va por rachas y no es demasiado activo, y además de esto, solo lo mantiene activo una persona. Por lo que según lo mencionado en los criterios, no lo cumple. 
  - [ ] Como se basa en Unittest, tiene una salida casi idéntica al mismo, por lo que de igual manera no tiene una salida amigable. 
  - [ ] Tiene una mala documentación de cara a gente novata, pocos ejemplos prácticos o supuestos reales, y una muy mala organización.
  - [ ] No tiene para nada un inicio sencillo, el cual se complica por su documentación tan mal organizada y escasa. De hecho de sus primeros comentarios en la documentación es que si eres un usuario novato consideres usar pytest en su lugar.
  - [x] [Permite el uso de fixtures](https://docs.nose2.io/en/latest/plugins/layers.html?highlight=fixtures#organizing-test-fixtures-into-layers) mediante lo que ellos llaman plugins. Por lo que si cumple este requisito. 
- [Green](https://github.com/CleanCut/green)
  - [x] Cumple, aunque con un par de peros. Tiene +160 issues cerrados y solo 2 abiertos, de los cuales, ambos atendidos, repitiendo la misma fórmula para los PR así que por esa parte si cumple. Sin embargo, lleva sin recibir commits desde julio de 2021, es decir 6 meses desde el último commit en el momento en el que se hace el análisis, lo cual, no está del todo mal, pero además de eso el proyecto está mantenido por una única persona, cosa que no inspira mucha confianza. A pesar de estos peros, como dije al principio, cumple el requisito.
  - [x] Se basa en unittest, pero a diferencia del anterior, este trae añadidos como colorear y mostrar de una forma más clara y visible la salida de los informes, por lo que cubre el requisito a pesar de basarse en unittest.
  - [ ] Tiene la peor documentación de todas las alternativas vistas, no dispone de web dedicada para la documentación, sino que utiliza el README del repositorio para ello, siendo bastante escueta, mala y sin ejemplos. Tampoco usa la Wiki del propio repositorio, en su lugar te venden [un curso en Udemy](https://www.udemy.com/course/python-testing-with-green/), por lo que no cumple para nada este requisito.
  - [ ] Debido a la mala documentación y poca claridad de la misma, tiene unos primeros pasos bastante complicados, así que tampoco cumple este requisito.
  - [ ] Al igual que en el requisito anterior, debido a la mala documentación que tienen, ha sido sido dificil averiguar si es compatible con fixtures, pero finalmente se ha llegado a la conclusión de que no lo es, ya que no aparece nada al respecto en su documentación visible gratuita (desconozco si en su curso de pago los mencionarán), y además un usuario en un issue [menciona que con fixtures sería facil de hacer](https://github.com/CleanCut/green/issues/60#issuecomment-112241525), de lo que deduzco que no los soportan. Por lo que no cumple este requisito
- [Mamba](https://github.com/nestorsalceda/mamba)
  - [ ] No cumple el tener una comunidad activa, de hecho a pesar de no serlo, parece un proyecto abandonado. No tiene commits desde noviembre de 2020, y tiene una gran cantidad de PR e issues abiertos o pendientes en comparación con los cerrados.
  - [ ] A pesar de expresar de una forma adecuada el lugar en el que falla, y el tiempo de ejecución, no da una salida muy amigable o user friendly, sobre todo en comparación con el resto de alternativas, por lo que no cumple este requisito.
  - [ ] Tiene una documentación muy escasa y pobre. Sí que tiene un par de ejemplos concretos de como empezar, pero poco más. Por lo que no cumple este requisito.
  - [x] A pesar de tener una documentación mala, los primeros pasos y el cómo crear un test simple si está documentado de forma aceptable, por lo que el cómo empezar no es excesivamente complicado, cumpliendo este requisito. 
  - [ ] No es compatible con el uso de fixtures, ya que en su documentación oficial no hay ni mención sobre como implementarlos. Por lo que no cumple este requisito.


### Conclusión 
Tras un correcto análisis de los posibles test runners encontrados, vemos que pocos de ellos cumplen varios de los requisitos establecidos, siendo Pytest el que más cumple de todos, por lo que ha sido el elegido finalmente a pesar de no cumplir el 100% de los requisitos.

Adicionalmente aún así, a pesar de no haber pasado el requisito de tener una documentación bien organizada o con suficientes ejemplos, para el uso que se va a utilizar en este proyecto, es más que suficiente.

--- 

## Biblioteca de Aserciones
***
### Requisitos
- Sintaxis Intuitiva (se tendrá en cuenta, con bastante importancia, la forma de crear aserciones, si tiene una sintaxis simple, sencilla y similar al lenguaje natural)
- Comunidad Activa (igual que lo que comenté para el marco de ejecución)
- Documentación Suficiente (también en la misma tónica que para el requisito del marco de ejecución, debe de tener una documentación clara. No por ser más extensa debe ser mejor, se valorará lo clara que sea y lo seccionada que esté, así como temas que aborde en la misma y la utilidad que tenga para este proyecto)

### Opciones Existentes
Las bibliotecas de aserciones que he encontrado tras varias búsquedas han sido:
- [Verify](https://github.com/dgilland/verify)
  - [x] Cumple el requisito de sintaxis intuitiva pues trata de componer los comprobantes de una forma bastante natural a como lo haríamos mentalmente.
  - [ ] No cumple con una comunidad activa pues lleva desde 2017 sin actividad en el repositorio, ya sea por parte del owner como por parte de la comunidad.
  - [ ] No tiene una buena documentación, ya que casi no tiene un simple tutorial de primeros pasos, y el que tiene es un copia y pega del README del repo. 
- [AssertPy](https://github.com/assertpy/assertpy)
  - [x] Tiene una sintaxis fácil de entender, aunque no tan buena como Grapa o PyTruth, pero lo suficiente natural y simple como para cumplir el requisito.
  - [x] A pesar de que es mantenido por una sola persona, y no es muy rápida contestando issues, sigue activa y con mantenimiento. Su último commit es de agosto de 2021. Por lo que viendo el mantenimiento que recibe el resto de bibliotecas, sí que podemos decir que es activa.
  - [x] Tiene una documentación bastante buena y completa, con muchos ejemplos reales y concisos. Además, está bien organizada, por lo que cumple el requisito. De hecho en este aspecto es el mejor de todos.
- [PyTruth](https://github.com/google/pytruth)
  - [x] Es uno de los que mejor cumple este requisito, teniendo una sintaxis muy intuitiva y natural.
  - [ ] No es un proyecto con mantenimiento activo, por tanto, no proporcionan soporte, y no aceptan issue ni PR. Lo cual lo descarta totalmente de este análisis.
  - [ ] No tiene documentación como tal, aunque el README es bastante completo.
- [Grappa](https://github.com/grappa-py/grappa)
  - [x] Cumple con creces el requisito de sintaxis intuitiva. Es de todos los encontrados el que más se parece a la forma de hablar natural, siendo esta la principal de las motivaciones de su proyecto.
  - [ ] No tiene actividad desde noviembre de 2020 por lo que no cumple con una comunidad activa. Además, en los últimos issues uno de los owners comentó que estaba bastante ocupado y que no podía atenderlo en ese momento, dejando el trabajo para otro de los miembros.
  - [x] A pesar de no tener una documentación demasiado buena en comparación con otras, sí que es muy concisa y concreta, tiene ejemplos muy bien seleccionados y claros, siendo de gran utilidad para este proyecto.
- [unittest](https://github.com/python/cpython/tree/main/Lib/unittest)
  - [ ] No cumple el requisito pues tiene una sintaxis bastante arcaica, obsoleta, repetitiva y poco natural, haciendo que sea liosa. (En comparación con el resto de librerías de aserciones enfocadas con una sintaxis más natural y humana)
  - [x] Tiene una comunidad activa pues lo mantiene el propio equipo de Python al ser una parte del mismo, aunque eso a su vez hace que cueste encontrar como buscar algún PR o issue que hable de esta biblioteca de aserciones.
  - [x] Sí que tiene una documentación bastante explicita y con ejemplos, además al ser tan popular y conocida, hay una cantidad muy grande de páginas con ejemplos y tutoriales de terceros, etc.
### Conclusión 

Tras el análisis la única biblioteca que cumple todos los requisitos es AssertPy. Por lo que esa es la elegida para el proyecto.

Comentar que de no ser por la sensación de abandono que tiene Grappa, la opción elegida habría sido Grappa pues a nivel de sintaxis es más intuitivo.
***

# Principios F.I.R.S.T.

FIRST es el acrónimo de las cinco características que deben tener nuestros tests unitarios para ser considerados tests con calidad:

- [x] Fast (rápido): Esta característica se cumple pues los test se pasan en 0.04s 
  ![Prueba ejecución test](/docs/imgs/ejecucion_test.png)
- [x] Independent (independiente): Se cumple porque para los 3 test se crea un objeto Respuesta nuevo e independiente que no depende del anterior.

- [x] Repeatable (repetible): También se cumple pues no tienen dependencias de servidores externos ni de información de terceros. Toda la información necesaria viene implementada en los propios test.
- [x] Self-validating (auto evaluable): Se ejecutan automáticamente al lanzar la tarea de test en el task runner y expresan el resultado válido o inválido al terminar los mismos.
- [x] Timely (oportuno): Los test se han pensado antes que el desarrollo del código. Aunque no se vea reflejado en el orden de los commits, el desarollo si que ha cumplido dicho principio, pues el código se ha hecho pensando en pasar los test previamente establecidos.

***
# Aclaración sucedido con unittest

En la revisión anterior tuve un desliz relacionado con unittest, ya que lo había clasificado como test runner y como librería de aserciones a la vez. Esto fue debido a que en la documentación oficial y en múltiples sitios que hablan de unittest, lo denominan como un [framework de unit testing](https://docs.python.org/3/library/unittest.html#module-unittest), y destacan la posibilidad de usar unittest para [construir y correr test](https://docs.python.org/3/library/unittest.html#basic-example). Pero efectivamente, tras la revisión y comentarios de JJ he podido cerciorarme de que unittesting NO es un test runner, a pesar de que la forma de mencionarlo y hablar de él en webs y documentación oficial sea tan abstracta, ya que realmente es una librería de aserciones con ciertos añadidos para test, por lo cual pasa a llamarse test framework. Pero esto no lo convierte en un test runner, ya que unittest NO interpreta la salida de los ficheros de testeo, ni es capaz de buscar dichos ficheros de testeo, entre otros.

Por lo que tras esto, se ha eliminado unittest del proceso de selección de test runner y se ha mantenido en el de librería de aserciones.
