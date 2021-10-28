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
        """Constructor de la clase Pregunta."""

        self.tipo = tipo
        self.pregunta = pregunta
        self.respuestas = respuestas


    def __getitem__(self, i):
        """Permite acceder a los atributos de clase mediante un índice."""

        return [self.tipo, self.pregunta, self.respuestas][i]
