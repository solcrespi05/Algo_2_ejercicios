'''ejercicio cadena restaurantes
'''
class Producto:
  def __init__(self, nombre, precio_unitario, cantidad_inicial_stock):
    self.nombre = nombre
    self.precio_unitario = precio_unitario
    self.stock = cantidad_inicial_stock

  def actualizar_stock(self, cantidad_vendida):
    if cantidad_vendida > self.stock:
      return f'No hay esa cantidad de stock de {self.nombre}'
    else:
      self.stock -= cantidad_vendida
      return f'El stock actual de {self.nombre} es {self.stock}'


class Pedido:
  contador_pedidos = 0
  def __init__ (self):
    self.lista_productos = []
    self.estado = "En preparación"
    Pedido.contador_pedidos += 1
    self.id = Pedido.contador_pedidos

  def agregar_producto(self, producto, cantidad):
    if self.estado == 'En preparación':
      if cantidad > producto.stock:
        return f'No se pudo cargar el producto por falta de stock'
      else:
        self.lista_productos.append((producto, cantidad))
        producto.actualizar_stock(cantidad)
    else:
      return 'No se pueden agregar más productos, ya que el pedido está entregado'

  def calcular_total(self, descuento=0.10):
    total = 0
    for producto, cantidad in self.lista_productos:
        total += cantidad * producto.precio_unitario
    return total * (1 - descuento)


  def actualizar_estado(self):
    self.estado = 'Entregado'
    return 'Se actualizó el estado del pedido a Entregado'

#Pruebas por chat gpt
# Crear productos
producto1 = Producto("Pizza", 8.50, 10)
producto2 = Producto("Hamburguesa", 5.00, 20)
producto3 = Producto("Soda", 1.50, 50)

# Verificar que los productos se crearon correctamente
print(producto1.nombre == "Pizza")  # Debería ser True
print(producto1.precio_unitario == 8.50)  # Debería ser True
print(producto1.stock == 10)  # Debería ser True

# Actualizar stock y verificar
print(producto1.actualizar_stock(3))  # Debería restar 3 al stock
print(producto1.stock == 7)  # Debería ser True
print(producto1.actualizar_stock(8))  # Debería mostrar un mensaje de error por falta de stock
print(producto1.stock == 7)  # Stock no debería cambiar si no hay suficiente stock

# Crear un pedido
pedido = Pedido()

# Verificar que el pedido se creó correctamente
print(pedido.id == 1)  # Debería ser True
print(pedido.estado == "En preparación")  # Debería ser True

# Agregar productos al pedido
print(pedido.agregar_producto(producto1, 2))  # Debería agregar 2 pizzas
print(len(pedido.lista_productos) == 1)  # Debería ser True
print(pedido.agregar_producto(producto2, 21))  # Debería mostrar un error por falta de stock

# Calcular total del pedido con descuento
print(pedido.calcular_total())  # Debería calcular el total con un 10% de descuento

# Actualizar estado del pedido
print(pedido.actualizar_estado())  # Debería actualizar el estado a "Entregado"
print(pedido.estado == "Entregado")  # Debería ser True

# Intentar agregar producto después de entregar el pedido
print(pedido.agregar_producto(producto3, 2))  # No debería permitir agregar más productos

