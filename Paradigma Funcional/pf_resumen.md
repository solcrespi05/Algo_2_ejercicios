# Paradigma Funcional

Created: August 12, 2024 12:00 PM
Ejercicios: https://github.com/solcrespi05/Algo_2_ejercicios/tree/main/Paradigma%20Funcional

# Paradigma Funcional

Se basa en el concepto de f**unciones matemáticas,** evita el cambio de estado y las mutaciones de variables. Se centra en el uso de expresiones, la evaluación de funciones y en la composición de estas para resolver problemas. Es un **paradigma declarativo** ya que se diseñan soluciones a través de la aplicación de funciones, definiendo qué se debe calcular en lugar de cómo realizarlo a través de instrucciones. 

### Conceptos del Paradigma Funcional

- **Inmutabilidad**: Los datos son inmutables, no se pueden cambiar. Solo se pueden crear nuevos objetos con el estado deseado.
- **Funciones Puras**: Las funciones no tienen efectos secundarios y siempre producen el mismo resultado para los mismos argumentos. No dependen de variables externas o del estado del programa y tampoco lo alteran.
- **Transparencia Referencial:** una función dada con los mismos argumentos devolverá siempre el mismo resultado.
- **Evaluación perezosa**: Es una estrategia de evaluación que demora la evaluación de una expresión hasta que se necesite su valor.
- **Recursión**: Se fomenta para controlar el flujo del programa.

### El concepto de estado

El estado de un objeto se define a partir del valor asociado en cierto instante a sus atributos, y luego mediante métodos se puede modificar el estado del objeto. En el **paradigma imperativo** es común que se realicen las modificaciones sobre el valor de las variables a través de la ejecución ordenada de sentencias o instrucciones. 

```python
#Ejemplo de contador con el paradigma imperativo en python. 
contador: int = 0

def incrementar_contador():
    global contador
    contador += 1

incrementar_contador()
print(contador)     # Salida: 1
```

Es propio del **paradigma imperativo** el uso de **procedimientos**, donde se modulariza cierta funcionalidad en un bloque de código que no devuelve un retorno. Es por ello que un procedimiento necesariamente produce algún **efecto secundario** en el programa al ejecutarse, de lo contrario no tendría sentido de existir.

En el paradigma funcional entonces reemplazaremos la noción estado por la **evaluación de funciones**, las cuales generarán nuevos valores a partir de los recibidos por parámetros. En Python, veremos que **generamos nuevos objetos** a partir de otros recibidos.

### Ciudadanos de primera clase

Una **función de orden superior** cumple al menos una de estas condiciones:

- Recibe una o más funciones como argumento
- Devuelve una función como retorno

En el área de computación algunos lenguajes permiten definir funciones de orden superior, y es principalmente una característica clave en la **programación funcional**. De esta forma, estos lenguajes consideran a las funciones como **ciudadanos de primera clase**, ya que podemos:

- pasarlas como parámetros de una función
- devolverlas como resultado de una función
- asignarlas a variables
- almacenarlas en estructuras de datos

> **Las funciones de orden superior son aquellas funciones que pueden aceptar otras funciones como argumentos y/o devolver funciones como resultados**.
> 

```python
from typing import TypeVar, Union
from collections.abc import Callable, Sequence

Numerico = Union[int, float]

T = TypeVar("T")

def aplicar_operacion(lista: Sequence[T], operacion: Callable[[T], T]) -> Sequence[T]:
    resultado = []
    for elemento in lista:
        resultado.append(operacion(elemento))
    return resultado

# Definición de funciones que se aplicarán a la lista
def cuadrado(x: Numerico) -> Numerico:
    return x * x

def inverso(x: Numerico) -> Numerico:
    return 0 - x

# Uso de funcion de orden superior
numeros: list[int] = [1, -2, 3, -4, 5, -6]
numeros_cuadrados = aplicar_operacion(numeros, cuadrado)  # Elevar al cuadrado
numeros_inversos = aplicar_operacion(numeros, inverso)   # Inverso aditivo

print(numeros_cuadrados)  # [1, 4, 9, 16, 25, 36]
print(numeros_inversos)  # [-1, 2, -3, 4, -5, 6]
```

