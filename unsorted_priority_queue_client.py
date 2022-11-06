from unsortedPriorityQueue import UnsortedPriorityQueue

cola= UnsortedPriorityQueue()

cola.add(1,2)
cola.add(0,3)
cola.add(3,4)
cola.add(6,5)

print("===="*20)
print("estructura completa cantidad de elementos: ",len(cola),"\n",cola._data)
print("===="*20)
print("elemento con el menor valor de clave: ",cola.min())
print("===="*20)
print("elimina de la estructura el elemento con menor valor de clave y lo devuelve \n",cola.remove_min())
print("estructura completa cantidad de elementos: ",len(cola),"\n",cola._data)
print("===="*20)

