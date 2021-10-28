import csv


def to_csv(l, filename):
    """Convierte una lista de objetos en un fichero csv

    Parámetros
    ----------
    l : list
        Lista de objetos a convertir en csv.
    filename : str
        Nombre del fichero de salida.
    """

    # lista de diccionarios y claves
    dics = [object.__dict__ for object in l]
    keys = set().union(*(d.keys() for d in dics))

    # crear csv
    with open(filename, 'w', newline='') as output:
        dict_writer = csv.DictWriter(output, keys)
        dict_writer.writeheader()
        dict_writer.writerows(dics)
