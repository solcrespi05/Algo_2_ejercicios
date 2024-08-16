"""a) Crear una clase Vehiculo con los siguientes atributos y métodos:
● Atributos:
○ marca (String)
○ modelo (String)
○ precioBase (double).
● Métodos:
○ Un constructor que acepte la marca, modelo y precio base del vehículo.
○ Un método calcularCostoAlquiler(int dias) que calcule el costo de alquiler del vehículo
durante el número de días especificado. El costo se calcula como precioBase * dias.
b) Crear dos subclases Auto y Moto, que hereden de la clase Vehiculo. Las subclases deben incluir
un constructor que llame al constructor de la superclase y también deben sobrescribir el método
calcularCostoAlquiler(int dias) de la siguiente manera:
● Para Auto, el costo de alquiler se calcula incrementando un 20% el costo común.
● Para Moto, el costo de alquiler se calcula con un descuento del 15% respecto al vehículo.
"""
class Vehiculo:
    def __init__(self, marca: str, modelo: str, precioBase: float):
        self.marca = marca
        self.modelo = modelo
        self.precioBase = precioBase
    
    def calcularCostoAlquiler(self, dias: int) -> float:
        costo = self.precioBase * dias
        return f'El Costo del Alquiler por el vehiculo de la marca: {self.marca}, modelo: {self.modelo}, por la cantidad de {dias} días es: ${costo}'

    def __str__(self) -> str:
        return f'El vehiculo de la marca {self.marca}, modelo: {self.modelo}. tiene un precio base de ${self.precioBase}'
    

class Auto(Vehiculo):
    def __init__(self, marca: str, modelo: str, precioBase: float):
        super().__init__(marca, modelo, precioBase)
    
    def calcularCostoAlquiler(self, dias: int) -> float: 
        costo = (self.precioBase * 1.2) * dias
        return f'El Costo del Alquiler por el auto de la marca: {self.marca}, modelo: {self.modelo}, por la cantidad de {dias} días es: ${costo}'

class Moto(Vehiculo):
    def __init__(self, marca: str, modelo: str, precioBase: float):
        super().__init__(marca, modelo, precioBase)

    def calcularCostoAlquiler(self, dias: int) -> float:
        costo = (self.precioBase * 0.85) * dias
        return f'El Costo del Alquiler por la moto de la marca: {self.marca}, modelo: {self.modelo}, por la cantidad de {dias} días es: ${costo}'

    
# Ejemplo de uso:
auto = Auto("Toyota", "Corolla", 1000)
moto = Moto("Yamaha", "MT-07", 700)

print(auto)
print(auto.calcularCostoAlquiler(5))

print(moto)
print(moto.calcularCostoAlquiler(5))

