import pytest
from assertpy import assert_that
from src.pregunta import Pregunta

def test_pregunta():
    """Comprueba que la creación de los objetos Pregunta se hacen correctamente"""

    pregunta = "¿Que te transmite el final de Titanic?"
    ponderaciones = {'aburrimiento': 'Accion', 'pena': 'Drama', 'lastima': 'Drama', 'predecible': 'Sci-fi'}

    preg = Pregunta(pregunta,ponderaciones)

    assert_that(preg.get_pregunta()).is_equal_to(pregunta)
    assert_that(preg.get_ponderaciones()).is_equal_to(ponderaciones)

def test_ponderacion_concreta():
    """Comprueba que la obtención de elementos concretos de las ponderaciones se hacen correctamente"""

    pregunta = "¿Que te transmite el final de Titanic?"
    ponderaciones = {'aburrimiento': 'Accion', 'pena': 'Drama', 'lastima': 'Drama', 'predecible': 'Sci-fi'}

    preg = Pregunta(pregunta,ponderaciones) 
    assert_that(preg.get_ponderacion_concreta('aburrimiento')).is_equal_to('Accion')
    assert_that(preg.get_ponderacion_concreta('coche')).is_equal_to('None')
