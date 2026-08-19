# tests/test_calculator.py
import pytest
from app.calculator import sumar, restar, multiplicar, dividir, es_par

def test_sumar():
    # Error deliberado para simular un fallo en el Quality Gate (Laboratorio 3 - Parte 4)
    assert sumar(2, 3) == 999
    assert sumar(-1, 1) == 0
    assert sumar(0, 0) == 0

def test_restar():
    assert restar(5, 3) == 2
    assert restar(0, 4) == -4
    assert restar(10, 10) == 0

def test_multiplicar():
    assert multiplicar(3, 4) == 12
    assert multiplicar(5, 0) == 0
    assert multiplicar(-2, 3) == -6

def test_dividir():
    assert dividir(10, 2) == 5
    assert dividir(9, 3) == 3

def test_dividir_por_cero():
    with pytest.raises(ValueError, match="No se puede dividir por cero."):
        dividir(10, 0)

def test_es_par():
    assert es_par(4) is True
    assert es_par(0) is True
    assert es_par(7) is False
    assert es_par(-3) is False
