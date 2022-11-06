from typing import Any
from python_ed_fcad_uner.data_structures import ArrayHeap

class HeapQueue(ArrayHeap):
    
    """estructura de tipo cola(FIFO) implementada con heap key=numero de ingreso
    """
    def __init__(self) -> None:
        super().__init__()
        self._key:int=0
        self._size:int=0
    
    def is_empty(self) -> bool:
        return self._size==0
    
    def enqueue(self,value: Any) -> None:
        self._key+=1
        super().add(self._key,value)
        self._size+=1
    
    def __len__(self) -> int:
        return self._size
    
    def dequeue(self) -> Any:
        if self.is_empty():
            raise Exception("Estructura vacía. No se puede continuar")
        resultado=super().min()
        super().remove_min()
        self._size -= 1
        return resultado
    
    

