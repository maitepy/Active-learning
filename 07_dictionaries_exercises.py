# 1 crear un diccionario
my_dict = {"Name": "maite", "Age": 43, "Country": "Spain"}
print(my_dict)

# 2 acceder a un valor 
print(my_dict["Name"])

# 3 añadir clave al diccionario
my_dict["job"] = "Programador"
print(my_dict)

# 4 modificar una entrada
my_dict["Age"] = 38
print(my_dict)

# 5 eliminar una clave
del my_dict["Country"]
print(my_dict)

# 6 crear un diccionario automatico
squares = {x: x**2 for x in range (1, 6)}
print(squares)
mine = {x: (x+1)*2 for x in range (1, 6)}
print(mine)

# 7 verificar si la clave existe
my_dict = {"Name": "maite", "Age": 43, "Country": "Spain"}
print("Name" in my_dict)

# 8 Imprimir las claves
print(my_dict.keys())

# 9 convertir claves en lista
my_list = list(my_dict)
print(my_list)
print(type(my_list))

# 10 crear un nuevo diccionario a partir de una lista

new_dict = dict.fromkeys(my_list, "desconocido")
print(new_dict)

