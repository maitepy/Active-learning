# 1 comprobar si el número es positivo negativo o cero
number = int(input("write a number: "))
if number < 0:
    print("negative number")
elif number == 0:
    print("cero")
else: 
    print("positive number")

# 2 mayor de edad o no
edad = int(input("How old are you?: "))
if edad < 18:
    print("Minor")
else:
    print ("Adult")
    
# 3 cadena de texto vacía
text = input("write a text: ")
if not text:
    print("The text is empty")
else:
    print("thank you!")

# 4 comparativa de dos inputs
number1 = int(input("Write a number: "))
number2 = int(input("Write other number: "))
if number1 > number2:
    print(f"{number1} is greater than {number2}")
if number1 < number2:
    print(f"{number2} is greater than {number1}")
if number1 == number2:
    print("both numbers are the same")

# 5 numero divisible
if number1 % 3 == 0 and number1 % 5 == 0:
    print(f"{number1} is divisible by 3 and 5")
else:
    print(f"{number1} is cannot be divided by 3 and 5")

# 6 numero par o impar
number3 = int(input("write a number: "))
if number3 % 2 == 0:
    print("even number")
else:
    print("odd number")

# 7 ¿puede votar?
if edad == 16 or edad == 17:
    print("you can vote with special permission")
elif edad >= 18:
    print("you can vote")
else:
    print("you cannot vote")

# 8 contraseña
password_try = input("password: ")
password = "psd24"
if password_try == password:
    print("correct")
else:
    print("error")

# 9 numero entre 10 y 20
if number1 <= 20 and number1 >= 10:
    print("the number is between 10-20")

# 10 semaforo
color = input("choose red, green or yellow: ")
if color == "red" or "Red" or "RED":
    print("STOP!")
elif color == "green" or "Green" or "GREEN":
    print("GO AHEAD!")
elif color == "yellow":
    print("pay attention")