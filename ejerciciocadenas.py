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

print("oscar, {}, solano, {}".format(s1, s2)) #formatea cadenas, agregar


#interpolacion

print(f"saludo {s1}, oscar {s2}")

#Transformacion de lista de caracteres 
print(list(s2)) #crea listas

# Transformacion de listas en cadena 
l1 = [s1, ", ", s2, "!"]
print(" ".join(l1)) #une todos los strings y lo devuelve una sola cadena de texto, debe ser string

#Transformaciones numericas 

s4 = "123456"
print(int(s4)) #convierte a numeros enteros
print(float(s4)) #convierte a numeros float

#comprobaciones varias

print(s1.isalnum()) #comprobar si tiene letras o numeros
print(s1.isalpha()) #comprobar si tiene letras
print(s1.isnumeric()) #si son numeros
print(s1.isdigit()) #si son digitos 


"""
EXTRA 
"""
def check(word1: str, word2: str):
    # Palindromos

    print(f"¿{word1} es un palindromo?: {word1 == word1[::-1]}")
    print(f"¿{word2} es un palindromo?: {word2 == word2[::-1]}")

    # Anagramas

    print(f"¿{word1} es anagrama de {word2}?: {sorted(word1) == sorted(word2)}")
    
    # Isogramas
    def isogram(word: str) -> bool: 

        word_dict = dict()

        for character in word:
         word_dict[character] = word_dict.get(character, 0) + 1

        isograma = True
        values = list(word_dict.values())
        isograma_len = values[0]
        for word_count in values:   
          if word_count != isograma_len: 
            isograma = False
            break
        return isograma

    print(f"¿{word2} es un isograma?: {isogram(word2)}") 

     
    



check("radar", "pythonpythonpythonpython")


