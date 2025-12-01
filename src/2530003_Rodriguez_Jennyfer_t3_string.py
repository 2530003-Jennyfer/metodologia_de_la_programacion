'''
while True:
    numbers = input("limit: ")
    even_summed = 0
    Uneven_summed = 0
    try:
        numbers= int(numbers)
        if numbers>0:
            for num in range(1,numbers+1):
                Uneven_summed += num

            for even in range(1,numbers+1): 
                    if even % 2 == 0:  
                        even_summed += even
        else:
            print ("Write a positive number bigger than zero")
            continue

        print(f"Sum = {Uneven_summed}")
        print(f"Even summed is {even_summed}")
        break

    except ValueError:
        print("The number you wrote isnt a number")
        continue
'''

'''
base = input("Base: ")
m = input("Limit: ")

try:
    base = int(base)
    m = int(m)

    if m >= 1:
        for bas in range(1,m+1):
            print(f"{base} x {bas} = {base*bas}")
    else:
        print("impossible")
except ValueError:
    print ("Not good at all")
'''
