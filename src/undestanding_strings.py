"""
String variables
Un string es de manera sencilla una serie de caracteres. 
En Python, todo lo que se encuentre dentor de comillas
simples (' ') o dobles (" ") se considera un string.
Ejmplo: 
"Esto es un string"
'Esto también es un string'
'Le dije a un amigo "Python es mi lenguaje favorito" '
"El lenguaje 'Python' lleva el nombre por Monty Python, no por la serpientre "
""" 
name = "Clase de programacion"
print (name)
# title
print(name.title())
"""
Un método es una acción que python
puede realizar en un framento de datos 
o sobre una variable.
   El punto después de una variable
   seguido del método title() dice que
   se tiene que ejecutar el método title()
   de la variable name. 
Todos los métodos van seguidos de paréntesis
 porque en ocasiones necesitan información adicional 
 para fucionar, la cual ira dentro de los parétesis. 
 En esta ocación, el método, title() no requiere información 
 adicional para funcionar.
"""
print("Método upper: ", name.upper())
print("Método lower: ", name.lower()) 
# Concatenación de STRINGS
first_name = "charly"
last_name = "mercury"
full_name = first_name + " " + last_name
print(full_name)
print(full_name.title())
## Whitespaces
"""
Un whitespaces se refiere a cualquier caracter que no 
se imprime, es decir, un espacio, tabuladores y
finales de linea. LOs whitespaces se utilizan
comúnmente para organizar las salidas de tal manera
 que sea más amigable de leer o ver para el usuario.

"""
print("Whitespaces Tabulador")
print("Python")
print("\tPython")
print("\t\tPython")
print("Whitespace Salto de línea")
print("Languages: \n\tPython\nC\n\tJavascript")

## Eliminacion de espacioes en blanco 
proramming_languages = " Python "
print(proramming_languages.rstrip())
print(proramming_languages.lstrip())
print(proramming_languages.strip())
## Syntax Error con String
message = 'Una fortaleza de python es su comunidad'
print(message)
message = 'Una fortaleza de "python" es su comunidad'
print(message)