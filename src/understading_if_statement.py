cars = ['audi','bmw','chevrolet','corvette','tesla']
for car in cars:
    if  car =="bmw" or car== "tesla" or car == "audi":
        print(car.upper())
    else:
        print(car)

# Condicionales: El condicional es el corazón de un if
# Condicional True
car = "bmw"
print(car=="bmw") #Salida-> true
# Condicional False
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
# Multiple adicional 