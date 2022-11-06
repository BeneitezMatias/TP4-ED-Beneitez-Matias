from python_ed_fcad_uner.data_structures import BinaryTreeNode,LinkedBinaryTree,LinkedQueue
from linkedBinaryTreeExtAbstract import LinkedBinaryTreeExtAbstract
from typing import Any, List, Union

from python_ed_fcad_uner.data_structures.linear.queues.linked_queue import LinkedQueue

class LinkedBinaryTreeExt(LinkedBinaryTree,LinkedBinaryTreeExtAbstract):
    
    def hermanos(self, nodo1 : BinaryTreeNode, nodo2: BinaryTreeNode) -> bool:
        resultado=False
        queue = LinkedQueue()
        queue.enqueue(self._root)
        
        while not queue.is_empty():
            current = queue.first()
                        
            if current.left_child:
                queue.enqueue(current.left_child)
                
            if current.right_child:
                queue.enqueue(current.right_child)

            if current.left_child==nodo1 and current.right_child==nodo2 or current.left_child==nodo2 and current.right_child==nodo1:
                resultado=True
            
            queue.dequeue() 
        return resultado
    
    def hojas(self) -> List[Any]:
        lista=[]
        queue = LinkedQueue()
        queue.enqueue(self._root)
        
        while not queue.is_empty():
            current = queue.first()
                        
            if current.left_child:
                queue.enqueue(current.left_child)
                
            if current.right_child:
                queue.enqueue(current.right_child)

            if current.left_child==None and current.right_child==None:
                lista.append(current.element)
            queue.dequeue()
        
        return lista

    def internos(self) -> List[Any]:
        lista=[]
        queue = LinkedQueue()
        queue.enqueue(self._root)
        
        while not queue.is_empty():
            current = queue.first()
            agrego=False            
            
            if current.left_child:
                hijo=current.left_child
                if hijo.left_child or hijo.right_child:
                    agrego=True
                    lista.append(hijo.element)
                queue.enqueue(current.left_child)
            
            
            if current.right_child: 
                hijo=current.right_child
                if hijo.left_child or hijo.right_child:
                    lista.append(hijo.element)     
                queue.enqueue(current.right_child)

            queue.dequeue()
        
        return lista
        
    def profundidad(self, nodo : BinaryTreeNode) -> int:
        resultado=0
        queue = LinkedQueue()
        queue.enqueue(self._root)

        while not queue.is_empty():
            current = queue.first()
            
            if current.__eq__(nodo):
                break
            
            resultado+=1
            
            if current.left_child:
                if current.left_child.__eq__(nodo):
                  break
                queue.enqueue(current.left_child)
                
            if current.right_child:
                if current.right_child.__eq__(nodo):
                    break
                queue.enqueue(current.right_child)
            
            queue.dequeue()
        
        return resultado
    
    def altura(self, nodo : BinaryTreeNode) -> int:
        resultado=0
        queue = LinkedQueue()
        queue.enqueue(self._root)
        
        while not queue.is_empty():
            current = queue.first()
            if current.__eq__(nodo):
                nodo_buscado=current
                break            
            if current.left_child:
                queue.enqueue(current.left_child)
                
            if current.right_child:
                queue.enqueue(current.right_child)

            queue.dequeue()
        
        queue2 = LinkedQueue()
        queue2.enqueue(nodo_buscado)
        hijos_derecha=0
        hijos_izquierda=0
       
        while not queue2.is_empty():
            current = queue2.first()
            if current !=nodo_buscado:
              hijos_izquierda+=1
            if current.left_child:
                queue2.enqueue(current.left_child)
            queue2.dequeue()
        
        queue2.enqueue(nodo_buscado)
        while not queue2.is_empty():
            current = queue2.first()
            if current !=nodo_buscado:
              hijos_derecha+=1    
            if current.right_child:
                queue2.enqueue(current.right_child)
            queue2.dequeue()
        
        if hijos_izquierda>=hijos_derecha:
            resultado=hijos_izquierda
        else:
            resultado=hijos_derecha 
        
        return resultado
