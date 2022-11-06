from priorityQueueStack import PriorityQueueStack

pila=PriorityQueueStack()

pila.push(1,2)
pila.push(2,3)
pila.push(3,4)
pila.push(4,5)

print("===="*20)
print("pila completa tamaño:",len(pila),"\n",pila._data)
print("===="*20)
print("tope de la pila: ",pila.top())
print("===="*20)
print("quita y devulve el tope de la pila",pila.pop())
print("pila completa tamaño: ",len(pila),"\n",pila._data)
print("===="*20)
