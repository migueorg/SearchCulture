# Elección Test Unitarios
***
## Marco de Ejecución
***
### Requisitos (Criterios de búsqueda y selección)
- Comunidad Activa (se tendrá en cuenta la frecuencia con la que hacen commits, fecha de la última versión, cantidad de PR e issues abiertos, forma de contestar ante aportaciones de la comunidad, número de personas que mantienen el proyecto, etc)
- Claridad en los informes de los test (se valorará la salida que nos de al finalizar los test, la facilidad para ver que ha salido bien y que ha salido mal, etc)
- Documentación concisa (se valorarán los ejemplos proporcionados en la documentación, organización de las secciones, la facilidad para buscar dudas o problemas, existencia de FAQ, así como utilidad de la misma)
- Facilidad de uso (se tendrá en cuenta la curva inicial de dificultad para usar el framework, simplicidad para desplegarlo así como la complejidad para añadir los test)


### Opciones Existentes
Las test runners que he encontrado para Python han sido los siguientes:
- [Unittest](https://github.com/python/cpython/tree/main/Lib/unittest)
  - [x] Cumple una comunidad activa pues forma parte de la comunidad oficial de Python. Aunque esto puede ser una desventaja pues el equipo no se dedica exclusivamente a esto sino a Python en general.
  - [ ] No tiene una salida muy amigable, es concreta pero en algunos casos puede generar rechazo por su sintaxis u organización de la misma. Otras alternativas son más claras. Por tanto no cumple este punto.
  - [x] Tiene una documentación bastante concisa, con ejemplos concretos junto con la salida a esperar, unos primeros pasos basntante sencillos y completa, por lo que cumple el requisito de documentación.
  - [x] Al disponer de una documentación y comunidad abundante, así como de librería de aserciones propia, la curva de dificultad inicial es bastante sencilla y rápida. Por lo que si cumple este requisito.
- [Pytest](https://github.com/pytest-dev/pytest) (antiguo [Testify](https://github.com/Yelp/Testify))
  - [x] Cumple con una comunidad activa. De hecho al ser uno de los más conocidos, tiene una gran actividad tanto en issues como en PR, y en medida de lo posible por el gran volumen, se ve como contestan con rápidez y los atienden. Además también tienen una gran cantidad de commits, todos con bastante frecuencia, y que el equipo de desarrollo no está compuesto o mantenido por una sola persona.
  - [x] Dispone de una salida bastante fácil de comprender y rápida de detectar el error, resaltando la línea que provoca el fallo y el motivo de una forma ordenada e intuituva, por lo que si que cumple este requisito.
  - [ ] A pesar de tener una documentación correcta, no tiene ejemplos concretos ni una forma organizada de mostrarla, así como explicaciones suficientes que acompañen a algunos de los ejemplos. Por tanto no cumple este criterio.
  - [x] Los pasos iniciales son bastante simples y rápidos por tanto tiene una curva inicial bastante simple a pesar de una documentación que deja que desear, por lo que si cumple este requisito.
- [Nose2](https://github.com/nose-devs/nose2) (antiguo Nose)
  - [ ] No cumple con mis criterios de tener una comunidad activa, a pesar de que su commit más reciente es de hace 2 días y no tienen muchos issues ni PR abiertos, pero realmente sus commits son de muy cuando en cuando, por lo que se aprecia que el desarrollo va por rachas y no es demasiado activo, y además de esto, solo lo mantiene activo una persona. Por lo que según lo mencionado en los criterios, no lo cumple. 
  - [ ] Como se basa en Unittest, tiene una salida casi idéntica al mismo, por lo que de igual manera no tiene una salida amigable. 
  - [ ] Tiene una mala documentación de cara a gente novata, pocos ejemplos prácticos o supuestos reales, y una muy mala organización.
  - [ ] No tiene para nada un inicio sencillo, el cual se complica por su documentación tan mal organizada y escasa. De hecho de sus primeros comentarios en la documentación es que si eres un usuario novato consideres usar pytest en su lugar.
- [Green](https://github.com/CleanCut/green)
  - [x] Cumple, aunque con un par de peros. Tiene +160 issues cerrados y solo 2 abiertos, de los cuales, ambos atendidos, repitiendo la misma fórmula para los PR así que por esa parte si cumple. Sin emargo lleva sin recibir commits desde julio de 2021, es decir 6 meses desde el último commit en el momento en el que se hace el análisis, lo cual, no está del todo mal, pero además de eso el proyecto está mantenido por una única persona, cosa que no inspira mucha confianza. A pesar de estos peros, como dije al principio, cumple el requisito.
  - [x] Se basa en unittest, pero a diferencia del anterior, este trae añadidos como colorear y mostrar de una forma más clara y visible la salida de los informes, por lo que cubre el requisito a pesar de basarsse en unittest.
  - [ ] Tiene la peor documentación de todas las alternativas vistas, no dispone de web dedicada para la documentación, sino que utiliza el README del repositorio para ello, siendo bastante escueta, mala y sin ejemplos. Tampoco usa la Wiki del propio repositorio, en su lugar te venden [un curso en Udemy](https://www.udemy.com/course/python-testing-with-green/), por lo que no cumple para nada este requisito.
  - [ ] Debido a la mala documentación y poca claridad de la misma, tiene unos primeros pasos bastante complicados, así que tampoco cumple este requisito.
- [Mamba](https://github.com/nestorsalceda/mamba)
  - [ ] No cumple el tener una comunidad activa, de hecho a pesar de no serlo, parece un proyecto abandonado. No tiene commits desde noviembre de 2020, y tiene una gran cantidad de PR e issues abiertos o pendientes en comparación con los cerrados.
  - [ ] A pesar de expresar de una forma adecuada el lugar en el que falla, y el tiempo de ejecución, no da una salida muy amigable o user friendly, sobretodo en comparación con el resto de alternativas, por lo que no cumple este requisito.
  - [ ] Tiene una documentación muy escasa y pobre. Sí que tiene un par de ejemplos concretos de como empezar, pero poco más. Por lo que no cumple este requisito.
  - [x] A pesar de tener una documentación mala, los primeros pasos y el como crear un test simple si está documentado de forma aceptable, por lo que el como empezar no es excesivamente complicado, cumpliendo este requisito. 


### Conclusión 
Tras el análisis de las alternativas encontradas, las herramientas que cumplen más criterios de los que busco son Unittest y Pytest. Ambos cumplen el mismo número de requisitos, pero no los mismos. Por lo que tengo que decidir si priorizar el tener una salida e informe de resultados mejor frente a una documentación mejor estructurada y completa.

Debido a que este es un proyecto simple y pequeño, optaré por Pytest, con el fin de priorizar una salida más elegante, frente a la documentación más concisa y densa. Ya que para el uso que se va a hacer, la documentación de Pytest es más que correcta.

--- 

## Librería de Aserciones
***
### Requisitos
- 1
- 2
- 3

### Opciones Existentes

### Conclusión 