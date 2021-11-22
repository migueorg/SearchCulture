import itertools


class Pregunta:
    """Pregunta destinada a los usuarios.

    Atributos
    ---------
    id : int
        Identificador único.
    tipo : str
        Tipo de pregunta.
    pregunta : str
        Pregunta.
    respuestas : list[str]
        Posibles respuestas a elegir.
    """

    id_iter = itertools.count()
    
    def __init__(self, tipo, pregunta, respuestas):
        """Constructor de la clase Pregunta.

        Parámetros
        ----------
        tipo : str
            Tipo de pregunta.
        pregunta : str
            Pregunta.
        respuestas : list[str]
            Posibles respuestas a elegir.
        """

        self.id = next(Pregunta.id_iter)
        self.tipo = tipo
        self.pregunta = pregunta
        self.respuestas = respuestas
