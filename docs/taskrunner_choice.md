# Elección de Task Runner

## Requisitos
- Simplicidad
- Enfocado a Python
- Rápido
- Limpio
- Buena documentación
- Sencillez en la sintaxis para crear tareas
- Posibilidad de crear tareas que ejecuten más de una orden

## Conclusión 
El proceso de elección de Task Runner para este proyecto ha sido una tarea bastante más densa en el tiempo de lo que me hubiese gustado, habiendo pasado por varias etapas y con ello varias pruebas diferentes que se comentarán a continuación.

Inicialmente se tuvo en cuenta el dúo de Poetry + Invoke pero al ser las más comunes y existir la necesidad de utilizar dos herramientas, se decidió buscar otras alternativas. De dicha búsqueda surgió Pydoit. Al entrar más en detalle, Pydoit parecía una muy buena alternativa, pues era simple, enfocado a Python, rápido y limpio. De hecho su uso era más simple que el de Poetry lo cual fue un motivante importante. Por lo que se empezó el desarrollo de sus tareas específicas (puede verse en commits anteriores).

Una vez se habían construido varias tareas y trasteado más en profundidad con él, se pudo comprobar que efectivamente cumplía el requisito de sencillez en su sintaxis para tareas, y que la documentación a pesar de no ser la más completa o detallada, era correcta y suficiente. Pero entonces surgió un problema bastante importante para mi criterio de selección. Pydoit **no permite** la creación de tareas que ejecuten más de una acción, a excepción de la tarea task_all (la cual ejecuta todas las tareas de golpe). Por lo que si por ejemplo quieres hacer un task_clean que limpie varios directorios, no podrías lanzar dos comandos independientes para cada directorio, tendrías que concatenar los comandos bash con sintaxis del tipo acción1 && acción2. Lo mismo para el task_check_sintaxis, debería juntar todos los comandos en uno solo, lo cual me parece una práctica muy poco elegante y sofisticada, y que a mi juicio, quita bastante sentido a Pydoit como task runner. De hecho buscando en los issues del repositorio oficial de Pydoit, encontré un usuario que como programador, sugería la [posibilidad de ejecutar más de una orden con una misma tarea](https://github.com/pydoit/doit/issues/314), a lo que el desarrollador calificó como invalido y le contestó que si quería ejecutar más de una orden que [crease un script bash y lo lanzase con Poetry](https://github.com/pydoit/doit/issues/314#issuecomment-515147179). Solución que por cierto a mi me parece una guarrada. Es por eso que teniendo ya lista la mayoría de las tareas y documentación lista (visible en commit anteriores, pues he decidido conservarlos), decidí seguir buscando otra alternativa. De aquí surgen nuevos requisitos para futuras elecciones como es la posibilidad de crear tareas que ejecuten más de una orden.

Después de esto, se barajó la posibilidad de usar [PyBuilder](https://github.com/pybuilder/pybuilder), pues a pesar de no ser un task runner como tal, daba bastante juego, pero al revisar su documentación fue descartado rápidamente. No es simple, ni limpio pues involucra bastantes archivos para funcionar, y la documentación no me pareció muy clara de primeras.

Finalmente, encontré [pypyr](https://github.com/pypyr/pypyr), el cual de primeras me pareció que era bastante simple ya que con un simple yaml defines todas las tareas que queiras, haciéndolo de estal forma bastante rápido y limpio. Además de por supuesto enfocado a python. Tras echar un vistazo a su documentación, me pareció una documentación bastante clara, concisa y a la vez completa, con una gran cantidad de ejemplos, además de tener una sintaxis bastante directa por lo que se veía sencilla para crear tareas. Con esto ya teníamos otros dos requisitos satisfechos. Y finalmente, para no caer en el mismo problema que Pydoit, si que permite la ejecución de varias órdenes con una sola tarea, de hecho lo permite de varias formas diferentes. 

Por lo que definitivamente, la elección ha sido de [pypyr](https://github.com/pypyr/pypyr).