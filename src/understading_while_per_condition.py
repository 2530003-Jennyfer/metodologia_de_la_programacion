"""
Vamos
"""
CORRECT_PIN = "1234"
MAX_ATTEMPTS = 3
attempt = 0
while attempt < MAX_ATTEMPTS:
    user_input = input("Ingresa tu PIN: ")
    if user_input == CORRECT_PIN:
        print("Acceso concedido")
        break
    else:
        attempt+=1
        reamining_attemps = MAX_ATTEMPTS -attempt
        if reamining_attemps > 0:
            print("Ingresa un pin valido")
            print(f"Te queda {reamining_attemps} intentos")
        else: 
            print("Cuenta bloqueada")
