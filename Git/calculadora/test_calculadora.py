import pytest
from calculadora import suma  # Importamos la función desde calculadora.py

# Prueba para la función suma
def test_suma():
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0
    assert suma(0, 0) == 0
    assert suma(3.5, 2.5) == 6.0