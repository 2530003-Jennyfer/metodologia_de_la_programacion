# Funciones 
# Las funciones son bloques de cogido para realizar 
# una tarea en especifico 

# Cuando queremos realizar la tarea que se ha definido
# en la funcion, tenemos que llamar el nombre de la 
# función que realizar la acción
"""
Sintaxis de una función
def nombre_función():
    acciones

ejemplo: Vamos a definir una funcion que de un saludo a Christopher
"""
def gretting_christopher():
    """
    Funcion para llamar a una persona llamada Christopher
    """
    for i in range(0,5):
        print("Hello Christopher")

gretting_christopher()
"""
 Estroctura de una funcion
 def nombre_function:
    '''
    docstrings
    '''
    actions
"""
# Ejemplo de una función que genere el nombre completo de una persona y lo regrese.
def create_full_name(first_name, last_name, middle_name=""):
    full_name = f"{first_name.strip()} {middle_name.strip()} {last_name.strip()}".title()
    return full_name
first_name = input("Dame tu primer nombre: ")
middle_name = input("Dame tu segundo nombre: (Si no tienes segundo nombre dar enter) ")
last_name= input("Dame tu apellido: ")
gretting_fullname = create_full_name(
    first_name.lower(),
    last_name.lower(),
    middle_name.lower())
print(gretting_fullname)