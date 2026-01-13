"""
CLASES
"""

class Programer: 
    def __init__(self, name: str, age: int, language: list):
         self.name = name
         self.age = age
         self.language = language 
        
    def print(self):    
         print(f"nombre: {self.name} | Edad: {self.age} | Language: {self.language}")

my_programmer = Programer("Oscar",  36, ["Python", "Php"])
my_programmer.print()

# Extra

class stack: 
     def __init__(self):
          self.stack = []

     def push(self, item):
          self.stack.append(item)
          

     def pop(self): 
          if self.count() == 0: 
               return None
          return self.stack.pop()

     def count(self): 
          return len(self.stack)

     def print(self):      
          for item in reversed(self.stack):
               print(item)

my_stack = stack()
my_stack.push("A")
my_stack.push("B")
my_stack.push("C")
print(my_stack.count())
my_stack.print()
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()
print(my_stack.count())



#Fifo

class Queue:
     def __init__(self):
          self.queue = []

     def equeue(self, item):
          self.queue.append(item)

     def deequeue(self):
          if self.count() == 0:
               return None
          return self.queue.pop(0)          
      
     def count(self): 
        return len(self.queue)

     def print(self):      
          for item in reversed(self.queue):
               print(item)

my_queue = Queue()        
my_queue.equeue("A")
my_queue.equeue("B")
my_queue.equeue("C")
print(my_queue.count())
my_queue.print()
     