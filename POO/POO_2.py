'''Implemente una clase Monedero que permita gestionar la cantidad de dinero que
una persona dispone en un momento dado. La clase deberá tener un constructor
que permitirá crear un monedero con una cantidad de dinero inicial y deberá
definir un método para meter dinero en el monedero, otro para sacarlo y
finalmente, otro para consultar el disponible; solo podrá conocerse la cantidad de
dinero del monedero a través de este último método. Por supuesto, no se podrá
sacar más dinero del que haya en un momento dado en el monedero.
'''

class Monedero:
  def __init__(self, dinero_inicial):
    self.dinero = dinero_inicial

  def meter_dinero(self, cantidad):
    self.dinero += cantidad

  def sacar_dinero(self, cantidad):
    if cantidad > self.dinero:
      print('No tiene esa suma de dinero en el monedero')
    else:
      self.dinero -= cantidad

  def consultar_monto(self):
    return f'El dinero actual de la cuenta es: {self.dinero}'


monedero = Monedero(6000)
monedero.consultar_monto()
monedero.meter_dinero(50)
monedero.sacar_dinero(7000)
