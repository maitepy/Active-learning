# 1 crear e imprimir tupla
tupla = (10, 20, 30, 40, 50)
print(tupla)

# 2 mostrar elemento
print(tupla[1])

# 3 intentar modificar
# tupla[0] = 10 error

# 4 contar
tupla2 = (1, 2, 3, 3, 4, 5, 3)
print(tupla2.count(3))

# 5 encontrar indice
texto_tupla = ("Java", "Python", "Javascript"," Python")
print(texto_tupla.index("Python"))

# 6 concatenar tuplas
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
suma = tupla1 + tupla2
print(suma)
print(type(suma))

# 7 subtupla
print(tupla[2:4])

# 8 convertir en lista
colores_tupla = ("rojo", "verde", "azul")
colores_lista = list(colores_tupla)
colores_lista[1] = "amarillo"
print(colores_lista)
print(type(colores_lista))
colores_tupla2 = tuple(colores_lista)
print(colores_tupla2)
print(type(colores_tupla2))

# 9 eliminar tupla
my_tuple = colores_tupla2
print(my_tuple)
del my_tuple
# print(my_tuple) da error

# 10 crear tupla con solo un elemento
tupla_uno = (100, )
print(tupla_uno)
print(type(tupla_uno))
print(len(tupla_uno))