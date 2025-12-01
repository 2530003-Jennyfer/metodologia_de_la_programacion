entrada = input("Ingresa una lista separada por comas: ")
isinlist = False

lista = entrada.strip().split(",")

New_Product = input("Ingresa un producto: ")

lista.append(New_Product)

Search_Item = input("Que producto quieres buscar? ")

for n in lista:
    if Search_Item == n:
        isinlist = True

if isinlist == True:
    print(f" {Search_Item} esta en la lista")
else:
    print(f"{Search_Item} no esta en la lista")

print(lista)
print(len(lista))

