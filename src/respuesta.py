from datetime import datetime


class Respuesta:
    """Respuesta de un usuario a una pregunta.

    Atributos
    --------
    id_usuario : int
        Identificador del usuario que responde.
    id_pregunta : int
        Identificador de la pregunta a la que se responde.
    fecha : datetime
        Fecha en la que se responde a la pregunta.
    respuesta : str
        Respuesta del usuario a la pregunta.
    """

    def _init_(self, id_usuario, id_pregunta, respuesta):
        """Constructor de la clase Pregunta.

        Parámetros
        ----------
        id_usuario : int
            Identificador del usuario que responde.
        id_pregunta : int
            Identificador de la pregunta a la que se responde.
        respuesta: str
            Respuesta del usuario a la pregunta.
        """

        self.id_usuario = id_usuario
        self.id_pregunta = id_pregunta
        self.fecha = datetime.now()
        self.respuesta = respuesta
