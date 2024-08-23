#a. Una función recursiva digitos, que dado un número entero, retorne su cantidad de dígitos.
"""def digitos(numero: int) -> str:
    total = 0
    numero = str(numero)
    for digito in numero:
        total += 1
    print( f'El total de dígitos del número es {total}')
"""
#forma recursiva
def digitos(numero:int):
    if abs(numero)< 10:
        return 1
    else: 
        return 1+ digitos(numero//10)

#b. Una función recursiva reversa_num que, dado un número entero, retorne su imagen especular. Por ejemplo: reversa_num(345) = 543
def reversa_num(numero, resultado=0):
    numero = abs(numero)
    if numero == 0:
        return resultado
    else:
        resultado = resultado * 10 + (numero % 10)
        return reversa_num(numero // 10, resultado)




