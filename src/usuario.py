from datetime import datetime
from collections import Counter


class Usuario:
    """Usuario de la aplicación SearchCulture.

    Atributos
    ---------
    tipo : int
        Tipo de usuario.
    alta : datetime
        Fecha de alta del usuario en la aplicación.
    region : str
        Región geográfica del usuario.
    intereses : list[str]
        Intereses del usuario como palabras clave.
    conteo : Counter
        Frecuencia absoluta de cada palabra usada por el usuario.
    """

    def __init__(self, tipo, alta, region, intereses, palabras):
        """Constructor de la clase Usuario.

        Parámetros
        ----------
        tipo : int
            Tipo de usuario.
        alta : datetime
            Fecha de alta del usuario en la aplicación.
        region : str
            Región geográfica del usuario.
        intereses : list[str]
            Intereses del usuario como palabras clave.
        palabras : list[str]
            Lista de palabras usadas por el usuario.
        """

        self.tipo = tipo
        self.alta = alta
        self.region = region
        self.intereses = intereses   
        self.conteo = Counter(palabras)