En este ejemplo definimos una función de orden superior `aplicar_operacion` que recibe una función como segundo parámetro. Luego, como en Python las funciones son ciudadanos de primera clase (son objetos), podemos pasarlas como argumento a nuestra función previa.

### Composición de funciones

$h = g o f => h(x) = g(f(x))$

Este *encadenamiento* de funciones es clave en la programación funcional ya que nos permite *conectar* la entrada y salida de funciones para realizar la transformación deseada.

El RESULTADO de una función se pasa como ARGUMENTO a OTRA. Python lo facilita porque trata a las funciones como ciudadanos de primera clase.

### Inmutabilidad

Es la incapacidad de un objeto para cambiar su estado después de su creación. Esto implica que una vez que se ha creado un objeto inmutable, sus atributos internos no pueden ser modificados. 

Beneficios:

- Claridad y entendimiento: Simplifica la lógica, no es necesario rastrear cambios en el estado a lo largo del tiempo.
- Prevención de cambios accidentales: previene cambios accidentales en el estado del objeto.
- Concurrencia mas sencilla y segura: eliminan la necesidad de sincronización para evitar problemas de concurrencia.
- Facilita la Programación funcional: facilita la adopción de principios funcionales.
- Optimización de Rendimiento: Los compiladores y entornos de ejecución pueden optimizar el código que involucra objetos inmutables.

### Transitividad

En Python, los atributos de un objeto pueden ser referencias a otros objetos. Si un objeto contiene referencias a otros y son **mutables**, el objeto original puede mutar.

**Mutabilidad transitiva**: Si el objeto B es mutable, cualquier cambio en B a través de cualquier referencia afectará el estado al objeto A.
**Inmutabilidad transitiva**: para que el objeto A sea inmutable, todos los objetos a los que A hace referencia (como B) también deben ser inmutables.

- Tipos nativos de Python inmutables: int, float, complex, bytes, str, tuple.
- Tipos nativos de Python mutables: list, dict, set.

## Clases Inmutables

### Ocultando atributos

