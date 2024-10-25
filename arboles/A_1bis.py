"""Ejercicio: Nivel de un nodo
Implementar una operación que, dado un valor o etiqueta de un nodo, devuelva cuál es el nivel
 del mismo dentro del árbol.

Ejercicio: Igualdad en árboles
Implementar la operación __eq__() para un árbol que permita identificar si dos árboles son iguales.

Ejercicio: Recorrido guiado
Implementar una función recursiva que, dado un árbol binario y una lista de instrucciones
 ('izquierda' o 'derecha') que conforma un camino guiado comenzando desde el nodo raíz, 
 devuelva el contenido del nodo que sea accesible utilizando el camino guiado."""

from typing import Generic, Optional, TypeVar

T= TypeVar('T')

class ArbolBinario(Generic[T]):
    def __init__(self, dato: T,
                  si: Optional["ArbolBinario[T]"] = None,
                    sd: Optional["ArbolBinario[T]"] = None):
        self.dato = dato
        self.si = si
        self.sd = sd
        