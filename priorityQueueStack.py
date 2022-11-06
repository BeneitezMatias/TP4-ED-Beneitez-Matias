from typing import Any
from unsortedPriorityQueue import UnsortedPriorityQueue

class PriorityQueueStack(UnsortedPriorityQueue):
    """estructura de tipo Pila implementada con una cola de prioridad sin ordenar
    """
    def __init__(self) -> None:
        super().__init__()
        self._size: int = 0
    
    def __len__(self)-> int:
        return self._size
    
    def push(self, k: Any, v: Any) -> None:
        """Agrega un elemento al final de la estructura
        """
        super().add(k,v)
        self._size+=1

    def top(self):
        """devuelve sin quitar el elemento en el tope de la pila
           Arroja excepcion si la pila esta vacia 
        """
        if self.is_empty():
            raise Exception("estructura vacia. No se puede continuar.")
        
        return self._data[-1]
        
    def pop(self):
        """devuelve y quita el elemento en el tope de la pila
           Arroja excepcion si la pila esta vacia 
        """
        if self.is_empty():
            raise Exception("estructura vacia. No se puede continuar.")
        
        a_borrar=self._data[-1]
        self._data.remove(a_borrar)
        self._size-=1
        
        return a_borrar


    def is_empty(self) -> bool:
        return super().is_empty()