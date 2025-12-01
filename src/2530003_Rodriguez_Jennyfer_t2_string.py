'''
Pro1
while True:
    temp = input("Ingrese la temperatura:  ")
    try:
        temp = float(temp)
        kelvin_temp = temp + 273.15
        fahrenheit = temp*(9/5)+32
        if kelvin_temp<=0:
            Print("Temperatura imposible")
            continue
        else:
            print(f"Temperatura en Fahrenheit es {fahrenheit}")
            print(f"Temperatura en kelvin es {kelvin_temp}")
            break
    except ValueError:
        print("La temperatura es imposible por reglas de termodinamica")
        continue
'''    

'''   
hours_worked = float(input("Horas trabajadas: "))
hourly_rate = float(input("Pago por hora: "))


if hours_worked < 0 or hourly_rate <= 0:
    print("Error: invalid input")
else:
    regular_hours = min(hours_worked, 40)
    overtime_hours = max(hours_worked - 40, 0)

    regular_pay = regular_hours * hourly_rate
    overtime_pay = overtime_hours * hourly_rate * 1.5
    total_pay = regular_pay + overtime_pay

    has_overtime = hours_worked > 40

    print("Regular pay:", regular_pay)
    print("Overtime pay:", overtime_pay)
    print("Total pay:", total_pay)
    print("Has overtime:", str(has_overtime).lower())
'''  

'''
total = float(input("Total de Compra: "))
is_student = input("Is he a student? ")
is_senior = input("is he a senior? ")
discount = False

if (is_student.upper() == "YES" or is_student.upper() == "NO") and (is_senior.upper() =="YES" or is_senior.upper()=="NO"):
    if is_senior.upper() == "YES" or is_student.upper() == "YES" or total>1000:
        discount = True
    
    if discount == True:
        print ("Discount Elegible")
        print (f"Total is {total * .9}")
    else:
        print ("Discount not elegible")
        print(f"Total is {total}")

else:
    print ("You are wrong")
'''
'''
n1 = input("Ingresa un número: ")
n2 = input("Ingresa un número: ")
n3 = input("Ingresa un número: ")

try: 
    n1=int(n1)
    n2=int(n2)
    n3=int(n3)

    sum_value = n1+n2+n3
    average_value = sum_value / 3
    maximo= max (n1, n2, n3)
    minimo = min(n1, n2, n3)
    if (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0):
        all_even= True

    print(f"La suma es: {sum_value}")
    print(f"El promedio es: {average_value} ")
    print(f"El maximo: {maximo}")
    print(f"El minimo: {minimo}")
    print(all_even)
except ValueError:
    print("Solo numeros")
'''

income= float(input("Set your income: "))
credit_score = int(input("Whats your credit score? "))
payment = int(input("whats your payment? "))

if income>0 and credit_score>0 and payment > 0:
    debt_ratio = income/payment

    print (debt_ratio)
    if income>8000 and debt_ratio>.4 and credit_score >=650:
        print ("Elegible for debt")
    else:
        print("Not elegible")
        


'''
weight_kg= float(input("Ingresa tu peso: "))
height_m= float(input("Ingresa tu altura: "))

if weight_kg > 0 and height_m > 0:
        
    weight_kg= weight_kg
    height_m= height_m
    bmi = weight_kg / (height_m * height_m)
        
    print(f"El bmi es: {bmi} ")
    if  bmi < 18.5:
        print("Underweight") 
    elif 18.5 <= bmi < 25.0:
        print("Normal") 
    elif bmi >= 25.0:
        print("overweight")
'''