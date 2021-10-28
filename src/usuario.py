import datetime


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
    """

    def __init__(self, tipo, alta, region, intereses):
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
        """

        self.tipo = tipo
        self.alta = alta
        self.region = region
        self.intereses = intereses    
