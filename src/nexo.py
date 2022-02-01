from src.respuesta import Respuesta
from src.pregunta import Pregunta

class Nexo:
    """Enlaza preguntas con respuestas, y calcula las ponderaciones de una respuesta.

    Atributos
    ---------
    pregunta : Pregunta
        Pregunta con la que se trabajará.
    respuesta : Respuesta
        Respuesta con la que se trabajará.
    generos : diccionario str:float
            Genero y puntuación del mismo
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
        self.generos = {'Accion':0.0, 'Drama':0.0, 'Comedia':0.0, 'Sci-fi':0.0}

    def get_pregunta(self):
        """Getter del atributo pregunta.
        Corresponde con el objeto pregunta dado."""

        return self.pregunta

    def get_respuesta(self):
        """Getter del atributo respuesta.
        Corresponde con el objeto respuesta dado."""

        return self.respuesta

    def get_generos(self):
        """Getter del atributo generos.
        Corresponde con los valores calculados para cada genero."""

        return self.generos

    def get_genero_concreto(self, genero):
        """Devuelve el valor de apego calculado para un genero en concreto"""

        return self.generos[genero]
