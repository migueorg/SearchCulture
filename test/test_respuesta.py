import pytest
from assertpy import assert_that
from src.respuesta import Respuesta

def test_respuesta():
    """Comprueba que la creación de los objetos Respuesta se hacen correctamente"""

    id_usuario = 1
    id_pregunta = 2
    respuesta = "Si que me parece muy muy bien"

    resp = Respuesta(id_usuario,id_pregunta,respuesta)

    assert_that(resp.get_id_usuario()).is_equal_to(id_usuario)
    assert_that(resp.get_id_pregunta()).is_equal_to(id_pregunta)
    assert_that(resp.get_respuesta()).is_equal_to(respuesta)

def test_descompone_respuesta():
    """Comprueba que la descomposición de respuesta a subcadenas de palabras se hace correctamente"""

    respuesta = "Si que me parece muy muy bien"
    resp = Respuesta(0,0,respuesta)

    palabras = resp.get_palabras()

    assert_that(palabras).is_length(7)
    assert_that(palabras).is_equal_to(['Si', 'que', 'me', 'parece', 'muy', 'muy', 'bien'])

def test_almacena_palabras():
    """Comprueba que el almacenaje de las palabras de la respuesta en forma de diccionario funciona correctamente"""

    respuesta = "Si que me parece muy muy bien"
    diccionario_manual = {'Si': 1, 'que': 1, 'me': 1, 'parece': 1, 'muy': 2, 'bien': 1}
    resp = Respuesta(0,0,respuesta)

    assert_that(resp.get_diccionario()).is_equal_to(diccionario_manual)

def test_palabra_mas_usada():
    """Comprueba que la extracción de la palabra más usada se hace correctamente"""

    respuesta = "Si que me parece muy muy bien"
    resp = Respuesta(0,0,respuesta)

    assert_that(resp.get_palabra_mas_usada()).is_equal_to("muy")

def test_palabra_concreta():
    """Comprueba que la extracción de una palabra concreta se hace correctamente"""

    respuesta = "Si que me parece muy muy bien"
    resp = Respuesta(0,0,respuesta)

    assert_that(resp.get_palabra_concreta('parece')).is_equal_to(1)
