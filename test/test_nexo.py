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
    resp = Respuesta(0,0,respuesta)

    nex = Nexo(preg,resp)

    assert_that(nex.get_pregunta()).is_equal_to(preg)
    assert_that(nex.get_respuesta()).is_equal_to(resp)
