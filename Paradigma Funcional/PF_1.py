"""Ejercicio: Función de orden superior
1)Implementar una función llamada wrapper que reciba por parámetro a otra función f sin
argumentos, la ejecute e imprima en pantalla el mensaje de ejecución: "Ejecutada f()".
2)Extender la función wrapper de forma que pueda aceptar cualquier función con
argumentos variables y se puedan pasar también desde la función wrapper para que se
invoquen en f. Por ejemplo, si f acepta 3 argumentos, éstos deberían también pasarse a
wrapper para que se invoque f(arg1, arg2, arg3) dentro.
TIP: Ver el type hint Callable.
TIP 2: Ver pasaje de argumentos con *args y **kwargs
"""
from typing import Callable, Any

def wrapper (f: Callable[..., Any], *args: Any, **kwargs: Any):
    f(*args, **kwargs)
    print (f'Ejecutada {f}()')

#prueba
def hola(nombre):
    print( f'Hola {nombre}')

wrapper(hola, 'Sol')
