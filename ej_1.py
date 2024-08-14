'''Implemente la clase Lamparita, que sirva para representar el estado de encendido
de una lamparita (encendido o apagado). Defina, asimismo, dos métodos que
permitan encender y apagar la luz de la lamparita y otro que indique en qué
estado se encuentra. La lamparita inicialmente está apagada.
'''
class Lamparita:
  def __init__(self, estado = False):
    self.estado = estado
    if self.estado == True:
      print('La lamparita esta encendida')
    else:
      print('La lamparita esta apagada')

  def encendida(self):
    self.estado = True
    print('La lamparita está encendida')

  def apagada (self):
    self.estado = False
    print('La lamparita esta apagada')

  def estado_actual(self):
    if self.estado == True:
      print('La lamparita esta encendida')
    else:
      print('La lamparita esta apagada')

lampara_1= Lamparita()
lampara_2 = Lamparita(True)
lampara_1.encendida()