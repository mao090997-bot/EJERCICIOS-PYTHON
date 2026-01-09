"""
Operaciones
"""
s1 = "Hola"
s2 = "python"
# concatenacion

print( s1 + " " + s2 + "!") #concatenar textos con +

# Repeticion 
print(s1 * 3) #repetir

#indexacion 

print(s1[0:2] + s2[2:3]) #ingresar a cadenas de texto

#longitud 
print(len(s2))

#slicing(porcion)
print(s2[2:5]) #por porciones ingresa
print(s2[2:5]) #por porciones ingresa

#busqueda
print("a" in s1)
print("h" in s2) # con busqueda en in

#reemplazar 
print(s2.replace("p", "h")) #para reemplazar 

#division
print(s2.split("t")) # corta las cadenas de texto

#conversion a mayusculas y minusculas

print(s2.upper())
print(s1.lower())
print("oscar solano".title()) #pone las primmeras letras en mayus
print("oscar solano".capitalize()) #la primera letra en mayus

#eliminacion de espacios al principio y final
print(" oscar solano ".strip()) #elimina espacios

#Busqueda al principio y al final
print(s1.startswith("Ho")) #pregunta si empieza con ese texto
print(s1.endswith("Ho")) #pregunta si termina con ese texto

#encontrar la posicion
print("oscar mauricio solano solano".find("solano")) #te dice donde empieza la palabra requerida

#busqueda de ocurrencias
print("oscar".count("c")) #cuenta cuantos elementos hay

#formatear cadena

print("oscar, {}, solano, {}".format(s1, s2))
