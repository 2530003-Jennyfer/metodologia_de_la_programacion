"""
 squares =[]
 for value in range(0,11)
    square = value**2
    square.append(square)
print(square)
"""
"""
Una lista comprehention combina el ciclo for
y la creación de nuevos elementos en una sola 
liena y automaticamente agrega cada nuevo element 
a la lista, es decir, sin utilizar el método append.
"""
square = [value**2 for value in range(0,11)]
# Para los números pares entre el 0 y el 100
square_range = [value for value in range(0,101,2)]
evens_if = [value for value in range(0,101) if value%2==0]
print(evens_if)