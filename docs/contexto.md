# User Journey

En la era de la información y el contenido a menudo nos vemos abrumados por la gran cantidad de material de la que disponemos con solo un par de clicks, generando esto un rechazo en gente que no dispone de tiempo para analizar todo el contenido y concluir en que es lo que le podría gustar en cada momento. Por otra parte, debido a las modas pasajeras y la necesidad que tiene la gente por seguirlas, las productoras han perdido el vínculo con sus usuarios de a pie, y desconocen lo que realmente buscan ver en las plataformas, pues ahora mismo solo se consume por moda y no por gusto propio. Finalmente, los servicios que entran al mundillo más tarde que sus competidores veteranos, les cuesta salir de la sombra de su competencia y darse a conocer, por lo que necesitan publicitarse con enlaces referidos a sus plataformas.

Por tanto vemos usuarios modelo como:

- Fran: Trabaja a jornada completa de cara al público, vive solo con su gato y tiene 25 años, por lo que cuando llega a casa solo le apetece consumir material que le haga reír, o que le suba la adrenalina después de un día agotador y monótono. 

- Manuel: Conductor de transporte público en pleno centro de Madrid, una persona muy seria, vive estresado, solo ve la tele mientras cena, en sesiones de no más de 50 minutos, por lo que no quiere nada complicado ni muy agitado. Odia la tecnología.

- David: Estudiante de 4º de la ESO, 16 años, se ha visto todas las recomendaciones de Netflix, le apetece estar de fiesta, pero no le dejan salir, se siente incomprendido y le sobra energía como para estar toda la noche viendo una maratón.

- Juan: Es encargado de la sección de innovación y producción de Netflix España. Se le han acabado las ideas sobre que tipo de contenido nuevo debe crear para los siguientes títulos de Netflix. Revisa Twitter en busca de lo que el público demanda, pero lleva 5 años sacando las mismas conclusiones. Necesita informes sobre los sentimientos y prioridades de la gente que consume ocio para saber que es lo que realmente demanda la gente.

- Pablo: Alto cargo del departamento de marketing de YouTube Music. Nadie quiere usar su plataforma por más que repiten que existe en anuncios de YouTube, por lo que necesita empezar a hacer partnership para que servicios externos enlacen los resultados con URLs a YouTube Music en vez de Spotify.

## Desgranando el User Journey

Del texto anterior podemos sacar tres tipos de usuarios interesados en este proyecto web:

1. Usuario promedio que espera que se le recomienden enlaces a películas, series, música y libros según sus sentimientos, personalidad y estado de ánimo acorde en cada momento, como resultado de contestar preguntas simples, sencillas y sin vocabulario técnico, en el mismo portal en el que está contestando preguntas.
2. Productoras de cine interesadas en perfiles reales y sinceros de usuarios ya que actualmente la gente ve principalmente lo que está de moda y se vuelve más complicado producir contenido que guste y no sea monótono. De esta forma podrían saber que es lo más demandado geográfica y temporalmente.
3. Servicios interesados en conseguir visitas gracias a aparecer su plataforma como recomendada cuando se calcule el contenido para los usuarios finales.

## Traduciendo a HU

Si expresamos las conclusiones anteriores en forma de HUs, nos quedaría de la siguiente forma: 

1. [[HU01]](https://github.com/migueorg/SearchCulture/issues/2) Como usuario promedio quiero obtener recomendaciones de películas, series, libros y música que me vayan a gustar o me apetezca consumir, sin necesidad de conocer títulos ni géneros ni autores, simplemente respondiendo preguntas sobre mi.
2. [[HU02]](https://github.com/migueorg/SearchCulture/issues/3) Como empresa cliente quiero obtener los datos recopilados de los usuarios en formato CSV para que puedan ser tratados por nuestro equipo informático
3. [[HU03]](https://github.com/migueorg/SearchCulture/issues/4) Como empresa cliente quiero ver los datos recopilados representados de forma gráfica, y con un resumen simple de los mismos.
4. [[HU04]](https://github.com/migueorg/SearchCulture/issues/5) Como representante de servicios que ofrecen contenido quiero que mi plataforma sea la predeterminada cuando se devuelva un resultado candidato para consumir por el usuario promedio, para captar de esta forma todas las visitas posibles.

## Productos Finales que se entregarán


1. [[M1]](https://github.com/migueorg/SearchCulture/milestone/6) Módulo de pregunta y recolecta de datos: Base inicial del proyecto, que realizará las preguntas y almacenará los datos que el usuario proporcione.

2. [[M2]](https://github.com/migueorg/SearchCulture/milestone/7) Módulo de procesado de datos: Calculará los porcentajes y ponderaciones de cada respuesta, en busca de resultados acertados usando algoritmos de clustering o similares.
   
3. [[M3]](https://github.com/migueorg/SearchCulture/milestone/8) Sistema de respuesta: Devolverá los resultados que haya obtenido del módulo de cálculo y procesado. Buscará el enlace de dicho resultado en el sistema distribuidor de contenido asociado.

4. [[M4]](https://github.com/migueorg/SearchCulture/milestone/9) Módulo Estadístico Proporcionará un análisis estadístico sencillo (solo a las empresas clientes, nunca a los usuarios finales) de los datos recopilados a los usuarios finales.

## ¿Cómo funciona?

El proyecto lanzará preguntas sobre el estado de ánimo actual, sobre como se siente al realizar determinadas tareas, como reaccionaría a ciertos eventos, y lo que le transmiten algunas supuestas escenas. (La mayoría de preguntas serán de escenas o tópicos sacados de películas. Otras preguntadas serán seleccionadas por las empresas cliente). 

Sobre esas respuestas se sacará un conteo de veces que ha dicho "bien", "mal", "no se", "alegría", "miedo", etc. A las cuales se les dará una determinada ponderación del tipo: "Si a las preguntas sobre la temática X se le han asignado 4 veces "bien" o "alegría" y 1 vez "mal", "miedo", determinamos que el genero Acción le puede gustar en un 80%". Para esto por ejemplo se podría usar un [analizador léxico](http://www.dabeaz.com/ply/) para evaluar estas cadenas, o una simple ponderación por cada repetición de ciertas palabras clave o sus símiles. 

Tras esto, sabremos que géneros cinematográficos son los que generan más rechazo o más interés a ese usuario. Por tanto, usando los resultados sobre el % de cada género, mediante un [algoritmo de clasificación](https://en.wikipedia.org/wiki/Statistical_classification) se recomendará contenido que cumpla esos generos. 