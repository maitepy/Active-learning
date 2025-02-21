# 1 longitud
text = "Aprediendo Python"
print(len(text))

# 2 concatenación
print("hola " + "Python")

# 3 salto de línea
str_salto = "esta cadena\n tiene salto de linea"
print(str_salto)
str_nsalto = "esta cadena no tiene\\n salto de linea"
print(str_nsalto)

# 4 f-strings 
name, surname, age = "Maite", "Gómez", 43
print(f"My name is {name} {surname}, I am {age}")
print("my name is %s %s, I am %d" % (name, surname, age))

# 5 desempaquetar
word = "Python"
a, b, c, d, e, f = word
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# 6 slices
to_slice = "Programación"
sliced = to_slice[3:7]
print(sliced)
alternate = to_slice[1:8:3]
print(alternate)

# 7 invertir cadena 
inverted = to_slice[::-1]
print(inverted)

# 8 mayúsculas
text = "apendiendo python"
print(text)
print(text.endswith("n"))
print(text[-1])
print(text.capitalize())
print(text.upper())
text = text.upper()
print(text.lower())
print(text.endswith("N"))

# 9 count
text = "Programación en Python"
print(text.count("n"))

#10 es numerica
numeric = "12345"
print(numeric.isnumeric())