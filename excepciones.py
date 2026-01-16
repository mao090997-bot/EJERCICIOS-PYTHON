"""
Ejercicio
"""
try:
  
  print(10/1)

  my_list = [1,2,3,4]
  print(my_list[6])

except Exception as e: #asi se captura el error
  
  print(f"se ha producido un error: {e}")


"""
EXTRA
"""  

class StrTypeError(Exception):
   pass


def process_params(parameters: list):
  if len(parameters) < 3:
      raise IndexError()
  elif parameters[1] == 0:
     raise ZeroDivisionError
  elif type(parameters) == str: 
     raise StrTypeError("El segundo elemento")
     

  print(parameters[2])
  print(parameters[0]/parameters[1])
  print(parameters[2] + 5)

try:
  process_params([1, 2, "brais", 4, 5])  

except IndexError as e:
   print("se ha producido un error")

 
except ZeroDivisionError as e: 
   print("no puede ser cero")

except Exception as e: 
   print(f"se ha producido un error {e}")   

print("el programa finaliza")   