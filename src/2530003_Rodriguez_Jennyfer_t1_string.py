"""
Manejo de strings en Python 
Jennyfer Rodriguez Ruiz
2530003
 IM-103
"""
Resumen ejecutivo 
Una cadena en Python es una secuencia de texto (tipo 'str') y es inmutable: cualquier transformación
devuelve una nueva cadena. Las operaciones básicas incluyen concatenación (+), repetición (*),
medición de longitud con len(), segmentación (text[a:b]), indexación (text[i]) y métodos
como lower(), upper(), strip(), replace(), split(), join(), startswith(), endswith().
La validación y normalización de la entrada del usuario (strip(), lower()) previene errores e inconsistencias en los datos
(p. ej., validación de correo electrónico, comprobación de contraseñas, detección de palíndromos). Este documento implementa
seis problemas que demuestran la creación, lectura, indexación, segmentación, concatenación, búsqueda,
reemplazo, división/unión y formateo de cadenas. Cada problema incluye descripción, entradas,
salidas, validaciones y tres casos de prueba (normal, borde, error).
"""
# Problem 1: Full name formatter (name + initials)
"""
Given a person's full name in a single string (for example, "juan carlos tovar"), the program should:
1) Normalize the text (strip, extra spaces, uppercase/lowercase).
2) Display the formatted name in the Title Case and the initials (for example, J.C.T.).
Inputs:
- full_name (string; full name, can be in uppercase, lowercase, or mixed case, with extra spaces).
Outputs:
- "Formatted name: <Name In Title Case>"
- "Initials: <X.X.X.>"
Validations:
- full_name must not be empty after strip().
- It must contain at least two words (for example, first and last name).
- Strings consisting only of spaces are not acceptable.
"""
full_name = input("introduce your full name\n")
list=full_name.split()
if full_name.isspace() or len(list)<2 : 
    print ("invalid input please reset the program.")
else:
    name_lower =full_name.lower().split() 
    formatted_name= " "
    for names in name_lower: 
        formatted_name = formatted_name + " " + names 
    print(f"formatted name :{formatted_name.title().strip()}") 
    initials=" "
    for word in formatted_name.title():
        if word.isupper(): 
            initials= initials +"."+  word 
    print (f"initials: {initials.strip('.')}") 
"""
Test cases
1) Normal
Input: "juan carlos tovar"
Output:
formatted name : Juan Carlos Tovar
initials: J.C.T

2) Border
Input: " jen   fer "
Output:
formatted name : Ana Lu
initials: A.L

3) Error
Input: "     Taylor"
Output:
invalid input please reset the program.

"""
# Problem 2: Simple email validator (structure + domain)
"""
Description:
Validates whether an email address has a correct basic format:
- Contains exactly one '@'.
- There must be at least one period (.) after the '@'.
- Contains no spaces.
If the email is valid, it also displays the domain (the part after the '@').
Inputs:
- email_text (string).
Outputs:
- "Valid email: true" or "Valid email: false"
- If valid: "Domain: <domain_part>"
Validations:
- email_text is not empty after strip().
- Count how many times '@' appears.
- Verify that there are no spaces (there should be no spaces in email_text).
Suggested key operations: strip(), count(), find(), slicing, in, not in.
"""
mail = input("set your e-mail\n")
mail = mail.strip(" ")#normalizamos las entradas
lenght = len(mail)#contamos la longitud del mensaje
num = mail.find("@")#buscamos un @
point = mail.find(".",num) # buscamos un . despues de el @
if "@" not in mail or num > point or mail.count("@")>1 or " " in mail or lenght == 0 or point== lenght-1:#verificamos que tenga @que el punto este despues de @ ylas demas condiciones
    email = False 
    print (f"valid e-mail:{email}")
else :
    email = True
    print(f"valid e-mail:{email}")
    print (mail [num:lenght])
"""
Test cases
1) Normal
Input: "usuario@gmail.com"
Output:
valid e-mail: True
@gmail.com

2) Border
Input: "  a@b.co  "
Output:
valid e-mail: True
@b.co

3) Error
Input: "user@@mail.com"
Output:
valid e-mail: False

