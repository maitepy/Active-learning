# 1 crear un set
my_set = {1, 2, 3, 4, 5}
print(my_set)
print(type(my_set))

# 2 añadir al set
my_set.add(6)
print(my_set)

# 3 no se repiten elementos
my_set.add(5)
print(my_set)

# 4 comprobar si hay un elemento
print(3 in my_set)

# 5 eliminar un elemento
my_set.remove(4)
print(len(my_set))
print(my_set)

# 6 vaciar set
my_set.clear()
print(len(my_set))

# 7 convertir set en lista
fruits = {"manzana", "naranja", "plátano"}
fruits_list = list(fruits)
print(fruits_list[0])

# 8 unión de sets
set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(set1.union(set2))
print(set1)

# 9 diferencia de sets
set1.add(4)
set2.add(3)
print(set1)
print(set2)
print(set1.difference(set2))
print(set2.difference(set1))
print(set1.symmetric_difference(set2))

# 10 eliminar un set
del my_set
print(my_set)
