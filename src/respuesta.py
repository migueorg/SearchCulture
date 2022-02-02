class Respuesta:
    """Respuesta de un usuario a una pregunta.

    Atributos
    --------
    respuesta : str
        Respuesta del usuario a la pregunta.
    palabras : list[str]
        Respuesta descompuesta en una lista de palabras individuales
    diccionario : diccionario str:int
        Coleeción de palabras que forman una respuesta almacenada junto con su número de apariciones.
    """

    def __init__(self, respuesta):
        """Constructor de la clase Respuesta.

        Parámetros
        ----------
        respuesta: str
            Respuesta del usuario a la pregunta.
        """

        self.respuesta = respuesta
        self.palabras = ""
        self.diccionario = {}

    def descompone_respuesta(self):
        """Extrae en una lista cada palabra de una respuesta"""

        self.palabras = self.respuesta.split()

    def get_palabras(self):
        """Devuelve el atributo palabras (respuesta separada en palabras individuales)"""
        
        self.descompone_respuesta()
        return self.palabras
    
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
