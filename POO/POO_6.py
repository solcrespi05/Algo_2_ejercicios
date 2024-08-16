"""Implemente la clase Fecha, que permita representar una terna de día, mes y año,
todos de tipo entero. Programar un método que determine si una fecha es mayor
a otra. Programar la sobrecarga del método __str__ y __gt__(operador mayor)."""
class Fecha: 
    def __init__(self, dia: int, mes: int, año: int):
        self.dia = dia
        self.mes =mes
        self.año = año
    
    def __gt__(self, otra_fecha):
        if self.año > otra_fecha.año:
            return True
        elif self.año < otra_fecha.año:
            return False
        else:
            if self.mes > otra_fecha.mes:
                return True
            elif self.mes < otra_fecha.mes:
                return False
            else: 
                return self.dia > otra_fecha.dia
            
    def __str__(self):
        #return f'Día: {self.dia}, Mes: {self.mes}, Año: {self.año}'
        return f'{self.dia}/{self.mes}/{self.año}'

                
f1 = Fecha(15, 8, 2024)
f2 = Fecha(14, 8, 2024)

print(f1 > f2)  # Debería imprimir: True
print(f1)  # Debería imprimir: 15/08/2024

                
