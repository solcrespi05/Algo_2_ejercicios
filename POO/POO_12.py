"""Implemente la clase Hora que contenga miembros datos separados para almacenar
horas, minutos y segundos. Un constructor inicializará estos datos en 0 y otro a valores
dados. Una función miembro deberá visualizar la hora en formato hh:mm:ss. Otra
función miembro sumará dos objetos de tipo hora, retornando la hora resultante.
Realizar otra versión de la suma que asigne el resultado de la suma en el primer objeto
hora.
b) Programar un procedimiento main(), que cree dos horas inicializadas y uno que no lo
esté. Se deberán sumar los dos objetos inicializados, dejando el resultado en el objeto
no inicializado. Por último, se pide visualizar el valor resultante."""

class Hora:
    def __init__(self, hora: int =0, minuto: int = 0, segundo: int = 0):
        self.hora = hora
        self.minuto = minuto 
        self.segundo = segundo

    def __str__(self):
        return f'{self.hora}:{self.minuto}:{self.segundo}'
    
    def sumar (self, otra_hora):
        resultado = Hora()
        
        resultado.segundo = self.segundo + otra_hora.segundo
        resultado.minuto = self.minuto + otra_hora.minuto + resultado.segundo // 60
        resultado.hora = self.hora + otra_hora.hora + resultado.minuto // 60

        resultado.segundo %= 60
        resultado.minuto %= 60
        resultado.hora %= 24 
        
        return resultado
    
    def sumar_asignar(self, otra_hora):
        self.segundo += otra_hora.segundo
        self.minuto += otra_hora.minuto + self.segundo // 60
        self.hora += otra_hora.hora + self.minuto // 60

        self.segundo %= 60
        self.minuto %= 60
        self.hora %= 24

        return self
    
#pruebas
hora1 = Hora(10, 45, 30)
hora2 = Hora(2, 20, 40)
hora3 = Hora()

# Suma y muestra el resultado
resultado = hora1.sumar(hora2)
print("Resultado de la suma en un nuevo objeto:", resultado)

resultado = hora3.sumar(hora1)
print(resultado)

# Suma y asigna el resultado en el primer objeto
hora1.sumar_asignar(hora2)
print("Resultado de la suma asignada al primer objeto:", hora1)







        