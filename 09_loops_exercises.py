print("exercise 1")

# 1 bucle números 1 - 10
number = 0
while number < 10:
    number += 1
    print(number)
print("exercise 2")    

# 2 bucle lista
my_list = [10, 20, 30, 40, 50]
for i in my_list:
    print(i)
print("exercise 3")    

# 3 bucle suma 1 al 100 REVISAR
i = 1
sumatorio = 0
while i <= 100:
    sumatorio += i
    i += 1
print(sumatorio)
print("exercise 4")

# 4 bucle "Python"
word = "Python"
for i in word:
    print(i)
print("exercise 5")

# 5 primer numero divisible por 7
i = 1
while i <= 50:
    i += 1
    if i % 7 == 0:
        print (i)
        break
print("exercise 6")

# 6 recorrer diccionario
dic = {"name": "Brais", "age": 37, "country": "Galicia"}
for i in dic:
    print(i)
print("exercise 7")

# 7 numeros pares
i = 1
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1
print("exercise 8")

# 8 usando range
ran = range(1, 11)
for i in ran:
    print(ran[-i])
    i += 1
print("exercise 9")

# 9 count
my_list = [30, 10, 30, 20, 30, 40]
counter = 0
for i in my_list:
    if i == 30:
        counter += 1
print(f"The number 30 appears {counter} times")
print("exercise 10")

# 10 detener el bucle
names = ["María", "Pedro", "Luisa", "Antonio", "Francisco", "Brais", "Maite", "Alejandra"]
for i in names:
    print(i)
    if i == "Brais":
        break
