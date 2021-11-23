import itertools


class Pregunta:
    """Pregunta destinada a los usuarios.

    Atributos
    ---------
    id : int
        Identificador único.
    pregunta : str
        Pregunta.
    respuestas : list[str]
        Posibles respuestas a elegir.
    """

    id_iter = itertools.count()
    
    def __init__(self, pregunta, respuestas):
        """Constructor de la clase Pregunta.

        Parámetros
        ----------
        pregunta : str
            Pregunta.
        respuestas : list[str]
            Posibles respuestas a elegir.
        """

        self.id = next(Pregunta.id_iter)
        self.pregunta = pregunta
        self.respuestas = respuestas
