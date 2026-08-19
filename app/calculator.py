# app/calculator.py

def sumar(a: float, b: float) -> float:
    """Retorna la suma de dos numeros."""
    return a + b

def restar(a: float, b: float) -> float:
    """Retorna la resta de dos numeros."""
    return a - b

def multiplicar(a: float, b: float) -> float:
    """Retorna la multiplicacion de dos numeros."""
    return a * b

def dividir(a: float, b: float) -> float:
    """Retorna la division de dos numeros. Lanza ValueError si se divide entre 0."""
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b

def es_par(numero: int) -> bool:
    """Determina si un numero entero es par."""
    return numero % 2 == 0
