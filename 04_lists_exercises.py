# 1 crear una lista
lista = [1,2,3,4,5]

# 2 accede e imprime el tercer elemento de la lista [10, 20, 30, 40, 50]
lista2 = [10, 20, 30, 40, 50]
print(lista2[2])

# 3 agregar a la lista
lista.append(6)
print(lista)

# 4 insertar en la lista
lista2.insert(2, 15)
print(lista2)

# 5 eliminar un valor
del lista2[2]
print(lista2)
lista2.insert(2, 30)
print(lista2)
lista2.remove(30)
print(lista2)

# 6 pop
print(lista)
lista.pop()
ultimo = lista.pop()
print(ultimo)

# 7 invertir lista
lista_cent = [100, 200, 300, 400, 500]
lista_cent.reverse()
print(lista_cent)

# 8 ordenar lista
lista_des = [3, 1, 4, 2, 5]
lista_des.sort()
print(lista_des)

# 9 concatenar listas
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2
print(list3)

# 10 crear sublista
print(lista2)
list = lista2[1:3]
print(list)