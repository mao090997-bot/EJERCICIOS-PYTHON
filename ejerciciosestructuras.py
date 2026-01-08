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
del diccionario["apellido"] #borrar elementos
diccionario = dict(sorted(diccionario.items())) # Ordenación
print(type(diccionario))
print(diccionario)

"""
Extra

"""

def my_agenda():
  
  agenda = {}

  def insertar_contacto():
     telefono = input("ingrese numero de telefono: ")
     if telefono.isdigit() and len(telefono) > 0 and len(telefono) <= 11: 
        agenda[nombre] = telefono
     else: 
      print("Debes introducir un numero con menos de 12 digitos") 

  while True: 

    print("")
    print("1. Buscar contacto")
    print("2. Insertar contacto")
    print("3. Actualizar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")

    opcion = input("\nSelecciona una opcion: ")

    match opcion:
        case "1":
          nombre = input("Ingrese el nombre del contacto: ")
          if nombre in agenda:
             print(f"el numero de telefono de {nombre} es {agenda[nombre]}")
             
          else:
              print(f"el nombre {nombre} no lo hemos encontrado")  
          
        case "2":
          nombre = input("Ingrese el nombre del contacto: ")
          
          insertar_contacto()

        case "3":
          nombre = input("Introduce nombre a actualizar: ")
          if nombre in agenda:
           insertar_contacto()
          else: 
            print(f"el contacto {nombre} no existe")

          
        case "4":
          nombre = input("Ingrese el nombre del contacto a eliminar: ")
          if nombre in agenda:
             del agenda[nombre]
             

          else: 
             print("ingrese contacto valido")
        case "5":
            print("Saliendo de la agenda")
            break
        case _:
            print("Opcion no valida. Elige una opcion del 1 al 5")


my_agenda()