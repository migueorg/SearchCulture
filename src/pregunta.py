import itertools


class Pregunta:
    """Pregunta destinada a los usuarios.

    Atributos
    ---------
    id : int
        Identificador único.
    pregunta : str
        Pregunta.
    ponderaciones : diccionario str:str
        Equivalente de cada palabra de la respuesta
    """

    id_iter = itertools.count()
    
    def __init__(self, pregunta, ponderaciones):
        """Constructor de la clase Pregunta.

        Parámetros
        ----------
        pregunta : str
            Pregunta.
        ponderaciones : diccionario str:str
            Equivalente de cada palabra de la respuesta
        """

        self.id = next(Pregunta.id_iter)
        self.pregunta = pregunta
        self.ponderaciones = ponderaciones

    def get_pregunta(self):
        """Getter del atributo pregunta.
        Corresponde con la pregunta que se le hará al usuario."""

        return self.pregunta

    def get_ponderaciones(self):
        """Getter del atributo ponderaciones.
        Corresponde con los valores que se tendrán en cuenta para las palabras que se respondan a esa pregunta."""

        return self.ponderaciones

    def get_ponderacion_concreta(self, palabra):
        """Getter de una ponderación concreta de una palabra.
        Corresponde con el genero equivalente de una palabra en concreto para esa pregunta."""

        valor = 'None'

        if palabra in self.ponderaciones:
            valor = self.ponderaciones[palabra]

        return valor
