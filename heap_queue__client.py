from heapQueue import HeapQueue

cola=HeapQueue()

cola.enqueue(8)
cola.enqueue(3)
cola.enqueue(4)
cola.enqueue(5)
cola.enqueue(6)

print("===="*20)
print("cola completa tamaño:",len(cola),"\n",cola._data)
print("===="*20)
print("quita y devuelve el elemento que entro primero",cola.dequeue())
print("===="*20)
print("cola completa tamaño:",len(cola),"\n",cola._data)
print("===="*20)
