"""
Ejercicios.7
"""
class Animal: 
    def __init__(self, name: str):
     self.name = name

    def sound(self):
       pass

#Subclases

class Dog(Animal): 
   
   def sound(self):
       print("Guau!")
 

  
class Cat(Animal): 
   
   def sound(self):
       print("Miau!")

def print_sound(animal: Animal):
   animal.sound()
 
my_animal = Animal("Animal")
print_sound(my_animal)

my_dog = Dog("Perro")
print_sound(my_dog)

my_cat = Cat("Gato")
print_sound(my_cat)
my_cat.sound()


"""
 Extra
"""   

class Employee: 
   
   def __init__(self, id: int, name: str):
      self.id = id
      self.name = name
      self.employees = []

   def add(self, employee):
      self.employees.append(employee)

   def print_employees(self):  
      for employee in self.employees:
         print(employee.name)

class Manager(Employee): 
   
   def coordinate_projects(self):
      print(f"{self.name} está coordinando proyectos")
   


class ProjectManager(Employee): 
   
   def __init__(self, id: int, name: str, project: str):
      super().__init__(id, name)
      self.project = project
   
   def coordinate_project(self):
      print(f"{self.name} está coordinando su proyecto")


class Programmer(Employee):     

   def __init__(self, id: int, name: str, language: str):
      super().__init__(id, name)
      self.language = language

   def code(self):
      print(f"{self.name} está programando en {self.language}")     
      
   
   def add(self, employee: Employee):
      print(f"Un programador no tiene {employee.name}")
   
my_manager = Manager(1, "oscar")
my_project_manager = ProjectManager(2, "frank", "Proyecto1")
my_project_manager2 = ProjectManager(3, "maricela", "Proyecto2")
my_programmer = Programmer(4, "Kontrol", "Swift")
my_programmer2 = Programmer(5, "Ros", "python")
my_programmer3 = Programmer(6, "all", "php")
my_programmer4 = Programmer(7, "bebe", "java")

my_manager.add(my_project_manager)
my_manager.add(my_project_manager2)

my_project_manager.add(my_programmer)
my_project_manager.add(my_programmer2)
my_project_manager2.add(my_programmer3)
my_project_manager2.add(my_programmer4)

my_programmer.add(my_programmer2)

my_programmer.code()
my_project_manager.coordinate_project()
my_manager.coordinate_projects()
my_manager.print_employees()
my_project_manager.print_employees()
my_programmer.print_employees()