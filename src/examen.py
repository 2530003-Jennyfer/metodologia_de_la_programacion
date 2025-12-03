# Problema 2
width =  input("Set your width: ")
height = input("set your height: ")
try:
    width= int(width)
    height= int(height)
    if width>0 and height>0:
        area= (width*height)/2
        print(area)
        perimeter= height+width
        print(perimeter)
    else:
        print("Error")
except:
    print("error")


# preguta de rescaste
#user_number = input("Ingresa un numero")
#is not user_number.isdigit()

