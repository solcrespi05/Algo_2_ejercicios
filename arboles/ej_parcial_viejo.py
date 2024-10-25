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
        sd: Optional["ArbolBinario[T]"] = None,
        especial: bool = False
    ) -> "ArbolBinario[T]":
        t = ArbolBinario()
        t.raiz = NodoAB(dato, si, sd, especial)
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


    def preorder_especial(self) -> list[T]:
        resultado = []
        self._preorder_especial(self.raiz, resultado)
        return resultado
    
    def _preorder_especial(self, nodo: Optional["NodoAB[T]"], resultado: list[T]):
        if nodo is None:
            return
        resultado.append(nodo.dato)
        if not nodo.especial:
            self._preorder_especial(nodo.si, resultado)
            self._preorder_especial(nodo.sd, resultado)
    
    def es_especial(self) -> bool:
        return self._es_especial(self.raiz)
    
    def _es_especial(self, nodo: Optional["NodoAB[T]"]) -> bool:    
        if nodo is None:
            return True
        if nodo.especial:
            return self._es_especial(nodo.si) and self._es_especial(nodo.sd)
        return False
    
    def podado_especial(self) -> int:
        return self._podado_especial(self.raiz)
    def _podado_especial(self, nodo: Optional["NodoAB[T]"]) -> int:
        if nodo is None:
            return 0
        if nodo.especial:
            return self._contar_nodos(nodo.si.raiz) + self._contar_nodos(nodo.sd.raiz)
        return self._podado_especial(nodo.si) + self._podado_especial(nodo.sd)


    def _contar_nodos(self, nodo: Optional["NodoAB[T]"]) -> int:
        if nodo is None:
            return 0
        return 1 + self._contar_nodos(nodo.si) + self._contar_nodos(nodo.sd)
    

class NodoAB(Generic[T]):
    def __init__(self, dato: T,
                 si: Optional["ArbolBinario[T]"] = None,
                 sd: Optional["ArbolBinario[T]"] = None,
                 especial: bool = False):
        self.dato = dato
        self.si = si
        self.sd = sd
        self.especial = especial

# Crear árbol basado en el ejemplo del documento
arbol = ArbolBinario.crear_nodo(10)  # Raíz con valor 10
izq = ArbolBinario.crear_nodo(5)     # Hijo izquierdo con valor 5
der = ArbolBinario.crear_nodo(15, especial=True)  # Hijo derecho con valor 15 (especial)
izq_izq = ArbolBinario.crear_nodo(3)  # Hijo izquierdo de 5
izq_der = ArbolBinario.crear_nodo(7)  # Hijo derecho de 5

# Conectar nodos
izq.raiz.si = izq_izq
izq.raiz.sd = izq_der
arbol.raiz.si = izq
arbol.raiz.sd = der

# Preorder especial (debería ignorar los hijos de 15 porque es especial)
print("Preorder especial:", arbol.preorder_especial())  # Output esperado: [10, 5, 3, 7, 15]
