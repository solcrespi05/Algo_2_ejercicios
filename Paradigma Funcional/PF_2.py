"""Implementar una versión de un conjunto de elementos de cualquier tipo que
sea inmutable. Podemos apoyarnos en la tuple de Python. El conjunto se
crea con una cantidad de elementos variables y luego ya no puede
modificarse."""

from collections import namedtuple

Persona = namedtuple ('Persona', ['nombre', 'edad'])
sol = Persona('Sol', 20)

print (sol.nombre)
print (sol.edad)
