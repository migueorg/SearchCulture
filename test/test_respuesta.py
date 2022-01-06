import pytest
from assertpy import assert_that
from src.respuesta import Respuesta

#Comprueba que la creación de los objetos Respuesta se hacen correctamente
def test_respuesta():
    id_usuario = 1
    id_pregunta = 2
    respuesta = "Si que me parece muy muy bien"

    resp = Respuesta(id_usuario,id_pregunta,respuesta)

    assert_that(resp.get_id_usuario()).is_equal_to(id_usuario)
    assert_that(resp.get_id_pregunta()).is_equal_to(id_pregunta)
    assert_that(resp.get_respuesta()).is_equal_to(respuesta)

#Comprueba que la descomposición de respuesta a subcadenas de palabras se hace correctamente
def test_descompone_respuesta():
    respuesta = "Si que me parece muy muy bien"
    resp = Respuesta(0,0,respuesta)

    palabras = resp.get_palabras()

    assert_that(palabras).is_length(7)
    assert_that(palabras).is_equal_to(['Si', 'que', 'me', 'parece', 'muy', 'muy', 'bien'])

#Comprueba que el almacenaje de las palabras de la respuesta en forma de diccionario funciona correctamente
def test_almacena_palabras():
    respuesta = "Si que me parece muy muy bien"
    diccionario_manual = {'Si': 1, 'que': 1, 'me': 1, 'parece': 1, 'muy': 2, 'bien': 1}
    resp = Respuesta(0,0,respuesta)

    assert_that(resp.get_diccionario()).is_equal_to(diccionario_manual)
