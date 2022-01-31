import respuesta
import pregunta

class Nexo:
    """Enlaza preguntas con respuestas, y calcula las ponderaciones de una respuesta.

    Atributos
    ---------
    pregunta : Pregunta
        Pregunta con la que se trabajará.
    respuesta : Respuesta
        Respuesta con la que se trabajará.
    """
    
    def __init__(self, pregunta, respuesta):
        """Constructor de la clase Nexo.

        Parámetros
        ----------
        pregunta : Pregunta
            Pregunta con la que se trabajará.
        respuesta : Respuesta
            Respuesta con la que se trabajará.
        """

        self.pregunta = pregunta
        self.respuesta = respuesta

