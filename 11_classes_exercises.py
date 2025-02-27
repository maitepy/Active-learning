# 1 definir una clase
class Animal:
    def __init__ (self, species):
        self.species = species
    
    def make_sound(self):
        print("generic animal sound")

cat = Animal("cat")
Animal.make_sound(cat)
        
# 2 modificar la clase
class Animal:
    def __init__ (self, species):
        self.species = species
    
    def make_sound(self):
        if self.species == "cat":
            print("meow")
        elif self.species == "dog":
            print("woof")
        elif self.species == "cow":
            print ("moo")
        else:
            print("generic animal sound")

dog = Animal("dog")
cow = Animal ("cow")

Animal.make_sound(cat)
Animal.make_sound(dog)
Animal.make_sound(cow)

# 3 propiedad privada
class Car:
    def __init__(self, brand, model, speed):
        self.brand = brand
        self.model = model
        self.__speed = 0
 
    def print_car_data(self):
        print(f"{self.brand}, {self.model}, {self.__speed} km/h")

cars = [Car("Toyota", "Corolla", 180), 
    Car("Ford", "Mustang", 250), 
    Car("Tesla", "Model 3", 220), 
    Car("BMW", "M3", 280), 
    Car("Audi", "A4", 240)
]

for car in cars:
    car.print_car_data() #como __speed es una propiedad privada se mantiene en 0
print("modificamos velocidad")

# 4 modificar propiedad privada
class Car:
    def __init__(self, brand, model, speed):
        self.brand = brand
        self.model = model
        self.__speed = 0
 
    def print_car_data(self):
        print(f"{self.brand}, {self.model}, {self.__speed} km/h")
 
    def accelerate(self):
        self.__speed += 10
        
    def brake(self):
        self.__speed = max(0, self.__speed - 10)

cars = [Car("Toyota", "Corolla", 180), 
    Car("Ford", "Mustang", 250), 
    Car("Tesla", "Model 3", 220), 
    Car("BMW", "M3", 280), 
    Car("Audi", "A4", 240)
]
for car in cars:
    car.accelerate()
    car.accelerate()
    car.accelerate()
    car.brake()
    car.print_car_data()

# 5 
print("exercise 5:")
class Book:
    def __init__(self, title, author):
        self.title = title
        self.__author = author
 
    def get_author(self):
        return self.__author
 
    def change_title(self, new_title):
        self.title = new_title
        return new_title 
        

books = [Book("The Elements of Statistical Learning", "Trevor Hastie, Robert Tibshirani, Jerome Friedman"),
    Book("Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow", "Aurélien Géron"),
    Book("Python for Data Analysis", "Wes McKinney")
]

for book in books:
    print(book.get_author())

book = Book("The Elements of Statistical Learning", "Trevor Hastie, Robert Tibshirani, Jerome Friedman")
print(book.change_title("my book"))

# 6 nota media
class Student:
    def __init__(self, name, surname, califications):
        self.name = name
        self.surname = surname
        self.califications = califications
  
    def average(self):
        return sum(self.califications) / len(self.califications)
    
    
aida = Student("Aída", "García", [5, 7, 6, 9, 8, 7, 3])
aida_average = Student.average(aida)
print(f"{aida.name} {aida.surname}, calification: {aida_average:.2f}")

# 7  depositar y sacar dinero cuenta banco
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
 
    def add_money(self, income):
        self.balance += income
        print(f"your current balance is {self.balance}")
 
    def cash_out(self, outcome):
        if self.balance - outcome < 0:
            print(f"that amount exceeds the available balance in the account: {self.balance}")
        else:
            self.balance -= outcome
            print(f"your current balance is {self.balance}")

my_account = BankAccount("maite", 30)
my_account.add_money(100)
my_account.cash_out(100)
my_account.cash_out(80)

# 8 distancia entre dos puntos
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, x1, y1):
        return ((self.x-x1)**2 + (self.y-y1)**2)**0.5

point = Point(3, 7)
distance = point.distance(-2, 4)
print(distance)

# 9 salario por hora
class Employee:
    def __init__(self, name, hourly_wage, hours_worked):
        self.name = name
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked
        
    def salary(self):
        return self.hours_worked * self.hourly_wage

aida = Employee("aida", 10, 40)
print(aida.salary())

# 10 inventario
class Store:
    def __init__(self, inventory):
        self.inventory = inventory
        
    def add_product(self, product):
        self.inventory.append(product)
        
    def show_inventory(self):
        for i in self.inventory:
            print(i)

current_inventory = Store(["Apple", "Banana", "Pear"])
current_inventory.add_product("Chocolate")
current_inventory.show_inventory()