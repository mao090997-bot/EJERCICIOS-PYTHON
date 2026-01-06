"""
OPERADORES DE LENGUAJE 

"""
#operadores aritmeticos

print(f"suma:{10+4}")
print(f"resta: {12-4}")
print(f"multiplicacion: {4*8}")
print(f"division: {45/7}")
print(f"modulo: {45%4}") #modulo lo que queda de la division
print(f"exponente: {10 ** 2}")
print(f"division entera {34//4}") #lo que cabe en la division

#operadores de comparacion

print(f"igualdad {10 ==3}")
print(f"desigualdad {45 != 3}")
print(f"mayor que {45 > 3}")
print(f"menor que {45 < 3}")
print(f"mayor o igual que {45 >= 45}")
print(f"menor o igual que {45 <= 3}")

#operadores logicos

print(f"AND {23 + 56 == 34 and 23 < 12}")
print(f"OR {23 + 56 == 34 or 23 < 12}") #con cualquiera de las condiciones sale verdadero si es verdadero
print(f"NOT {not 12 == 5}")

#operadores de asignacion

my_numero = 11 #asignacion
print(my_numero)
my_numero += 1 #suma y asignacion
my_numero -= 1 
my_numero *= 1 
my_numero /= 1 
my_numero %= 1
my_numero **= 1 
my_numero //= 2

#operadores de identidad compara si dos variables son el mismo objeto

hola = my_numero
print(f"{hola is my_numero}")
print(f"{hola is not my_numero}")

#operadores de pertenencia 
print(f"{"o" in "oscar"}")
print(f"{"o" not in "oscar"}")

#operadores de bit

a = 10 
b = 3

"""
ESTRUCTURAS DE CONTROL
"""

# condicionales 

mao = "oscar"

if mao == "oscar solano":
    print(True)
elif mao == "solano":
    print("este es su apellido")
else:
    print("ingrese otro nombre")    

#iterativas

oscar = ["mao", "solano", "raquel"]

for nombre in oscar:
    if nombre == "bella":
     print("su nombre es mao")

    else: 
       contar = len(oscar) 
       print(contar)
oscar = 23
while oscar != 34:
   oscar += 1
   print(oscar)        

#manejo de excepciones

"""try:
   num1 = int(input("ingrese un numero: "))
   num2 = int(input("ingrese un numero: "))
   print(f"la suma es {num1+num2}")
except:
   print("ingrese un numero valido")
      
finally:
   print("que locura")"""


"""
EXTRA

"""
for numero in range(10, 56):
   if numero % 2 == 0 and numero != 16 and numero % 3 != 0:
      print(numero)

      

 
         