# Empty Dictionary
homer_0 = {
    'color': 'yellow',
    'bag': 'maggie-bag',
    'hari': 'black', 
    'drees': 'green', 
    'mom': False}
#print(homer_0)
# print(type(homer_0))
marge = {
    'color': 'yellow',
    'bag': 'homer-donut', 
    ' hari': 'blue', 
    'drees': 'green', 
    'mom': True} 
print(marge['bag'])
alien_0 = {'color': 'yellow'}
print(alien_0['color'])
#Modifying an element of a dictionary 
alien_0['color']= 'blue'
print(alien_0)
# Adding elements to a dictionary 
alien_0['x_position'] =0
alien_0['y_position'] =25
alien_0['name']='Paul'
print(alien_0)
# Looping though items
print('\n Looping though items')
for key, value in alien_0.items():
    print(f'The key {key} has value {value}')
# looping though keys
print('\nLooping though keys')
for key in alien_0.keys():
    print(key)
# Looping thogh values
print('\n Looping though values')
for value in alien_0.values():
    print(value)

## Diccionarios 
covenant_grunt = {
    "color": 'orange',
    'weapon': 'plasma-gun',
    'armament': 'plasma-grande',
    'health': 2,
}

covenant_elite = {
    "color": 'blue',
    'weapon': 'plasma-gun',
    'armament': 'plasma-grande',
    'health': 7,
}

covenant_jackal = {
    "color": 'gray',
    'weapon': 'plasma-gun',
    'armament': 'plasma-grande',
    'health': 5,
}
convenants= [
    covenant_grunt,
    covenant_elite,
    covenant_jackal
]
for convenant in convenants:
    print('\n', convenant)
    for key, value in convenant.items():
        print(key, value)
# Lista de dicionario 
sutudents = {
    'santiago': ['reprobado', 'prepa1', 'rebelde']
    'jorge': ['aprobado', 'cbtis271', 'goleador']
    'Gabriel': ['aprobado', '119muerte', 'forite']
}
# Diccionario en diccionario 
## Estudiar el meteodo get en el diccionario
