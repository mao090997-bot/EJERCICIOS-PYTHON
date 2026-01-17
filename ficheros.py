import os

"""
Ejercicios
"""

file_name ="oscarsolano.txt"

with open(file_name, "w") as file:
    file.write("oscar\n")
    file.write("28\n")
    file.write("Python")

with open(file_name, "r") as file:    
    print(file.read())
    
os.remove(file_name)


    


"""
Extra
"""

file_name = "oscarsolano23.txt"

open(file_name, "a")

while True:
    print("1.Añadir producto")
    print("2.Consultar producto")
    print("3. Actualizar producto")
    print("4. Borrar producto")
    print("5. Mostrar producto")
    print("6. Calcular venta total")
    print("7. Calcular la venta por producto")
    print("8. Salir")

    option = input("seleccione una opcion: ")

    if option == "1": 
        name = input("Nombre: ")
        quantity = input("Cantidad: ")
        price = input("precio: ")

        with open(file_name, "a") as file:
            file.write(f"{name}, {quantity}, {price}\n")


    elif option == "2":    
        pass
    elif option == "3":    
        pass
    elif option == "4":    
        pass
    elif option == "5":    
      with open(file_name, "r") as file:    
         print(file.read())
        
    elif option == "6":    
        pass
    elif option == "7":
        pass
    elif option == "8":    
        os.remove(file_name)
        break
    else: 
        print("Seleccione una opcion disponible")    