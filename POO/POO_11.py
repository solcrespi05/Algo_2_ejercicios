"""Definir la clase ExpresionAritmetica, que permita representar constantes
numéricas enteras, operaciones binarias de suma y producto, y operaciones
unarias de negación aritmética, incrementar y decrementar. Toda expresión
deberá poder evaluar el resultado de la expresión, retornando el valor entero
resultante. Definir tantas subclases como posibilidades existan de armar
expresiones aritméticas."""


class ExpresionAritmetica: 
    def __init__(self):
        pass
        
class Suma(ExpresionAritmetica):
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b

    def suma (self):
        return (self.a + self.b)

class Producto(ExpresionAritmetica):
    def __init__(self, a, b):
        super().__init__()
        self.a =a
        self.b = b

    def producto(self):
        return (self.a*self.b)

class Negación(ExpresionAritmetica):
    def __init__(self, a) :
        super().__init__()
        self.a = a
    
    def negación(self):
        return (-self.a)

class Incrementar(ExpresionAritmetica):
    def __init__(self, a):
        super().__init__()
        self.a =a
    
    def incrementar(self):
        return (self.a + 1)


class Decrementar(ExpresionAritmetica):
    def __init__(self, a):
        super().__init__()
        self.a = a

    def decrementar(self):
        return (self.a-1)

#pruebas  
suma_test = Suma(3, 5)
print( suma_test.suma() == 8)

suma_test_neg = Suma(-4, 7)
print(suma_test_neg.suma() == 3)

producto_test = Producto(4, 6)
print( producto_test.producto() == 24)

producto_test_neg = Producto(-3, 7)
print (producto_test_neg.producto() == -21)

negacion_test = Negación(5)
print( negacion_test.negación() == -5)

negacion_test_neg = Negación(-10)
print (negacion_test_neg.negación() == 10)

incrementar_test = Incrementar(7)
print (incrementar_test.incrementar() == 8)

incrementar_test_neg = Incrementar(-3)
print (incrementar_test_neg.incrementar() == -2)

decrementar_test = Decrementar(9)
print (decrementar_test.decrementar() == 8)

decrementar_test_neg = Decrementar(-2)
print (decrementar_test_neg.decrementar() == -3)

