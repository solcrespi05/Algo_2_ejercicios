"""Implemente la clase Punto (pares de coordenadas de tipo float x, y). Defina
constructores y métodos para asignar valores a las coordenadas de los puntos,
retornar el valor de cada coordenada, y sumar dos puntos, retornando su
resultado. Definir un método booleano de igualdad entre dos puntos.
"""
class Punto:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def set_x(self, x = 0):
        self.x = x

    def set_y(self, y=0):
        self.y = y
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def __add__ (self, otro_punto):
        return Punto(self.x + otro_punto.x, self.y + otro_punto.y)
    
    def __eq__(self, otro_punto):
        return self.x == otro_punto.x and self.y == otro_punto.y

# Pruebas
p1 = Punto(1.5, 2.5)
p2 = Punto(3.0, 4.0)
p3 = p1 + p2

print(f"Punto 3: ({p3.get_x()}, {p3.get_y()})")  # Debería imprimir: (4.5, 6.5)

print(p1 == p2)  # Debería imprimir: False
p4 = Punto(1.5, 2.5)
print(p1 == p4)  # Debería imprimir: True

        