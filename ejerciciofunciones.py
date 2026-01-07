"""
funciones definidas por el usuario
"""
#funcion simple 

def greet():
    print("hola, madre")
greet()

#funcion con retorno

def return_hola ():
    return "la vida es bella"
bella = return_hola()
print(return_hola()) #tambien se puede imprimir ingresando la funcion el print

#funcion con argumentos 
def colombia (a, b): #las funciones con parametros debe llevar letras, str, ni hacer operaciones
         return a + b
print(colombia(34, 67))

def saludo (name):
      print(f"hola {name}")
saludo("maravilloso")   

#con argumentos

def nombre (nombre, numero):
      return nombre * numero
print(nombre (34, 56))

#con un argumento predeterminado

def amor (name="oscar"):
      print(f"hola {name}")
amor()

#con argumentos y retorno

def hola (nombre, apellido):
      return f"{nombre}, {apellido}"
print(hola("oscar", "solano"))

#con retorno de varios valores

def multiple_return_greet():
      return "oscar", "solano"

nombre, apellido = multiple_return_greet()
print(nombre)
print(apellido)    

# con un numero variable de argumentos

def variable_arg_greet(*names):
      for name in names:
            print(f"hola, {name}")
variable_arg_greet("oscar", "mauricio", "solano", 345) #con esto se puede imprimir varios valores con * antes de parametro


#con un numero variable de argumentos con palabra clave
"""def variable_key_arg_greet(**names):
      for key, value in names.items:
            print(f"hola, {value} ({key})")
variable_key_arg_greet(
      languaje="oscar", 
      nombre="mauricio", 
      apellido="solano", 
      age=345)"""
"""
funciones dentro de funciones
"""

def outer_function():
      def inner_function():
            print("funcion interna: Hola, Python!")
      inner_function()
outer_function()      

"""
Funciones del lenguaje:
"""
print(len("oscar")) #cuenta numeros
print(type("oscar")) #tipo de datos
print(str(45)) #convierte a texto
print(abs(-56)) #da el valor absoluto, en positivo
print(round(67.56)) #redondea el numero al mas cercano
print(max(1,5,6)) #da el numero mayor
print(min(8,9,4)) #da el numero menor
print(sum([45, 67]))
print(sorted([34,45,67,43])) #ordena elementos
print(range(2,5)) #imprime un rango de numeros
print(zip([1,3,4]), ([34,56,78])) #une listas

"""
Variablles locales y globales

"""     

global_var = "python" #VARIABLE GLOBAL

print(global_var)

def hello_python():
      local_var = "Hola"
      print(f"{local_var}, {global_var}")
hello_python()

"""
Ejercicio

"""

def colombia (azul, blanco):
      cont = 0
      for i in range(1,101):
            if i % 3 == 0 and i % 5 == 0:
                  print(azul + blanco)
            elif i % 3 == 0:
                  print(azul)
            elif i % 5 == 0:
                  print(blanco)   
          
            else:      
                print(i) 
                cont += 1
      return(cont)          

print(colombia ("amor", "belleza"))       

