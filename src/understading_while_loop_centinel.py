"""
 Docstring for understading_while_loop_centinel
 Un programa que:
   -cuente cunatos números ha ingresado el usuario
   -realice la suma de éstos números
   -me diga cuál es el mínimo de los números ingresados
   -me diga cuál es el maximo de los números ingresados
"""
counter = 0 
sum_quantitis = 0.0
minium = None
naximum = None

while True :
    print("Escribe exit para salir")
    user_input = input("Ingresa una cantida (MXN): ")
    
    if user_input == 'exit' :
        break
    
    try:
        value = float(user_input)
    except ValueError:
        print("Caracter invalido. Por favor ingres un número")
    except KeyboardInterrupt:
        print("Slida manual")
    counter+=1 #Counter = conuter + 1 (contador)
    sum_quantitis += value #sum_quantitis = sum_quantitis + value (sumador)
    if minimum is None or value < naximum:
        minimum = value
    if minimum is None or value > maximo
    naximum = value 
print("cantidad de números ingresados", counter)
print("Suma de los numeros ingresados", sum_quantitis)
print("Minimo de los numeros ingresados", minimum)
print("Maximo de los numeros ingresados", naximum)
