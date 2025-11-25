
# Jennyfer Rodriguez Ruiz
# 2530003
# IM-103

## Resumen ejecutivo 
#Una cadena en Python es una secuencia de texto (tipo 'str') y es inmutable: cualquier transformación
# devuelve una nueva cadena. Las operaciones básicas incluyen concatenación (+), repetición (*),
# medición de longitud con len(), segmentación (text[a:b]), indexación (text[i]) y métodos
# como lower(), upper(), strip(), replace(), split(), join(), startswith(), endswith().
# La validación y normalización de la entrada del usuario (strip(), lower()) previene errores e inconsistencias en los datos
# (p. ej., validación de correo electrónico, comprobación de contraseñas, detección de palíndromos). Este documento implementa
# seis problemas que demuestran la creación, lectura, indexación, segmentación, concatenación, búsqueda,
# reemplazo, división/unión y formateo de cadenas. Cada problema incluye descripción, entradas,
# salidas, validaciones y tres casos de prueba (normal, borde, error).

# Problem 1: Full name formatter (name + initials)
"""
Dado el nombre completo de una persona en una sola cadena (por ejemplo: "juan carlos tovar"), el programa debe:
1) Normalizar el texto (strip, espacios extra, mayúsculas/minúsculas).
2) Mostrar el nombre formateado en Title Case y las iniciales (por ejemplo: J.C.T.).

Entradas:
- full_name (string; nombre completo, puede venir en mayúsculas, minúsculas o mezclado, con espacios extra).

Salidas:
- "Formatted name: <Name In Title Case>"
- "Initials: <X.X.X.>"

Validaciones:
- full_name no debe estar vacío después de strip().
- Debe contener al menos dos palabras (por ejemplo, nombre y apellido).
- No aceptar cadenas que sean solo espacios.
"""
full_name = "Jennyfer Rodriguez   RUiz"
print(full_name)
Formatted_name = full_name.title()
print(Formatted_name) # Salida 
title_name = " ".join(Formatted_name for Formatted_name in Formatted_name)
print(title_name)

# Problem 2: Simple email validator (structure + domain)
"""
Descripción:
Valida si una dirección de correo tiene un formato básico correcto:
- Contiene exactamente un '@'.
- Después del '@' debe haber al menos un '.'.
- No contiene espacios en blanco.
Si el correo es válido, también muestra el dominio (la parte después de '@').

Entradas:
- email_text (string).

Salidas:
- "Valid email: true" o "Valid email: false"
- Si es válido: "Domain: <domain_part>"

Validaciones:
- email_text no vacío tras strip().
- Contar cuántas veces aparece '@'.
- Verificar que no haya espacios (no debe haber " " en email_text).

Operaciones clave sugeridas: strip(), count(), find(), slicing, in, not in.
"""
email_text = 'jenny@gmail.com'

# Problem 3: Palindrome checker (ignoring spaces and case)
"""
Descripción:
Determina si una frase es un palíndromo, es decir, se lee igual de izquierda a derecha y de derecha a izquierda, ignorando espacios y mayúsculas/minúsculas.

Ejemplos:
- "Anita lava la tina" -> palíndromo.
- "Hola mundo" -> no palíndromo.

Entradas:
- phrase (string).

Salidas:
- "Is palindrome: true" o "Is palindrome: false"
- (Opcional) Mostrar también la versión normalizada de la frase.

Validaciones:
- phrase no vacía tras strip().
- Longitud mínima razonable después de limpiar espacios (por ejemplo, al menos 3 caracteres).

Operaciones clave sugeridas: lower(), replace(" ", ""), slicing inverso text[::-1], comparación ==.
"""
# Problem 4: Sentence word stats (lengths and first/last word)
"""
Descripción:
Dada una oración, el programa debe:
1) Normalizar espacios (quitar espacios al principio y al final).
2) Separar las palabras por espacios.
3) Mostrar:
   - Número total de palabras.
   - Primera palabra.
   - Última palabra.
   - Palabra más corta y más larga (por longitud).

Entradas:
- sentence (string).

Salidas:
- "Word count: <n>"
- "First word: <...>"
- "Last word: <...>"
- "Shortest word: <...>"
- "Longest word: <...>"

Validaciones:
- Oración no vacía tras strip().
- Debe contener al menos una palabra válida después de split().

Operaciones clave sugeridas: strip(), split(), len(), recorrer la lista de palabras para encontrar mínima y máxima longitud.
"""

# Problem 5: Password strength classifier
"""
Descripción:
Clasifica una contraseña como "weak", "medium" o "strong" según reglas mínimas (puedes afinarlas, pero documéntalas en los comentarios).

Ejemplo de reglas:
- Weak: longitud < 8 o todo en minúsculas o muy simple.
- Medium: longitud >= 8 y mezcla de letras (mayúsculas/minúsculas) o dígitos.
- Strong: longitud >= 8 y contiene al menos:
  - una letra mayúscula,
  - una letra minúscula,
  - un dígito,
  - un símbolo no alfanumérico (por ejemplo, !, @, #, etc.).

Entradas:
- password_input (string).

Salidas:
- "Password strength: weak"
- "Password strength: medium"
- "Password strength: strong"

Validaciones:
- No aceptar contraseña vacía.
- Verificar longitud con len().

Operaciones clave sugeridas:
- Recorrer carácter por carácter.
- Métodos: isupper(), islower(), isdigit(), isalnum().
- Uso de banderas booleanas (has_upper, has_lower, etc.).
"""

# Problem 6: Product label formatter (fixed-width text)
"""
Descripción:
Dado el nombre de un producto y su precio, genera una etiqueta en una sola línea con el siguiente formato:
Product: <NAME> | Price: $<PRICE>
La cadena completa debe tener exactamente 30 caracteres:
- Si es más corta, rellena con espacios al final.
- Si es más larga, recorta hasta 30 caracteres.

Entradas:
- product_name (string).
- price_value (puede leerse como string o número; conviértelo a string para mostrarlo).

Salidas:
- "Label: <exactly 30 characters>"
(Puedes mostrar la etiqueta entre comillas para que se vean los espacios.)

Validaciones:
- product_name no vacío tras strip().
- price_value debe poder convertirse a un número positivo.

Operaciones clave sugeridas:
- Uso de f-strings o concatenación para formar la etiqueta base.
- len() para medir la longitud.
- slicing para recortar: label[:30].
- Relleno con espacios hasta alcanzar 30 caracteres.
"""
# CONCLUSION
# El manejo de cadenas es esencial en la entrada/salida, 
#ya que la mayoría de los datos de usuario son textuales y requieren normalización para evitar discrepancias
# (p. ej., diferencias entre mayúsculas y minúsculas, espacios adicionales).
# Use lower(), strip(), split() y join() para tareas típicas de normalización y análisis.
# Normalizar antes de comparar evita falsos negativos (p. ej., "Email@Example.com" vs. "email@example.com").
# Diseñar validaciones (no vacías, comprobaciones de formato) evita almacenar datos innecesarios y errores posteriores.
# La inmutabilidad de las cadenas significa que la segmentación y las modificaciones producen nuevas cadenas;
# esto es eficiente y seguro si se gestiona correctamente.