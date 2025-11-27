"""
El while es un ciclo controlado/ comando 
por condición.
La estructura básica de un while es: 
   while conditional:
     actions
"""
"""
 Programa si el usuario escribe un número 
 entre el 25 y 50, entonces estár dentro del rango 
 y salimos del while,
 del otro modo pedirle otro número 
"""
# While infinito
while True:
    try:
        number = int(input("Ingresar un número: "))

        if number >= 25 and number <= 50: 
            print("Estas dentro del rango, lo hicicte bien")
            break
        else:
            print("Esta fuera del rango, intentar otra vez")

    except ValueError:
        print("Se ha introduciodo una variable no valida")
    except KeyboardInterrupt :
        print("\nPrograma terminado por el usuario")
        break
print("Saliste del while")
