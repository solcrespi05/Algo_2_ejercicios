#ejercicio 1: nivel de un nodo. 
#Dado un árbol binario y un nodo, se pide implementar el método nivel que devuelve la distancia entre la raíz del árbol y el nodo.
#Ejemplo: en el árbol a de la imagen, nivel(a, 5) → 2, nivel(a, 10) → 3, nivel(a, 2) → 1
from typing import Generic, Optional, TypeVar

T = TypeVar('T')

class ArbolBinario(Generic[T]):  # Definir ArbolBinario primero para usarlo en NodoAB
    def __init__(self):
        self.raiz: Optional["NodoAB[T]"] = None
        self.antecesor: Optional["ArbolBinario[T]"] = None

    @staticmethod
    def crear_nodo(
        dato: T, 
        si: Optional["ArbolBinario[T]"] = None, 
        sd: Optional["ArbolBinario[T]"] = None
    ) -> "ArbolBinario[T]":
        t = ArbolBinario()
        t.raiz = NodoAB(dato, si, sd)
        if si is not None:
            t.raiz.si.antecesor = t
        if sd is not None:
            t.raiz.sd.antecesor = t
        return t

    def es_vacio(self) -> bool:
        return self.raiz is None

    def insertar_si(self, si: "ArbolBinario[T]"):
        if self.es_vacio():
            raise TypeError('Árbol vacío')
        self.raiz.si = si
        self.raiz.si.antecesor = self

    def nivel(self, dato: T) -> int:
        # Método que calcula la distancia entre la raíz y un nodo
        return self._nivel(self, dato, 0)

    def _nivel(self, arbol: Optional["ArbolBinario[T]"], dato: T, nivel_actual: int) -> int:
        if arbol is None or arbol.es_vacio():
            return -1
        if arbol.raiz.dato == dato:
            return nivel_actual
        # Buscar en el subárbol izquierdo
        nivel_izq = self._nivel(arbol.raiz.si, dato, nivel_actual + 1)
        if nivel_izq != -1:
            return nivel_izq
        # Buscar en el subárbol derecho
        return self._nivel(arbol.raiz.sd, dato, nivel_actual + 1)
    def __eq__(self, other: "ArbolBinario[T]") -> bool:
      if other is None or not isinstance(other, ArbolBinario):
        return False
      return self._iguales(self.raiz, other.raiz)

    def _iguales(self, nodo1: Optional["NodoAB[T]"], nodo2: Optional["NodoAB[T]"]) -> bool:
      if nodo1 is None and nodo2 is None:
        return True
      if nodo1 is None or nodo2 is None:
        return False
      return (nodo1.dato == nodo2.dato and 
            self._iguales(nodo1.si.raiz, nodo2.si.raiz) and 
            self._iguales(nodo1.sd.raiz, nodo2.sd.raiz))

class NodoAB(Generic[T]):
    def __init__(
        self, 
        dato: T, 
        si: Optional["ArbolBinario[T]"] = None, 
        sd: Optional["ArbolBinario[T]"] = None
    ):
        self.dato: T = dato
        self.si: "ArbolBinario[T]" = si if si is not None else ArbolBinario()
        self.sd: "ArbolBinario[T]" = sd if sd is not None else ArbolBinario()

# Ejemplo de uso
if __name__ == "__main__":
    # Crear el árbol
    a = ArbolBinario.crear_nodo(1)
    b = ArbolBinario.crear_nodo(2)
    c = ArbolBinario.crear_nodo(3)
    d = ArbolBinario.crear_nodo(4)
    e = ArbolBinario.crear_nodo(5)
    f = ArbolBinario.crear_nodo(6)
    g = ArbolBinario.crear_nodo(7)
    
    # Insertar hijos
    a.insertar_si(b)
    a.raiz.sd = c
    b.raiz.si = d
    b.raiz.sd = e
    c.raiz.si = f
    c.raiz.sd = g

    # Encontrar niveles
    print(f"Nivel de 5: {a.nivel(5)}")  # Debería devolver 2
    print(f"Nivel de 10: {a.nivel(10)}")  # Debería devolver -1 (no encontrado)
    print(f"Nivel de 2: {a.nivel(2)}")  # Debería devolver 1


#ejercicio 2 : igualdad de árboles
#Dado dos árboles binarios, se pide implementar el método iguales que devuelve True si los árboles son iguales y False en caso contrario.

# Crear dos árboles iguales
a1 = ArbolBinario.crear_nodo(1)
b1 = ArbolBinario.crear_nodo(2)
c1 = ArbolBinario.crear_nodo(3)
a1.insertar_si(b1)
a1.raiz.sd = c1

a2 = ArbolBinario.crear_nodo(1)
b2 = ArbolBinario.crear_nodo(2)
c2 = ArbolBinario.crear_nodo(3)
a2.insertar_si(b2)
a2.raiz.sd = c2

print(f"Árboles a1 y a2 son iguales: {a1 == a2}")  # Debería devolver True

# Crear un árbol diferente
d1 = ArbolBinario.crear_nodo(4)
a1.raiz.si.raiz.si = d1

print(f"Árboles a1 y a2 son iguales: {a1 == a2}")  # Debería devolver False
