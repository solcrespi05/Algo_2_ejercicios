# POO en Python

Created: August 12, 2024 12:00 PM
Ejercicios: https://github.com/solcrespi05/Algo_2_ejercicios/tree/main/POO

# Convención de nombres

Estilos en Python—> https://peps.python.org/pep-0008/

Snake Case

Se usa para variables, funciones, parámetros, módulos. 

mi_variable, celular_costo()

Pascal Case

Se usa para clases, variables de tipo, excepciones 

MiClase, LogEnDisco.

Mayúsculas con guión 

Se usa para constantes 

LONGITUD_LISTA, CANTIDAD_NROS

# Objetos

Python es un leguaje de tipado dinámico (ducktyping), por esto las variables no tienen asociado un tipo de dato. 

Las [type hints](https://www.notion.so/Type-Hints-44b17b3788cb4d17ace066e2979da029?pvs=21), mediante librerías no nativas, nos permiten hacer una verificación de tipos. Pero esta verificación no es parte del lenguaje y por lo tato no es forzada por el mismo. 

**Una variable en Python es simplemente una etiqueta a una referencia** en memoria. Esta referencia en memoria es básicamente la **dirección donde se aloja una instancia u objeto**. Por tal motivo una variable no tiene asociado un tipo de dato, esa información **está asociada al objeto en memoria**.

Cuando se genera una variable a través de la asignación =, se asocia la etiqueta al objeto, y podemos accederlo mediante ella.

Si la variable luego se asigna a otro nuevo objeto y no quedan variables que referencian al objeto previo, el recolector de basura se encargará de liberar de la memoria de ese objeto.

```python
nombre = 'Emma'
nombre2 = nombre
id(nombre)          # 2365055303536
id(nombre2)         # 2365055303536
```

Estas dos variables hacen referencia al mismo objeto y podemos acceder a el a través de ambas. 

### Identidad de Objetos

Cada objeto tiene asociado un identificador de identidad que es **exclusivo**, este identificador suele ser la dirección de memoria. Se consulta con la operación id(). 

```python
id(33)                      # 140721232205608
id('Esto es una cadena')    # 2365055278640
x = 5.5
id(x)                       # 2365048316752
```

<aside>
📌 La identidad de un objeto no se puede cambiar después de ser instanciado

</aside>

### Tipo de datos

Se desprende de la clase la cual se instancia y define qué operaciones podemos realizar sobre este objeto, esto provee encapsulamiento. 

Se consulta con la función type(). El valor devuelto corresponde al atributo especial __class__.

```python
type('Esto es una cadena')  # <class 'str'>
type(33)                    # <class 'int'>
type([1,2])                 # <class 'list'>
type(len)                   # <class 'builtin_function_or_method'>

'Esto es una cadena'.__class__  # <class 'str'>
```

El atributo __class__  podría ser modificado en el tiempo de ejecución, **pero no es recomendable hacerlo.**

# Clases

```python
class NombreClase:
# Definición de atributos y métodos de la clase
```

### Instanciación vs inicialización

La instanciación es el proceso de **crear un objeto** a partir de una clase. Involucra dos métodos en Python. Cuando se instancia una clase, el flujo es: 

1. Método __new__():  es llamado para crear y devolver una nueva instancia del objeto.
2. Método __init__():  es llamado para inicializar esa instancia.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
```

El método inicializador `__init__()` recibe como primer argumento la instancia(self por convención), y luego recibe los argumentos necesarios para inicializar el objeto. Los atributos `self.nombre` y `self.edad` son propios de esa instancia.  

```python
juana = Persona("Juana", 23)    
print(juana)                    # <__main__.Persona at 0x1d2bd5b1750>
print(hex(id(juana)))           # 1d2bd5b1750
print(juana.nombre)             # Juana
print(juana.edad)               # 23
```

## Miembros de instancia y miembros de clase

Pueden ser de dos tipos: miembros de clase y miembros de instancia. 

### Atributos

- Atributos de clase: son compartidos por todas las instancias de la clase. Se definen fuera de cualquier método de la clase y se accede a ellos utilizando el nombre de la clase. Se pueden utilizar para almacenar datos que son comunes a todas las instancias de la clase.
- Atributos de instancia: son específicos de cada objeto. Se definen dentro del método inicializador utilizando el parámetro self. Cada instancia de la clase tiene sus propias copias de los atributos de instancia.

```python
class Persona:
    contador_personas = 0

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        Persona.contador_personas += 1

juana = Persona("Juana", 23)
hugo = Persona("Hugo", 33)

juana.nombre                # 'Juana
hugo.edad                   # 33
Persona.contador_personas   # 2
juana.contador_personas     # 2
hugo.contador_personas      # 2
```

En el ejemplo contador_personas es un miembro de clase que se utiliza para llevar la cuenta de cuantas instancias de la clase Persona se generaron, mientras que nombre y edad son miembros de instancia ya que se definieron con self. Para acceder a miembro se utiliza el punto “`.`” (dot notation).

### Métodos

Las funciones definidas dentro de una clase son **métodos de instancia** y tienen la particularidad que el primer parámetro siempre es la instancia actual.

```python
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        Persona.contador_personas += 1
    def nombre_completo(self):
        return f'{self.nombre} {self.apellido}'

juana = Persona("Juana", "Lopez")
juana.nombre_completo()             # 'Juana Lopez'
```

El método `nombre_completo` es un método de instancia ya que consume o accede a atributos de instancia. 

Los **métodos de clase** operan en la clase. Pueden acceder y modificar el estado de la clase que afecta a todas las instancias de la clase. Solo pueden acceder a atributos de clase , ya que el primer parámetro es la clase. Por convención se nombra cls. Se define con el decorador @classmethod. Se usa para trabajar con datos comunes a a todas las instancias de la clase

```python
class Persona:
    contador_personas = 0

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        Persona.contador_personas += 1

    @classmethod
    def personas_creadas(cls):
        return cls.contador_personas

juana = Persona("Juana", "Lopez")
Persona.personas_creadas()          # 1
juana.personas_creadas()            # 1
```

> **Una instancia puede acceder a miembros de instancia y miembros de clase**
> 

Los **métodos estáticos** no operan ni sobre una instancia de la clase ni sobre la clase misma. Son funciones asociadas con la clase para propósitos organizacionales. Se definen con el decorador @staticmethod 

```python
class Persona:
    # Implementación de Persona...

    @staticmethod
    def a_minusculas(cadena):
        return cadena.lower()

Persona.a_minusculas('Probando Método Estático')  # 'probando método estático'
```

Los métodos estáticos (cont) al igual que con los métodos de clase, no es necesario instanciar un objeto para invocarlos. Son buenos candidatos para modelar comportamiento de ayudar (helpers)

Los Helpers son funciones o métodos diseñados para realizar tareas comunes, repetitivas o de soporte dentro de código. Estas funciones son pequeñas, especificas y encapsulas una lógica particular que puede ser reutilizada en diferentes partes del programa. Permiten actualizar y mantener el código.

### Métodos especiales (dunder o mágicos)

Son invocados implícitamente para ejecutar cierta operación sobre un tipo de dato. Comienzan y terminan con “`__`”. Se puede definir u comportamiento diferente para nuestras clases respecto a los operadores del lenguaje logrando una sobrecarga de operadores. 

Algunos son:

1. `__init__(self,…)`
2. `__str__(self)`: Devuelve una representación en cadena “informal” del objeto. 
3. `__repr__(self)`: Devuelve una representación en cadena ”oficial” del objeto.
4. `__len__(self)`: Devuelve el numero de elementos de un objeto. 
5. `__getitem__(self, key)`: Permite el acceso a elementos mediante el operador []
6. `__setitem__(self,key,value)`: Permite la asignación de valores mediante el operador []
7. `__eq__(self,otro)`: Define la comparación de igualdad entre objetos. Es invocado cuando de utiliza el operador ==.
8. `__hash__`: Retorna número entero que identifica al objeto. Si dos objetos son considerados iguales según el método __eq__, también deben tener el mismo valor hash. La documentación oficial recomienda devolver el valor hash de la tupla con los atributos utilizados en el __eq__().
9. `__inter__(self) y __next__(self)`: Permiten que un  objeto se iterable.
10. `__call__`:permite que las instancias de un clase sean llamadas como si fueran funciones. 

```python
class Persona:
    # resto de la implementación de Persona...
    
    def __repr__(self):
        return f'<{self.__class__.__name__}("{self.nombre}","{self.edad}")>'
    def __str__(self):
        return f'Nombre: {self.nombre}, Edad: {self.edad} años'
		def __eq__(self, otro):
        return isinstance(otro, Persona) and self.nombre == otro.nombre and self.edad == otro.edad
		def __hash__(self):
		    return hash((self.nombre, self.edad))

juana = Persona("juana", 23)
juana2 = Persona("juana", 23)
juana == juana2     # True
juana = Persona("juana", 23)    # Nombre: juana, Edad: 23 años
juana = Persona("juana", 23)    # <Persona("juana","23")>
```

```python
class FormateadorMayusculas:
    def __init__(self):
        self.texto = ''
    def __call__(self, texto: str) -> str:
        return texto.upper()
    
a_mayusculas = FormateadorMayusculas()
a_mayusculas('esto es una prueba')      # 'ESTO ES UNA PRUEBA'
```

```python
class MiContenedor:
    def __init__(self):
        self.elementos = []
    def __len__(self):
        return len(self.elementos)
    
contenedor = MiContenedor()
len(contenedor)     # 0
```

## Accesibilidad a miembros de clase

En Python no hay un mecanismo que permita modificar la visibilidad de los elementos de una clase. Se distingue entre miembros públicos y no públicos solo mediante una convención de nombre. 

Un miembro de una clase con un nombre que comienza con `_`, se asume es **no público**. Si bien Python **no restringe el acceso desde afuera**, es una señal a quien consume la clase que **no debe accederlo directamente**.

Por otra parte, también existe otra forma de nombrar miembros no públicos mediante el prefijo de doble guión bajo `__`. En este caso, el intérprete modifica internamente el nombre del miembro anteponiendo como prefijo `_NombreClase`.

```python
class MiClase:
    def __init__(self):
        self.x = 1
        self._y = 2
        self.__z = 3

mi_objeto = MiClase()
print(dir(mi_objeto))           # ['_MiClase__z', ..., '_y', 'x']
print(mi_objeto.x)              # 1
print(mi_objeto._y)             # 2
print(mi_objeto._MiClase__z)    # 3
mi_objeto._MiClase__z = 9
print(mi_objeto._MiClase__z)    # 9
```

### Atributos → propiedades

El encapsulamiento en POO es un principio que permite proteger los atributos y métodos de una clase para evitar su acceso y modificación directa desde afuera. Una forma respecto del acceso y la modificación de los atributos de una clase es mediante el uso de propiedades: permiten definir métodos “getter” y “setter”.

```python
class Persona:
	 def __init__(self, nombre):
		 self._nombre = nombre # Atributo "privado"
	 @property
	 def nombre(self):
		 """Getter para el atributo nombre"""
		 return self._nombre
	 @nombre.setter
	 def nombre(self, valor):
		 """Setter para el atributo nombre"""
		 self._nombre = valor
# Crear una instancia de la clase Persona
persona = Persona('Juan')
#Acceder a los atributos a través de getters
print(persona.nombre) # Salida: Juan
# Modificar los atributos a través de setters
persona.nombre = 'Ana'
print(persona.nombre) # Salida: Ana
```

# Herencia

La herencia se realiza mediante la declaración de una clase derivada o subclase que hereda de una clase extendida o superclase. La subclase hereda todos los atributos y métodos de la superclase. Se representa una jerarquía de abstracciones. 

```python
#Herencia simple
class Persona:
    pass
    
class Estudiante(Persona):
    pass

juana = Estudiante()
isinstance(juana, Estudiante)   # True
isinstance(juana, Persona)      # True
isinstance(juana, object)       # True

#Herencia múltiple
class UserCampus(Estudiante, Docente):  # Ejemplo de herencia múltiple
    pass
```

Object es la CLASE BASE más general de la cual todas las demás clases derivan. Define varios MÉTODOS COMUNES que están disponibles para todas las instancias de las clases. Algunos son: __init__, __str__, __repr__, __eq__, __hash__.

### Constructor heredado

Si la superclase y subclase tienen un inicializador definido, debemos al primero explícitamente en el inicializador de nuestra subclase.

```python
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
class Estudiante(Persona):
    def __init__(self, nombre, apellido, matricula):
        super().__init__(nombre, apellido)  # Invoca inicializador de Persona
        self.matricula = matricula

juana = Estudiante("Juana", "Lopez", 1234)
```

### Sobreescritura

Una SUBCLASE REDEFINE un método de su superclase para cambiar su
comportamiento.

```python
class Animal:
 def hacer_sonido(self):
	 print("Algún sonido genérico")
	 
class Perro(Animal):
 def hacer_sonido(self):
	 print("Guau guau")
	 
perro = Perro()
perro.hacer_sonido() # Salida: Guau guau
```

### Polimorfismo

Diferentes clases comparten el mismo nombre de método pero lo implementen de manera específica. Es un componente esencial de la herencia que permite escribir código más flexible y reutilizable. Se apoya en el concepto de sobreescritura.

```python
class Gato:
	 def hacer_sonido(self):
		 print("Miau")
class Perro:
	 def hacer_sonido(self):
		 print("Guau guau")
def hacer_sonido_animal(animal): #NOTAR QUE LA FUNCIÓN ESTÁ FUERA de las clases
 animal.hacer_sonido()
gato = Gato()
perro = Perro()
hacer_sonido_animal(gato) # Salida: Miau
hacer_sonido_animal(perro) # Salida: Guau guau
```

### Method Resolution Order (MRO)

Mecanismo por el cual se determina **un orden particular donde buscaremos implementaciones de un método a lo largo de la jerarquía de clases**.

```python
class A:
    def metodo1(self):
        return 'Metodo1 de A'
class B(A):
    def metodo1(self):
        return 'Metodo1 de B'
 
objeto_b = B()
objeto_b.metodo1()      # Metodo1 de B
A.mro()     # [__main__.A, object]
B.mro()     # [__main__.B, __main__.A, object]
```

### Clases abstractas

Para definir nuestra propia clase abstracta, simplemente debemos **heredar de la clase abc.ABC**.

Para forzar este comportamiento debemos agregar al menos un **método abstracto** utilizando el decorado

```python

from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    @abstractmethod
    def mostrar_info(self):
        raise NotImplementedError

vehiculo = Vehiculo("Toyota", "Corolla")    # TypeError: Can't instantiate abstract class Vehiculo with abstract method mostrar_info
```

Si no definimos el método `mostrar_info()` como abstracto, entonces podríamos instanciar a `Vehiculo` a pesar de modelarla como una clase abstracta

### Comparadores

Estos métodos nos permiten **sobrecargar los operadores de comparación**, como `==`, `!=`, `<`, `>`, `<=` y `>=`, para nuestros propios tipos de datos personalizados.

- `__ne__(self, other)`: Se invoca cuando se utiliza el operador de desigualdad (!=) para comparar dos objetos, por defecto utiliza `__eq__()` invirtiendo su valor retornado.
- `__lt__(self, other)`: Se invoca cuando se utiliza el operador menor que (<) para comparar dos objetos. Se puede apoyar en `__gt__()` invirtiendo su resultado.
- `__gt__(self, other)`: Se invoca cuando se utiliza el operador mayor que (>) para comparar dos objetos. Se puede apoyar en `__lt__()` invirtiendo su resultado.
- `__le__(self, other)`: Se invoca cuando se utiliza el operador menor o igual que (<=) para comparar dos objetos. Se puede apoyar en `__ge__()` invirtiendo su resultado.
- `__ge__(self, other)`: Se invoca cuando se utiliza el operador mayor o igual que (>=) para comparar dos objetos. Se puede apoyar en `__le__()` invirtiendo su resultado.

# Funciones internas

Son funciones definidas dentro de otras funciones. Pueden acceder a las variables locales y los parámetros de la función externa. Permiten modularizar el código y encapsular la lógica. 

```python
def funcion_externa():
    def funcion_interna():
        return "Esta es una funcion interna."

    return funcion_interna()

print(funcion_externa())  # "Esta es una funcion interna."
print(funcion_interna())  # NameError: name 'funcion_interna' is not defined
```

Beneficios: 

- Funciones de ayuda(helpers): Si esta operación de ayuda se consume sólo desde cierta clase, se podría definir simplemente un método privado (posiblemente estático) que sea accedido sólo desde dentro de la clase. Si la operación de ayuda sólo se consumirá desde cierta función o método, entonces una buena opción es definirla como **función interna**.
- Encapsulamiento: Mediante el uso de funciones internas podemos encapsular funcionalidades dentro de una función externa. Esto es útil cuando deseamos **restringir el acceso de cierta función interna al ámbito de la función externa**.

### Clausura

Es la **combinación de una función con el ámbito en el que fue creada**, incluso después de que ese ámbito haya dejado de existir, manteniendo el acceso a las variables locales de la función externa. 

Un caso común donde se utiliza es en la currificación ([paradigma funcional](https://www.notion.so/Paradigma-Funcional-3185bd988bcb455ca0bebe01b6cb3314?pvs=21)).

```python
def crear_clausura(x):
 def clausura(y):
			 # La función interna puede acceder a 'x', que es una variable de la función externa.
			 return x + y # Retorna la suma de 'x' y 'y'.
		# Retornamos la función interna 'clausura'.
		# 'clausura' "recuerda" el valor de 'x' incluso después de que 'crear_clausura' haya terminado.
		return clausura
		
# Crear una instancia de la clausura.
# Llamamos a 'crear_clausura' con el valor 5, lo que devuelve la función 'clausura' con 'x' fijado en 5.
sumar_cinco = crear_clausura(5)
# Usar la clausura.
# Ahora, 'sumar_cinco' es una función que espera un argumento 'y' y sumará ese 'y' con el 'x' que recuerda
print(sumar_cinco(10)) # Salida: 15. Esto calcula 5 + 10 y devuelve 15.
print(sumar_cinco(20)) # Salida: 25. Esto calcula 5 + 20 y devuelve 25.
```

# Decoradores

Función que recibe otra función como argumento y devuelve una nueva función con un comportamiento modificado o extendido. Se aplican a las funciones con el símbolo @.

```python
def mi_decorador(func):
	 # Definimos una función interna 'nueva_funcion' que envolverá a la función original 'func'
	 def nueva_funcion(*args, **kwargs):
		 #Podemos agregar código que queremos que se ejecute antes de llamar a 'func'
		 print("Antes de ejecutar la función")
		 # Llamamos a la función original 'func' con los argumentos que recibió
		 resultado = func(*args, **kwargs)
		 #Podemos agregar código que queremos que se ejecute después de llamar a 'func'
		 print("Después de ejecutar la función")
		 # Devolvemos el resultado de la función original 'func'
		 return resultado
	 # Retornamos la función interna 'nueva_funcion'
	 return nueva_funcion
	 
# Aplicamos el decorador
@mi_decorador #mismo nombre que el decorador
def saludar(nombre):
	 print(f"Hola, {nombre}")
# Llamamos a la función decorada 'saludar'
saludar("Juan") #Salida: Antes de ejecutar la función Hola, Juan Después de ejecutar la función
```

# Organización del código (completar dsp) ver documentación y excepciones que no estan la ppt

### Módulos

```python
# Archivo modulo2.py
from modulo1 import ClaseA

def funcion2():
    clasea = ClaseA()   # ok, importada desde modulo1
    claseb = ClaseB()   # error, no se importó desde modulo1
```

Veamos el ejemplo donde tenemos dos módulos: `modulo1` y `móoulo2`. En el primer módulo definimos `ClaseA` y `ClaseB`. En el segundo módulo definimos una función `funcion2`. Consideremos que ambos archivos `modulo1.py` y `modulo2.py` se encuentran en la misma carpeta en nuestro sistema operativo.

Analizando el contenido de `modulo2.py` vemos que podemos importar a través de la instrucción [`import`](https://docs.python.org/3/reference/import.html) las definicioes que se encuentran en otro módulo (archivo). En este caso particular, se utiliza una forma de importar más específica, donde solicitamos traer sólo la definición de `ClaseA` con la instrucción `from`. Lo interesante de esta opción es que **podemos consumir lo importado sin agregar el prefijo del módulo** como veremos a continuación.