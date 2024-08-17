"""Implementar una función generadora que permita producir todos los números
primos uno a uno.
Nota: Un número es primo si no es divisible por ningún número entre 2 y su raíz
cuadrada."""
from collections.abc import Iterator
import math


def es_primo(n: int) -> bool:
    """Función auxiliar para verificar si un número es primo."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    raiz = int(math.sqrt(n)) + 1
    for i in range(3, raiz, 2):
        if n % i == 0:
            return False
    return True

def generando_primos() -> Iterator[int]:
    numero= 2
    while True: 
        if es_primo(numero):
            yield numero
        numero += 1 

primos = generando_primos()
# Obtener los primeros 10 números primos
for _ in range(10):
    print(next(primos))