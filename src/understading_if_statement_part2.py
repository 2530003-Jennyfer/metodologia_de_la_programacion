age = 0

try:
    age = int(input("Escribe tu edad: "))
    

except:
    age = -1
    print("Error, ingresaste un caracter no válido")
# 
if age >= 100:
    print("Tienes más de un siglo")
elif age>=18 and age <100 :
        print("Eres mayor de edad")
elif age >=0 and age < 18:
     print("Eres menor de edad")
else: 
    print("Tuviste un error")
       
print("Holi charly")

# Actividad 
age = 0 
try: 
    age = int(input("Ingresa la edad: "))
except:
    age= -1
    print("Error, ingresaste un caracter no válido")
if age <= 4 and age >=0: 
    print("La entrada es gratuita")
elif age <18 and age >4: 
    print("La entrada cuesta $200")
elif age >= 18: 
    print("La entrada cuesta $400")
else: 
    print("Error")
# Multiple if 
guisos = ["asado", 'salsa verde', 'pozole', 'deshebrada']
if 'asado' in guisos:
    print("Si hay asado")
else:
    print("No hay asado")
if 'tamales' in guisos:
    print('Si hay tamales')
else:
    print('no hay tamales')
if 'salsa verde' in guisos:
    print("Si hay salsa verde")
else:
    print("No hay salsa verde")

guiso =[]
if guiso:
    print("Hay guisos")
#Utilizando varias listas 
guisos_disponibles = ['salsa verde','deshebrada','mole']
guisos_a_ordenar = ['deshebrada', 'caldo de iguana']
print("¿Que guisos desea ordenar?")
for guis in guisos_a_ordenar:
    print(f'deseo {guisos_a_ordenar}')
    if guis in guisos_disponibles:
        print(f"si tenemos {guis}")
    else:
        print("No tenemos ese guiso")
print("Realizando pedido...")

