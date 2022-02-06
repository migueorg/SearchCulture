import pytest
from assertpy import assert_that

from src.pregunta import Pregunta
from src.respuesta import Respuesta
from src.nexo import Nexo

def test_nexo():
    """Comprueba que la creación de los objetos Nexo se hacen correctamente"""
    
    #En futuras versiones es conveniente usar fixtures para la creación de estos objetos
    pregunta = "¿Que te transmite el final de Titanic?"
    ponderaciones = {'aburrimiento': 'Accion', 'pena': 'Drama', 'lastima': 'Drama', 'predecible': 'Sci-fi', 'sueño': 'Accion'}
    preg = Pregunta(pregunta,ponderaciones)

    respuesta = "Mucho aburrimiento y sueño"
    resp = Respuesta(respuesta)

    nex = Nexo(preg,resp)

    assert_that(nex.get_pregunta()).is_equal_to(preg)
    assert_that(nex.get_respuesta()).is_equal_to(resp)

def test_generos():
    """Comprueba que el trabajo con los generos se hacen correctamente"""

    #En futuras versiones es conveniente usar fixtures para la creación de estos objetos
    pregunta = "¿Que te transmite el final de Titanic?"
    ponderaciones = {'aburrimiento': 'Accion', 'pena': 'Drama', 'lastima': 'Drama', 'predecible': 'Sci-fi', 'sueño': 'Accion'}
    preg = Pregunta(pregunta,ponderaciones)

    respuesta = "Mucho aburrimiento y sueño"
    resp = Respuesta(respuesta)

    nex = Nexo(preg,resp)
    generos_vacio = {'Accion':0.0, 'Drama':0.0, 'Comedia':0.0, 'Sci-fi':0.0}

    assert_that(nex.get_generos()).is_equal_to(generos_vacio)
    assert_that(nex.get_genero_concreto('Accion')).is_equal_to(0.0)

def test_calculos():
    """Comprueba que los calculos sobre los generos  en base a la pregunta y respuesta se hacen correctamente"""

    #En futuras versiones es conveniente usar fixtures para la creación de estos objetos
    pregunta = "¿Que te transmite el final de Titanic?"
    ponderaciones = {'aburrimiento': 'Accion', 'pena': 'Drama', 'lastima': 'Drama', 'predecible': 'Sci-fi', 'sueño': 'Accion'}
    preg = Pregunta(pregunta,ponderaciones)

    respuesta = "Mucho aburrimiento y sueño"
    resp = Respuesta(respuesta)

    nex = Nexo(preg,resp)
    generos_vacio = {'Accion':0.0, 'Drama':0.0, 'Comedia':0.0, 'Sci-fi':0.0}

    nex.calcula_generos()
    assert_that(nex.get_generos()).is_not_equal_to(generos_vacio)
    assert_that(nex.get_genero_concreto('Accion')).is_greater_than(0.0)
    assert_that(nex.get_genero_concreto('Accion')).is_less_than(3.0)
