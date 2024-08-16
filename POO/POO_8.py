"""Una empresa ferroviaria administra viajes en tren entre dos estaciones terminales de su red.
Un viaje tiene asociado un trayecto (desde una estación terminal de origen a una de destino, con una distancia
determinada y una cantidad de estaciones), una cierta cantidad de vagones y una capacidad máxima de
pasajeros.
También posee qué tipo de viaje corresponde en relación a sus características técnicas, si es un viaje con
tecnología diesel, si es eléctrico o si es de alta velocidad (esto es independiente del trayecto recorrido).
● Viaje diesel: El tiempo de demora promedio -en minutos- es la distancia en kilómetros multiplicada por la
cantidad de estaciones dividido 2 sumada a la cantidad de estaciones y de pasajeros dividido 10.
● Viaje eléctrico: El tiempo de demora promedio -en minutos- es la distancia en kilómetros multiplicada por la
cantidad de estaciones dividido 2.
● Viaje de alta velocidad: El tiempo de demora promedio -en minutos-es la distancia en kilómetros dividido
10.
Definir dentro de la clase Viaje el método tiempoDeDemora, que retorne la cantidad de minutos que tarda en
efectuar su recorrido con las siguientes variantes:
a) Especializando la clase Viaje en función del tipo de viaje.
b) Sin especializar la clase Viaje, relacionándola con la clase TipoDeViaje, que está especializada por cada tipo
de viaje.
"""
#Hice solo el punto a y hasta ahi pq no entendi mucho la consigna

class Viaje :
    def __init__(self, distancia: float, n_estaciones: int, n_pasajeros: int):
        self.distancia =distancia
        self.n_estaciones= n_estaciones
        self.n_pasajeros = n_pasajeros

class Diesel(Viaje):
    def tiempoDeDemora(self):
        return (self.distancia * self.n_estaciones) / 2 + (self.n_estaciones + self.n_pasajeros) / 10
    
class Electrico(Viaje):
    def tiempoDeDemora(self):
        return (self.distancia * self.n_estaciones) / 2 
    
class AltaVelocidad(Viaje):
    def tiempoDeDemora(self):
        return self.distancia/ 10

# Prueba para Viaje Diesel
viaje_diesel = Diesel(distancia=100, n_estaciones=10, n_pasajeros=50)
print(f"Tiempo de demora (Diesel): {viaje_diesel.tiempoDeDemora()} minutos")
# Esperado: (100 * 10) / 2 + (10 + 50) / 10 = 500 + 6 = 506 minutos

# Prueba para Viaje Electrico
viaje_electrico = Electrico(distancia=100, n_estaciones=10, n_pasajeros=50)
print(f"Tiempo de demora (Eléctrico): {viaje_electrico.tiempoDeDemora()} minutos")
# Esperado: (100 * 10) / 2 = 500 minutos

# Prueba para Viaje de Alta Velocidad
viaje_alta_velocidad = AltaVelocidad(distancia=100, n_estaciones=10, n_pasajeros=50)
print(f"Tiempo de demora (Alta Velocidad): {viaje_alta_velocidad.tiempoDeDemora()} minutos")
# Esperado: 100 / 10 = 10 minutos
