from datetime import datetime
from collections import Counter
import itertools


class Usuario:
    """Usuario de la aplicación SearchCulture.

    Atributos
    ---------
    id : int
        Identificador único del usuario.
    alta : datetime
        Fecha de alta del usuario en la aplicación.
    region : str
        Región geográfica del usuario.
    intereses : list[str]
        Intereses del usuario como palabras clave.
    conteo : Counter
        Frecuencia absoluta de cada palabra usada por el usuario.
    """

    id_iter = itertools.count()

    def __init__(self, alta, region, intereses, palabras):
        """Constructor de la clase Usuario.

        Parámetros
        ----------
        alta : datetime
            Fecha de alta del usuario en la aplicación.
        region : str
            Región geográfica del usuario.
        intereses : list[str]
            Intereses del usuario como palabras clave.
        palabras : list[str]
            Lista de palabras usadas por el usuario.
        """

        alta = datetime.now()
        self.id = next(Usuario.id_iter)
        self.alta = alta
        self.region = region
        self.intereses = intereses   
        self.conteo = Counter(palabras)
