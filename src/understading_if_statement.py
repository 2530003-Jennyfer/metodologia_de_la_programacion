cars = ['audi','bmw','chevrolet','corvette','tesla']
for car in cars:
    if  car =="bmw" or car== "tesla" or car == "audi":
        print(car.upper())
    else:
        print(car)


# Condicional True
car = "bmw"
print(car=="bmw") #Salida-> true
# Condicional False solucion a la condicion falsa
car_2= 'Audi'
print(car_2=='audi')#Salida->False
#Condicional True
car_2= 'Audi'
print(car_2.lower()=='audi') #Salida-> true
# Condicional ! = para determinar desigualdad 
requested_tooping = "mushrooms" #->String
if requested_tooping != 'anchovies': # ->True
    print("Hold the anchovies")
# Comparaciones númericas 
# Condicionales numéricos 
age =18 #->int
print(age==18)#->true
answer =17
if answer != 42:
    print("Esa no es la respuesta correcta. Intenta otra vez.")
age =19
print(age<21)#True
print(age<=21)#True
print(age>21)#False
print(age>=21)#False
# Multiple condiciones 
age_0 = 22
age_1 =18
print("Multiple condiciones")
print("Operaciones and - pseint (O)")
print(age_0 >= 21 and age_1 >= 21)
print(age_0 >= 21 and age_1 >= 18)
age_0 = 22
age_1 =18
print("Multiple condiciones")
print("Operaciones or - pseint (O)")
print(age_0 >= 21 or age_1 >= 21)
print(age_0 >= 23 or age_1 >= 21)
# ¿Como nos preguntamos si algun valor está en una lista? 
print("\n A value is in a lista")
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)
# A value not in a list
banned_users = ["gabriel", 'max', ' adnrik', 'quevedo', 'christo']
user = "pedro"
print(user not in banned_users)
# Variables de tipo booleanos 
#game_ active =True 
#can_edit =False

"""
 If statment
 if condition: 
    do something 
if condition: 
    do something (true)
else: 
    do something (False)

"""
# Preguntar la edad del user y decirle si tiene la edad suficiente para votar
# input()
age = int(input("\nCual es tu edad: "))
print(f"\nTu edad es: {age}")
if (age) >=18:
    print("Tu tienes la edad para votar")
else:
    print("Lo siento, eres demasiado joven para votar")