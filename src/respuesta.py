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

    def __init__(self, id_usuario, id_pregunta, respuesta):
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
        self.diccionario = {}

    def descompone_respuesta2(self, respuesta):
        """Extrae en una lista cada palabra de una respuesta
        
        Parámetros
        ---------
        respuesta : str
            string con la respuesta dada por el usuario.
        """

        self.palabras = respuesta.split()

    def descompone_respuesta(self):
        """Extrae en una lista cada palabra de una respuesta"""

        return self.descompone_respuesta2(self.respuesta)

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


    def almacena_palabras(self):
        """Guarda en un diccionario la palabras de la lista, 
        acompañado del número de apariciones que tiene cada una."""
        diccionario = {}

        for palabra in self.palabras:
            if palabra in diccionario:
                diccionario[palabra] += 1
            else: 
                diccionario[palabra] = 1

        self.diccionario = diccionario

    def get_diccionario(self):
        """Devuelve el diccionario con las palabras de la 
        respuesta y el número de veces que aparecen"""

        self.descompone_respuesta()
        self.almacena_palabras()
        return self.diccionario

    def get_palabra_mas_usada(self):
        """Devuelve la palabra más usada en la respuesta"""

        diccionario = self.get_diccionario()

        veces = 0
        palabra = ''
        for i, j in diccionario.items():
            if veces < j:
                veces = j
                palabra = i

        palabra_mas_usada = palabra

        return palabra_mas_usada

    def get_palabra_concreta(self, palabra):
        """Getter de una palabra concreta de una respuesta.
        Corresponde con el numero de veces que se ha dicho esa palabra."""

        if self.diccionario == {}:
            self.descompone_respuesta()
            self.almacena_palabras()

        valor = 0

        if palabra in self.diccionario:
            valor = self.diccionario[palabra]

        return valor
