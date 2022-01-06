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
        """Constructor de la clase Respuesta.

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
        self.palabras = ""

    def descompone_respuesta(self, respuesta):
        """Extrae en una lista cada palabra de una respuesta
        
        Parámetros
        ---------
        respuesta : str
            string con la respuesta dada por el usuario.
        """

        self.palabras = respuesta.split()

    def descompone_respuesta(self):
        """Extrae en una lista cada palabra de una respuesta"""

        return self.descompone_respuesta(self.respuesta)

    def get_palabras(self):
        """Devuelve el atributo palabras"""

        self.descompone_respuesta()
        return self.palabras

    def get_id_usuario(self):
        """Getter del atributo id_usuario.
        Corresponde con el usuario que hizo la respuesta."""

        return self.id_usuario

    def get_id_pregunta(self):
        """Getter del atributo id_pregunta.
        Corresponde con la pregunta que se está contestando."""

        return self.id_pregunta
    
    def get_respuesta(self):
        """Getter del atributo respuesta.
        Corresponde con lo que se haya contestado a la pregunta."""

        return self.respuesta


    def almacena_palabras(palabras):
        """Guarda en un diccionario la palabras de la lista, 
        acompañado del número de apariciones que tiene cada una.

        Parámetros
        ---------
        palabras : list[str]
            Respuesta previamente descompuesta.
        """
        diccionario = {}

        for palabra in palabras:
            if palabra in diccionario:
                diccionario[palabra] += 1
            else: 
                diccionario[palabra] = 0

        return diccionario