"""
# Problem 3: Palindrome checker (ignoring spaces and case)
"""
Description:
Determines whether a phrase is a palindrome, meaning it reads the same backward as forward, ignoring spaces and case.
Examples:
- "Anita lava la tina" -> palindrome.
- "Hola mundo" -> not a palindrome.
Input:
- phrase (string).
Output:
- "Is palindrome: true" or "Is palindrome: false"
- (Optional) Also display the normalized version of the phrase.
Validations:
- phrase not empty after strip().
- Minimum reasonable length after clearing spaces (e.g., at least 3 characters).
Suggested key operations: lower(), replace(" ", ""), reverse slicing text[::-1], comparison ==.
"""
word = input ("set your palindrome \n")
if word.strip().isspace()or len(word.strip())<3:#preguntamos si la palabra es espacio o si su longitud es menor a 3 caracteres
    is_palindrome= False 
else:
    word="".join(word.lower().strip().split())#unimos todo e ignoramos los espacios
    word2 = word[::-1]#ordenamos la palabra al revez ahora sin espacios
    if word2 == word: #compara las dos strings resultantes
        is_palindrome =True
    else:
        is_palindrome = False
print(f"is palindrome:{is_palindrome}")
"""
1) Normal
Input: "Anita lava la tina"
Output:
anitalavalatina
anitalavalatina
is palindrome: True

2) Border
Input: "A b A"
Output:
aba
aba
is palindrome: True

3) Error
Input: "  a "
Output:
is palindrome: False

"""
# Problem 4: Sentence word stats (lengths and first/last word)
"""
Description:
Given a sentence, the program should:
1) Normalize spaces (remove leading and trailing spaces).
2) Separate words with spaces.
3) Display:
- Total number of words.
- First word.
- Last word.
- Shortest and longest words (by length).
Input:
- sentence (string).
Output:
- "Word count: <n>"
- "First word: <...>"
- "Last word: <...>"
- "Shortest word: <...>"
- "Longest word: <...>"
Validations:
- Sentence must not be empty after `strip()`.
- Must contain at least one valid word after `split()`.
Suggested key operations: `strip()`, `split()`, `len()`, traversing the word list to find the minimum and maximum lengths.
"""

lid input please retry")
else:
    phrase= phrase.strip()
    word_count= phrase.split()
    for word in word_count:#busca palabra por palbra 
        num=len(word)# iguala la longitud de la palabra a una variable
        if longest < num:#si numero es mayor a longest
            longest = len(word) #el valor de num pasa a ser el valor de longest
            longest_word= word #la palabra se guarda en la variable longest_word
    for word in word_count:#busca en todas las palabras 
            short =len(word)# el valor de len es igual a la longitud de la palabra
            if shortest>short:#si shortest es mayor a short
                 shortest= short #el valor de shortest pasa a ser short
                 shortest_word= word # el valor de word se guarda en la variable shortest word
    print(f"your word count is {len(word_count)}")
    print(f"your first word is {word_count[0]}")
    print(f"your last word is {word_count[-1]}")
    print(f"your longest word is {longest_word} with a lenght of {longest}")
    print(f"your shortest word is {shortest_word} with a lenght of {shortest}")
"""
1) Normal
Input: "  the quick brown fox jumps  "
Output:
the quick brown fox jumps
your word count is 5
your first word is the
your last word is jumps
your longest word is jumps with a lenght of 5
your shortest word is the with a lenght of 3

2) Border
Input: "hello"
Output:
hello
your word count is 1
your first word is hello
your last word is hello
your longest word is hello with a lenght of 5
your shortest word is hello with a lenght of 5

3) Error
Input: "      "
Output:
invalid input please retry

"""
# Problem 5: Password strength classifier
"""
Description: 
This tool classifies a password as "weak," "medium," or "strong" based on minimal rules (you can refine these rules, but please document them in the comments).

