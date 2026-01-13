"""
Ejercicios
"""
# Pila/stack (lifo) #el ultimo en entrar es el primero en salir

stack = []
#push
stack.append("1")
stack.append("2")
stack.append("3")
print(stack)
#pop
stack_item = stack[len(stack) - 1] #Desapilar, sale el ultimo que entró
del stack[len(stack) - 1]

print(stack.pop()) # con pop desapilo listo

print(stack)

# Cola / (fifo) # el primero en entrar es el primero en salir

rabo = []
rabo.append(1)
rabo.append(2)
rabo.append(3)

print(rabo)

rabo_item = rabo[0]
del rabo[0]

print(rabo_item)

print(rabo.pop(0)) #desencola el elemento primero

"""
Extra

"""
# Web

def web_navegador():

    stack = []

    while True: 

        action = input("Añade una url o interactua con palabra adelante/atras/salir: ")

        if action == "salir":
            print("saliendo del navegador web")
            break

        elif action == "adelante":
            pass
        elif action == "atras": 
            if len(stack) > 0:         
             stack.pop()
        else:     
            stack.append(action)

        if len(stack) > 0: 
         print(f"Has navegado a la web: {stack[len(stack) - 1]}")
        else: 
            print("Estas en la pagina de inicio")
#web_navegador()


def printer():
   
   cola = []

   while True: 
      
    action = input("Añade un documento o selecciona imprimir/salir: ") 
    
    if action == "salir":
       break
    elif action == "imprimir": 
       if len(cola) > 0: 
        print(f"imprimiendo: {cola.pop(0)}")
    else: 
       cola.append(action)

    print(f"Cola de impresion {cola[len(cola) - 1]}")   

   
printer()   