"""
Las listas también pueden alamcenar 
números y de echo, son ideales para esto.
Python ofrecen una gran cantidad de 
herramientas que ayudan a trabajar
eficientemente listas de números. 
"""
# Método built-in range()
"""
El método range() nos ayudan a crear fácilmente 
series de números
Ejemplo:
"""
print("Números del 0 al 9")
for value in range(10): # 10 números entre 0-9
    print(value)
print("Números del 1 al 9")
for value in range(1,10): # 10 números entre 1-9
    print(value)
print("Números impares del 1 al 9")
for value in range(1,10,2): # 10 números entre 0-9
    print(value)
odd_numbers = list(range(1,10,2))
print(odd_numbers)
print("Números pares del 1 al 9")
for value in range(0,10,2): # 10 números entre 0-9
    print(value)
even_numbers = list(range(0,10,2))
print(even_numbers)
print("Tabla del 9 ")
for value in range(0,91,9): 
    print(value)
tabla_del_9 = list(range(0,91,9))
print(tabla_del_9)
# Cuadrados de los 10 primeros números 
squares = []
for number in range(1,11):
    square = number**2
    squares.append(square)
print(squares)
# Más métodos buil
# metodo min()
digits =[1,2,3,4,5,6,7,8,9,0]
print(min(digits))#Salida:0
# Metodo max()
digits =[1,2,3,4,5,6,7,8,9,0]
print(max(digits))#Salida:9
# Metodo sum()
digits =[1,2,3,4,5,6,7,8,9,0]
print(sum(digits))#Salida:45