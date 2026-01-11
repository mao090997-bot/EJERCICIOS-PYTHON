"""
Valor y referencia 

"""

# Tipos de datos por valor
"INT,  FLOAT, ST, BOOL"
my_int_a = 10
my_int_b = 20

print(my_int_a)
print(my_int_b)

# Tipo de datos por referencia 

#List, dict, set, tuple, objetos personalizados

my_list_a = [10, 20]
my_list_b = [30, 40]
print(my_list_a)
print(my_list_b)

#funciones con datos por valor 
my_int_c = 10

def my_int_func(my_int: int):
    my_int = 20
    my_int_c = 30 #no lo va a modificar porque es inmutable la variable
    print(my_int)

my_int_func(my_int_c)    
print(my_int_c)

#funciones con datos por referencia 



def my_list_func(my_list: list):
    my_list_e= my_list
    my_list.append(30)

    my_list_d = my_list_e
    my_list_d.append(40)

    print(my_list)
    print(my_list_d)

my_list_c = [10, 20]
my_list_func(my_list_c)  
print(my_list_c)    

# por valor

hola = 10
bebe = 20

def value(valor1: int, valor2: int) -> tuple:
    temp = valor1
    valor1 = valor2
    valor2 = temp
    return valor1, valor2

valor3, valor4 = value(hola, bebe)

print(f"{hola}, {bebe}")
print(f"{valor3}, {valor4}")
    