Example rules:
- Weak: Length < 8, all lowercase letters, or very simple.
- Medium: Length >= 8 and a mix of uppercase and lowercase letters or digits.
- Strong: Length >= 8 and contains at least:
- one uppercase letter,
- one lowercase letter,
- one digit,
- one non-alphanumeric symbol (e.g., !, @, #, etc.).
Input:
- password_input(string).
Output:
- "Password strength: weak"
- "Password strength: medium"
- "Password strength: strong"
Validations:
- Do not accept empty passwords.
- Verify length using len().
Suggested key operations:
- Traversing character by character.
- Methods: isupper(), islower(), isdigit(), isalnum().
- Use of boolean flags (has_upper, has_lower, etc.).
"""
password=input("please set your password\n")
size= len(password) 
print(size)
is_strong= False
has_upper=False
has_lower=False
has_num=False
has_special=False
if size==0:#evalua que la contraseña no este vacia
    print ("must set a password, please retry")
elif size<8:#si la contraseña tiene menos de 8 caracteres te dice que es debil
     print("your password is weak")
elif size>=8:#si tu contraseña supera los 8 caracteresevalua las demas caracteristicas que pide
    for character in password:
        if character.isupper():
            has_upper=True
        elif character.islower():
            has_lower=True
        elif character.isdigit():
            has_num=True
        elif not character.isalnum():
            has_special=True
    if has_upper==True and has_lower==True and has_num==True and has_special== True:#si lo tiene todo es fuerte
        is_strong=True
    if is_strong== True:#si es fuerte imprimir password is strong
        print("password strenght:strong" )
    elif has_upper==True and has_lower==True or has_num==True:
        print("password strength:medium")#si no tiene todas las caracteristicas es medium
    
    else:
        print("password strength:medium")
"""
1) Normal
Input: "Abc123$X"
Output:
8
password strenght:strong

2) Border
Input: "Abcdefgh"
Output:
8
password strength:medium

3) Error
Input: ""
Output:
0
must set a password, please retry

"""
# Problem 6: Product label formatter (fixed-width text)
"""
Description:
Given a product name and its price, generate a single-line label with the following format:
Product: <NAME> | Price: $<PRICE>
The complete string must be exactly 30 characters:
If it's shorter, pad with trailing spaces.
If it's longer, truncate it to 30 characters.
Inputs:
product_name (string).
price_value (can be read as a string or a number; convert it to a string to display it).
Outputs:
"Label: <exactly 30 characters>"
(You can display the label in quotes to show the spaces.)
Validations:
- product_name must not be empty after strip().
- price_value must be convertible to a positive number.
Suggested key operations:
- Use f-strings or concatenation to form the base label.
- len() to measure the length.
- Slicing to trim: label[:30].
- Padding with spaces to reach 30 characters.
"""
name=input("please set your product:\n")
price= input("please set the price\n")
data = (f"product: {name.strip()} | price: ${price.strip()}") #normaliza todo quitando espacios y lo ingresa al formato indicado
try:#intenta convertir la 2da entrada en float y evaluar  que el 1er caracter
    cost=float(price)
    if cost <0 or len(name.strip())==0 or not name.strip().isalpha():#evaluaque el nombre sea alfanumerico y que el costo sea mayor a 0
        print("please set a valid number or name")
    else:
        if len(data)==30:#evaluan que el string sea de 30 caracteres
            print(f"label:'{data}'")
        elif len(data)>30:#si el dato es mayor a 30 lo recorta hasta que tenga 30 caracteres
            print(f"label:'{data[:30]}'")
        elif len(data)<30:#si el dato es menor a 30 le agrega espacios hasta que lleguen a los 30 caracteres
            while len(data)<30:
                data=data+" "
            print(f"label:'{data}'")
except ValueError:# 
    print("please set a valid number")
"""
1) Normal
Input:
name = "Laptop"
price = "12999"
Output:
label:'product: Laptop | price: $12999   '

2) Border
Input:
name = "USB"
price = "99"
Output:
label:'product: USB | price: $99       '

3) Error
Input:
name = "  "
price = "500"
Output:
please set a valid number or name

4) Error (price no numérico)
Input:
name = "Mouse"
price = "abc"
Output:
please set a valid number


"""

# CONCLUSION
"""
String handling is essential in input/output,
since most user data is textual and requires normalization to avoid discrepancies 
(e.g., case differences, extra spaces).
Use lower(), strip(), split(), and join() for typical normalization and parsing tasks.
Normalizing before comparing avoids false negatives (e.g., "Email@Example.com" vs. "email@example.com").
Designing validations (non-empty, format checks) avoids storing unnecessary data and subsequent errors.
String immutability means that slicing and modifications produce new strings;
this is efficient and safe if handled correctly.
"""