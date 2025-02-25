# 1 personalizar saludo
def personalized_greeting(name = "stranger"):
    print(f"Hello {name}")

personalized_greeting("Maite")
personalized_greeting()

# 2 multiplicar
def multiply(number, number2):
    return(number * number2)
result = multiply(2, 5)
print(result)

# 3 saber si un número es par
def is_even(number):
    if number % 2 == 0:
        print(True)
    else:
        print(False)

is_even(5)

# 3 saber si un número es par en una linea
def is_even(a):
    return a % 2 == 0

print(is_even(4))

# 4 convertir a mayusculas
def convert_to_uppercase(text):
    return text.upper()

result = convert_to_uppercase("I'm learning Python")
print(result)

# 5 suma de numeros
def arbitrary_sum(*number):
    return sum(number)

result = arbitrary_sum(2, 5, 1, 10)
print(result)

# 6 saludo completo
def generate_full_greeting(name, surname):
    print(f"Hello {name} {surname}!")

generate_full_greeting("Maite", "Gómez")

# 7 elevar base al exponente
def power(base, exponent):
    return base ** exponent
    
result = power(2,3)
print(result)

# 8 promedio
def calculate_average(a, b, c):
    return a * b * c / 3

result = calculate_average(2, 3, 1)
print(result)

# 9 contar caracteres
def count_characters(text):
    return len(text)

result = count_characters("how many characters here")
print(result)

# 10 imprimir en mayusculas
def display_characters(*strains):
    for i in strains:
        print(i.upper())

display_characters("hello", "I'm learning", "Phython")