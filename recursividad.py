"""
Recursividad Ejercicio.
"""
def countdown(number: int):
    if number >= 0: 
     print(number)
     countdown(number - 1)

    
countdown(100)


"""
EXTRA
"""

def factorial(num: int) -> int:
   if num < 0: 
      print("Los numeros negativos no son validos")
      return 0
   elif num == 0: 
      return 1
   return num * factorial(num - 1) #se llama a si misma

print(factorial(5)) 


def fibonaci (num: int) -> int:
   if num <= 0: 
      print("debe ser mayor a cero")
      return 0
   elif num == 1: 
      return 0
   elif num == 2: 
      return 1
   else: 
      return fibonaci(num - 1) + fibonaci(num - 2)
      
   
print(fibonaci(9))