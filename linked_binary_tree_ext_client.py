from python_ed_fcad_uner.data_structures import BinaryTreeNode
from linkedBinaryTreeExt import LinkedBinaryTreeExt

nodo_a = BinaryTreeNode('A')
nodo_b = BinaryTreeNode('B')
nodo_c = BinaryTreeNode('C')
nodo_d = BinaryTreeNode('D')
nodo_f = BinaryTreeNode('F')
nodo_g = BinaryTreeNode('G')
nodo_h = BinaryTreeNode('H')
nodo_i = BinaryTreeNode('I')
nodo_k = BinaryTreeNode('K')
nodo_m = BinaryTreeNode('M')
nodo_n = BinaryTreeNode('N')

arbol = LinkedBinaryTreeExt()

arbol.add_left_child(None, nodo_a)
arbol.add_left_child(nodo_a, nodo_b)
arbol.add_right_child(nodo_a, nodo_f)
arbol.add_left_child(nodo_b, nodo_c)
arbol.add_right_child(nodo_b, nodo_d)
arbol.add_left_child(nodo_f, nodo_g)
arbol.add_right_child(nodo_f, nodo_k)
arbol.add_left_child(nodo_g, nodo_h)
arbol.add_right_child(nodo_g, nodo_i)
arbol.add_left_child(nodo_k, nodo_m)
arbol.add_right_child(nodo_k, nodo_n)
print(arbol)

print("===="*20)
print("lista de hojas: ",arbol.hojas())

print("===="*20)
print(nodo_m,"y",nodo_n,"¿son hermanos? ",arbol.hermanos(nodo_m,nodo_n))
print(nodo_b,"y",nodo_n,"¿son hermanos? ",arbol.hermanos(nodo_b,nodo_n))
print("===="*20)

print("profundidad del nodo",nodo_d,": ",arbol.profundidad(nodo_d))
print("profundidad del nodo",nodo_a,": ",arbol.profundidad(nodo_a))

print("===="*20)
print("lista de nodo internos: ",arbol.internos())
print("===="*20)
print("altura del nodo",nodo_a,": ",arbol.altura(nodo_a))
print("altura del nodo",nodo_m,": ",arbol.altura(nodo_m))
print("===="*20)
