"""Definir la operación procedimiento pares, que dado un número entero, muestre todos
 los pares de números enteros positivos que son suma del número entero dado. 
 Por ejemplo, 5 = (1 , 4), (2, 3)."""

def pares(n: int, a: int = 1) -> list:
    # Caso base: Si a ya no puede ser menor que n/2, se detiene
    if a >= n:
        return []

    b = n - a
    # Solo considera pares si a es menor que b
    if a < b:
        return [(a, b)] + pares(n, a + 1)
    else:
        return pares(n, a + 1)

print(pares(10))


        
     
