from unsortedPriorityQueueAbstract import UnsortedPriorityQueueAbstract
from typing import Any, Tuple
from python_ed_fcad_uner.data_structures import PriorityQueueBase

class UnsortedPriorityQueue(UnsortedPriorityQueueAbstract,PriorityQueueBase):
    
    def __init__(self) -> None:
        self._data = []
    
    def __len__(self) -> int:
        return len(self._data)
    
    def is_empty(self)-> bool:
        return len(self) == 0

    def add(self, k: Any, v: Any) -> None:
        self._data.append(self._Item(k,v))

    def min(self) -> Tuple[Any]:
        if self.is_empty():
            raise Exception("estructura vacia. No se puede continuar.")
        
        primero=self._data[0]
        menor_clave=primero._key
        dato=primero
        for n in self._data:
            if n._key<menor_clave:
                menor_clave=n._key
                dato=n
                 
        return dato

    def remove_min(self) -> Tuple[Any]:
        if self.is_empty():
          raise Exception("estructura vacia. No se puede continuar.")
        
        primero=self._data[0]
        menor_clave=primero._key
        dato=primero
        for n in self._data:
            if n._key<menor_clave:
                menor_clave=n._key
                dato=n
        
        self._data.remove(dato)
        return dato