Existe un **atributo de clase** especial [`__slots__`](https://docs.python.org/3/reference/datamodel.html#object.__slots__) que permite optimizar la creación de instancias en memoria, ya que **podemos asignarle un conjunto fijo de nombres de atributos** que tiene una instancia de esa clase. Por lo tanto, si definimos `__slots__ = ('x', 'y',)` como atributo de una clase significa que un objeto de esa clase sólo podrá tener como atributos a *x* e *y*.

### Properties

Sabemos que en Python existe posibilidad de convertir atributos en propiedades para mejorar el encapsulamiento de la clase. Una estrategia sería **convertir los atributos en propiedades de sólo lectura**, es decir, no definir los *setters*.

```python
class MiClaseInmutable:
    def __init__(self, valor_inicial):
        self._valor = valor_inicial
    
    @property
    def valor(self):
        return self._valor

objeto_inmutable = MiClaseInmutable(20)
objeto_inmutable.valor                      # 20
objeto_inmutable.valor = 10                 # AttributeError: property 'valor' of 'MiClaseInmutable' object has no setter
objeto_inmutable._valor = 10                # Modifica el valor
objeto_inmutable.valor                      # 10
```

### **Métodos especiales `__setattr__` y `__delattr__`**

Cuando intentamos realizar una asignación para un atributo de un objeto, internamente se invoca el método `__setattr__` que recibe como argumentos: el objeto en sí, el nombre del atributo y el valor a asignarle. Entonces, si sobrescribimos este método en nuestra clase inmutable, podríamos evitar cualquier tipo de asignación en los atributos de la clase.

El método `__delattr__` es similar y sólo recibe como argumento el nombre del atributo. Se invoca cuando se intenta eliminar un atributo de un objeto con el comando `del`. Así que también nos serviría para evitar que se eliminen atributos.

```python
class MiClaseInmutable:
    __slots__ = ('_valor',)

    def __init__(self, valor_inicial):
        super().__setattr__('_valor', valor_inicial)
    
    def __setattr__(self, __name: str, __value: Any) -> None:
        raise AttributeError(f'No es posible setear el atributo {__name}')
    
    def __delattr__(self, __name: str) -> None:
        raise AttributeError(f'No es posible eliminar el atributo {__name}')
    
    def valor(self):
        return self._valor
```

Si combinamos la sobrescritura de estos métodos con el uso del atributo `__slots__` logramos una **muy buena inmutabilidad** de la clase, por lo menos superficial.

### Named Tuples

Las tuplas son un tipo de dato inmutable en Python. Utilizar `namedtuple` que nos permite generar un objeto subclase de `tuple`, por ende inmutable, pero con los atributos con nombres en lugar de índices (código más legible y fácil de mantener).

El problema con esta estrategia es que perdemos el concepto de **encapsulamiento** que nos proveen las clases, vinculando la estructura con el comportamiento. Como solución podemos definir nuestra clase heredando desde `namedtuple`.
Debemos agregar `__slots__` para evitar que la clase pueda aceptar nuevos atributos, pero luego podemos definir el comportamiento que deseemos, como en el ejemplo sobreescribiendo el método especial `__repr__`.

```python
from collections import namedtuple

class MiClaseInmutable(namedtuple('MiClaseInmutable', 'valor1 valor2')):
    __slots__ = ()
    def __repr__(self) -> str:
        return f'{super().__repr__()} INMUTABLE'
    
mi_obj = MiClaseInmutable(10, 20)
mi_obj                  # MiClaseInmutable(valor1=10, valor2=20) INMUTABLE
```

### Dataclasses

El módulo `dataclasses` provee funcionalidad que implementa automáticamente **métodos especiales** en clases que diseñamos. La particularidad es que definimos la estructura de nuestras clases con **variables de clase** con anotaciones de tipo, y luego la función decoradora `dataclass` genera los atributos de instancia correspondientes implementando el método `__init__()`.

```python
from dataclasses import dataclass

@dataclass
class Persona:
    nombre: str
    apellido: str
    edad: int

    def es_adulta(self):
        return edad >= 18
```

Por defecto, el decorador `@dataclass` nos implementará automáticamente los siguientes métodos: `__init__()`, `__repr__()` y `__eq__()`.

El decorador `@dataclass` tiene un parámetro (recordemos que es una función como cualquier otra) que permite convertir a los **atributos de instancia de solo lectura**. El nombre del parámetro es `frozen` y es un booleano que si se define en `True` podemos evitar la asignación nueva de valores y así **proveer inmutabilidad a nuestra clase**.

```python
from dataclasses import dataclass

****@dataclass(frozen=True)
class Persona:
    nombre: str
    apellido: str
    edad: int

    def es_adulta(self):
        return edad >= 18
    
p = Persona("Julia", "Martinez", 22)
print(p)        # Persona(nombre='Julia', apellido='Martinez', edad=22)
p.edad = 20     # FrozenInstanceError: cannot assign to field 'edad'
```

## Funciones puras y transparencia referencial

Una **función pura** cumple con dos condiciones:

- Dados los mismos parámetros de entrada, **siempre** devuelve el mismo valor como retorno.
- No debe producir **efectos secundarios**, sólo debe enfocarse en realizar el cálculo necesarios para generar el retorno a partir de sus parámetros.

### Transparencia referencial

La primera condición está relacionada con el concepto lingüístico de **transparencia referencial**, donde podríamos reemplazar a cierta expresión de una función y argumentos aplicados simplemente con su valor de retorno y así no se producirían cambios semánticos en el programa.

```python
#La operación suma es una función pura porque cumple ambas condiciones
def suma(x: int, y: int) -> int:
    return x + y

nro: int = suma(10, 6) * 2
nro: int = 16 * 2           # Reemplazamos suma(10, 6) por su valor evaluado 16
```

### Efectos secundarios

Una operación que produce efectos secundarios o colaterales es aquella que **puede incluir diversas interacciones con el entorno del programa y modificar el estado fuera del ámbito local de la función**. Algunos de los tipos comunes de efectos secundarios incluyen:

- Modificación de variables globales
- Modificación de Argumentos:  Una función impura puede modificar el valor asociado a un parámetro (si se pasa por referencia) o alterar el estado de un objeto que se pase como argumento (en lenguajes que aceptan el pasaje por valor de referencias).
- Operación de Entrada/Salida (I/O): Interacciones con el mundo exterior, como lectura o escritura en archivos, envío de correos electrónicos, acceso a bases de datos, etc.
    - Impresiones en Consola o Registro de Eventos: son operaciones de salida.
    - Interacciones de Red:  Las operaciones de red, como solicitudes a una API.
- Llamadas a Funciones con Efectos Secundarios:  Si una función llama a otra función impura, automáticamente se convierte en una función impura también. A su vez, si ambas producen efectos colaterales, se pueden acumular y propagarse.
- Generación de Números Aleatorios: su resultado puede variar en diferentes llamadas, lo que introduce una variabilidad no determinista.

Ejemplos de implementación en las diapos de la 23 a 29

## Estrategias de evaluación

En el cálculo lambda computamos una expresión a través de la reescritura de la misma, aplicando diferentes reglas de conversión y reducción hasta llegar a expresiones irreducibles, lo que se denomina en *forma normal* o *forma canónica*. A través de la reducción Podemos encontrar dos estrategias para reducir un término a una *forma normal*, una expresión que resulta irreducible.

- **Orden aplicativo**: Se reducen primero las expresiones reducibles más internas, aquellas que no contienen términos reducibles.
- **Orden normal**: Se reducen primero las expresiones reducibles (*redex*) más externas, aquellas que no están incluidas como términos de otras.

### Evaluación estricta

Similar al **orden aplicativo**, en la evaluación estricta **se requieren resolver antes las expresiones internas** o argumentos de una función. Esta idea está relacionada con el concepto de **evaluación *impaciente*** o *eager* que plantea que debemos evaluar todos las expresiones internas antes de avanzar con la externa, aún si no fueran necesarias para calcular el valor.

> En Python prácticamente todo se evalúa de forma estricta, con ciertas excepciones que veremos a continuación en evaluación no estricta.
> 

```python
def func1():
    print('Evalua funcion 1')
    return 1
def func2():
    print('Evalua funcion 2')
    return 2
def sumaRara(x, y):
    print('Evalua funcion externa')
    return x if x == 1 else x + y

sumaRara(func1(), func2())
# Salida:
# Evalua funcion 1
# Evalua funcion 2
# Evalua funcion externa
# 1
```

### Evaluación no estricta

Similar al **orden normal**, pero no necesariamente requiere evaluar antes todas las externas. Una función evaluada de forma no estricta p**odría devolver un resultado aún si no se evaluaron todos sus argumentos.**

Uno de los aspectos que hace **eficiente** la programación funcional es la capacidad de **diferir el cómputo de expresiones al momento en el cual son requeridas.** Aquí el concepto de **evaluación en orden normal es fundamental** ya que permite ignorar expresiones que puedan ser muy costosas de operar si no son necesarias.

### Evaluación de cortocircuito

Se aplica a expresiones booleanas. Se implementa en Python y permite evitar la evaluación de un segundo término dependiendo del valor del primero.

- <expresion_1> and <expresion_2> : Si <expresion_1> es False, <expresion_2> no se evalúa.
- <expresion_1> or <expresion_2>: Si <expresion_1> es True, <expresion_2> no se evalúa.

```python
def esDivisor(nro: int, divisor: int) -> bool:
    return (divisor > 0) and (nro % divisor == 0)

esDivisor(10, 0)    # False
```

### Evaluación perezosa

Establece que la evaluación de una expresión puede dilatarse hasta que sea necesario su valor. El opuesto de la evaluación impaciente. 

Permite trabajar con **estructuras infinitas**. En Python usamos generadores implementados mediante funciones generadoras o expresiones generadoras, las cuales permiten retornar un **iterador perezoso** mediante la palabra reservada `yield`.

El `yield` es análogo al `return` de una función normal. Devuelve un iterador de cierta colección de datos.

Se ejecutan las instrucciones de la función generadora hasta el `yield`, momento en el cual **suspende la ejecución de la función** y se devuelve el valor actual dado por la expresión del `yield` en ese instante.

Un **iterador** en Python es un **objeto** que implementa los métodos especiales `__iter()__` y `__next()__` .Proveen una forma de **acceder a los elementos de a uno a la vez y sin repetirlos**

```python
from collections.abc import Iterator

def genera_saludo() -> Iterator[str]:
    yield "Hola"
    yield "Buenas"
    yield "Buen día"

iterador_saludos = genera_saludo()
print(next(iterador_saludos))   # Hola
print(next(iterador_saludos))   # Buenas
print(next(iterador_saludos))   # Buen día
print(next(iterador_saludos))   # Error StopIteration
```

El final está marcado por la **excepción `StopIteration` .**

```python
#Es útil para modelar estructuras infinitas. 
from collections.abc import Iterator

def positivos_pares() -> Iterator[int]:
    numero: int = 0
    while True:
        yield numero
        numero += 2
```

```python
#Asi seria la **expresión generadora** del ejemplo anterior
positivos_pares = (x for x in range(0, 10, 2))  # <generator object <genexpr> ...>
```

## Transformación de funciones

### Currificación

La conversión de una función con n argumentos en n funciones con un único argumento. Esto devuelve una función con aplicación parcial de un argumento en cada caso. 

`f(x, y, z) -> f(x)(y)(z)`

Se devuelve otra función con los argumentos pasados aplicados y aceptando los argumentos restantes.

Esto nos provee algunos beneficios:

- Construir funciones generalizadas que sean más fáciles de reutilizar.
- Generar de funciones específicas a partir de funciones generalizadas con algunos parámetros predefinidos.
- Facilita la composición de funciones.
- Facilita el razonamiento usando funciones parcialmente aplicadas.

```python
# Función simple de suma
def suma(x, y):
    return x + y

# Función currificada de suma
def suma_curry(x):
    def suma_x(y):
        return x + y
    return suma_x

print(suma(1, 3))
print(suma_curry(1)(3))
```

### functools.partial

Nos permite realizar la vinculación de la aplicación parcial a otra función.

```python
from functools import partial

def producto(x: int, y: int) -> int:
    return x * y

producto_10 = partial(producto, 10)
producto_10(2)
```

### pymonad.tools.curry

Tiene el mismo objetivo de facilitar la currificación de una función. Simplemente le debemos indicar la cantidad de argumentos con la cual se currifica.

```python
from pymonad.tools import curry

@curry(2)
def producto(x: int, y: int) -> int:
    return x * y

producto_10 = producto(10)
producto_10(2)
"""
también se puede asignar la función 
currificada a una nueva variable sin 
utilidar el decorador"""

from pymonad.tools import curry

producto_curry = curry(2, producto)
```

### Composición con decoradores

Recordemos que una composición es la aplicación de una función sobre el resultado de otra función evaluada. Un decorador puede cumplir con esa definición ya que básicamente realiza lo siguiente: `mi_funcion = decorador(mi_funcion)`.

El decorador `trim` adapta la función sobre la cual se aplica de forma que incorpora la eliminación de espacios en blanco de la cadena resultante

```python
from collections.abc import Callable
from functools import wraps

def trim(f: Callable[[str], str]) -> Callable[[str], str]:
    @wraps(f)
    def wrapper(texto: str) -> str:
        return f(texto).strip()
    return wrapper

@trim
def transforma_texto(texto: str) -> str:
    return texto.replace('.',' ')

transforma_texto('  esto es una prueba. ')  # 'esto es una prueba'
```

También podemos definir parámetros en funciones decoradoras, logrando así una composición del estilo: `h = g(y) o f`, donde `y` sería un parámetro propio de la función decoradora.

```python
from collections.abc import Callable
from functools import wraps

def trim(inicio: bool = True, fin: bool = True) -> Callable[[Callable[[str], str]], Callable[[str], str]]:
    def trim_deco(f: Callable[[str], str]) -> Callable[[str], str]:
        @wraps(f)
        def wrapper(texto: str) -> str:
            texto = f(texto)
            if inicio:
                texto = texto.lstrip()
            if fin:
                texto = texto.rstrip()
            return texto
        return wrapper
    return trim_deco
```

## Iteraciones e iterables

En la programación imperativa trabajamos con bucles. 

Dado que en el paradigma funcional **no disponemos de este tipo de estructuras** (bucles), debemos modelar esta lógica a través de funciones puras y la **recursión**.

Funciones que podemos utilizar para trabajar con objetos iterables desde un enfoque
funcional en Python:

● Mapeos: Construyen una nueva colección a partir de la original con la misma cantidad
de elementos pero aplicando cierta transformación,

● Filtrado: Construyen una nueva colección a partir de la original pero con una cantidad
reducida de elementos, ignorando aquellos que no cumplen cierto criterio.

● Reducciones: Producen un valor a partir de los elementos de una colección, por
ejemplo sum(), max(), len().

### map

En Python disponemos de la operación nativa [`map`](https://docs.python.org/3/library/functions.html#map) que recibe una función y al menos un objeto iterable, y **devuelve un iterador perezoso** (recordemos el `yield`) que entrega (a demanda) el resultado de aplicar esa función a cada elemento del iterable.

Si se pasaran más de un iterable, entonces la función debe aceptar tantos argumentos como iterables ya que se aplicaría a sus elementos.

Sintaxis → `map(function, iterable, *iterables)` 

Dado que recibe a otra función como argumento, `map` es una **función de orden superior**.

Esta operación básicamente reemplaza el comportamiento de un bucle `for-each` sobre cierta colección iterable, donde se aplica cierta operación en cada elemento de la colección para construir una nueva.

```python
xs: list[int] = [1, 2, 3, 4]
ys: list[int] = []
operacion = lambda x: x * x
for x in xs:
    ys.append(operacion(x))
```

Cuando aplicamos **`map` a listas** en Python, es recomendable utilizar [list comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions) ya que facilitan la lectura de código.

### filter

El filtrado de una colección consiste en aplicarle un predicado (función que devuelve un booleano) para generar una **nueva colección** que contiene sólo aquellos elementos de la original donde al aplicarles el predicado retorna *Verdadero*. 

```python
def es_par(n: int) -> bool:
    return n % 2 == 0

xs = [1, 2, 3, 4, 5, 6]

filter(es_par, xs)  # <filter at 0x1d2af1aed70> 
list(filter(es_par, xs))    # [2, 4, 6]
```

La función `filter` retorna también un **iterador perezoso**, un objeto *filter*, el cual retorna el valor del próximo elemento que cumple con el predicado (`es_par(<elemento>)` igual a `True`) cuando se lo requiere.

### Reduce

Representa el concepto funcional denominado [fold](https://en.wikipedia.org/wiki/Fold_(higher-order_function)), donde **se produce un valor** a partir de la aplicación de una **función acumuladora/combinadora/reductora** sobre una estructura iterable.

La idea de esta operación se resume en estos pasos:

1. Obtener un valor inicial que será valor acumulado/reducido.
2. Si el iterable no tiene elementos por iterar, devolver valor acumulado, sino avanzar al paso siguiente.
3. Aplicar una función reductora sobre el valor acumulado y el elemento actual del iterable.
4. Repetir el paso 1 usando el retorno del paso 2 como nuevo valor acumulado.

```python
from functools import reduce

def contar_letras(acumulado: int, elemento: str) -> int:
    return acumulado + len(elemento)

reduce(contar_letras, ['casa', 'puente', 'ojo'], 0)     # 13

valor_reducido = 0
    contar_letras(0, 'casa')            # valor_reducido: 4
        contar_letras(4, 'puente')      # valor_reducido: 10
            contar_letras(10, 'ojo')    # valor_reducido: 13
```

El reduce con valor inicial es útil en casos donde la secuencia podría estar vacía o para definir un valor inicial específico. 

Sintaxis → `reduce(funcion, secuencia, valor inicial)` 

```python
from functools import reduce
numeros = [1, 2, 3, 4, 5]
suma_con_inicial = reduce(lambda x, y: x + y, numeros, 0)
print(suma_con_inicial) # Output: 15
```