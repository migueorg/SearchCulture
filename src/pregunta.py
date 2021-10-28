class Pregunta:
    """Pregunta destinada a los usuarios.

    Atributos
    ---------
    tipo : str
        Tipo de pregunta.
    pregunta : str
        Pregunta.
    respuestas : list[str]
        Posibles respuestas a elegir.
    """

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

        self.tipo = tipo
        self.pregunta = pregunta
        self.respuestas = respuestas
