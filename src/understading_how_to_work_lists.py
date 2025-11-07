"""
Recorrer una lista sin importar la cantidad 
de elementos que tenga.
"""

magicians = ["ron", "hermione", "harry", "hagrid", "cedrik"]
print(magicians[0], magicians[1])
for magician in magicians:
    print(magician)
    print(magician.upper())
    print(f"{magician.title()} es fue un gran hechizo.")
    print(f"{magician.lower()}No podemos esperar para ver tu siguiente hechizo")
print("Gracias a todos, fue un gran espetaculo")
"""
Identación: 
Python utiliza la identación para determinar
cuando una línea de código está conectada a 
la línea de código anterior.
Básicamente se utiliza espacios en blanco para 
obligarnos a escribir código ordenado y estrucurado.
"""
# No olvidemos identar
#Error de logica
magicians1 = ["alice", "david", "carolina"]
for magician1 in magicians1
    print(magician1)
print(f"I can't wait to see your next trick, {magician1.title()} ")
#Identación innecesaria
message = "Hola python"
print (message)

   
