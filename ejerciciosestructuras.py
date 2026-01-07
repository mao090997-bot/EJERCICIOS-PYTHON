# listas 

lista = ["oscar", "rosa", "liliana", "maricela", "cristian"]

lista.append("frank") #agregar elementos al final de la lista
print(lista)
lista.remove("oscar") #eliminar
print(lista)

print(lista[2]) #acceder a las listas 
lista[2] = "marlon" #actualizar o reemplazar elementos 
print(lista)
print(sorted(lista)) #ordena la lista devolviendo otra lista
lista.sort()
print(lista) #ordenar listas

# TUPLAS = son inmutables

tupla = ("23", "12", "56", "oscar")

print(tupla[3])
print(tupla[2])
tupla = tuple(sorted(tupla)) #convierte la tupla en lista y con tuple se convierte en tupla
print(type(tupla))
print(tupla)

# SETS
my_set = {"hola", "mauricio", "oscar"}
my_set.add("mao0909")#insercion
my_set.add("mao0909")#insercion no permite duplicados
my_set.remove("hola")

print(type(my_set)) #remueve elementos

print(my_set)
my_set = set(sorted(my_set)) #el set no es una estructura ordenada
print(type(my_set))
print(my_set)

#DICCIONARIOS. 

diccionario = {"name":"oscar", "edad": "16", 
               "apellido": "solano"} #diccionarios se usa con clave y valor y se separa con : 
print(diccionario["apellido"]) #para ingresar a elementos
diccionario["email"] = "mao090997"  #insertar elementos a dic
diccionario["name"] = "mauricio" #actualizar elementos

print(type(diccionario))
print(diccionario)