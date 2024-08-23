"""Adaptar la solución propuesta con recursión mutua para determinar si un número es par o
impar pero permitiendo aceptar también números negativos.
"""
def es_par(n: int) -> bool:
  numero = abs(n)
  return n == 0 or es_impar(numero - 1)

def es_impar(n: int) -> bool:
  numero = abs(n)
  return False if n == 0 else es_par(numero - 1)

print(es_par(-10))   # True
print(es_par(-9))    # False
print(es_impar(4))  # False
print(es_impar(7))  # True