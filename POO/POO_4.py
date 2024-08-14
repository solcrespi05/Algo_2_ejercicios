''' ejercicio restaurantes Delicias del Mar'''
class Restaurante:
  contador_sucursales = 0
  def __init__(self, nombre, ciudad, cant_empleados):
    self.nombre = nombre
    self.ciudad = ciudad
    self.cant_empleados = cant_empleados
    Restaurante.contador_sucursales += 1

  @classmethod
  def obtener_numero_sucursales(cls):
    return  cls.contador_sucursales

  def calcular_costo_operativo(self, empleado_promedio = 2000):
    costo_operativo = self.cant_empleados * empleado_promedio
    return f'El costo operativo de la sucursal {self.nombre} es de {costo_operativo}, el detalle es el producto de la cantidad de empleados: {self.cant_empleados} y el salario promedio mensual por empleado: {empleado_promedio}'

Restaurante.contador_sucursales = 0

# Crear instancias de la clase Restaurante
restaurante1 = Restaurante("Delicias del Mar - Sucursal 1", "Ciudad A", 30)
restaurante2 = Restaurante("Delicias del Mar - Sucursal 2", "Ciudad B", 25)
restaurante3 = Restaurante("Delicias del Mar - Sucursal 3", "Ciudad C", 40)

# Verificar que los restaurantes se crearon correctamente
print(restaurante1.nombre == "Delicias del Mar - Sucursal 1")  # Debería ser True
print(restaurante1.ciudad == "Ciudad A")  # Debería ser True
print(restaurante1.cant_empleados == 30)  # Debería ser True

# Verificar el número de sucursales creadas
print(Restaurante.obtener_numero_sucursales() == 3)  # Debería ser True, ya que hemos creado 3 sucursales

# Calcular el costo operativo de cada sucursal
print(restaurante1.calcular_costo_operativo())  # Debería calcular el costo operativo con el salario promedio por defecto de 2000
print(restaurante2.calcular_costo_operativo(2500))  # Debería calcular el costo operativo con un salario promedio de 2500
print(restaurante3.calcular_costo_operativo(1800))  # Debería calcular el costo operativo con un salario promedio de 1800