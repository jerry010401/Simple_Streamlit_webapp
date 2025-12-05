# Inheritance:-

# Inheritance

class Manager:
    def Management(self):
        print("Rules")
    def project(self):
        print("projects")



# example-1:-

class Dad:       # Parent class
    def house(self):
        print("Blue")
    def garden(self):
        print("Green")
class son(Dad):   # child class
    def factory(self):
        print("red")
    def house(self):
        print("Yellow")
    def apart(self):
        print("Gray")

s=son()
s.house()
s.apart()
s.garden()
s.factory()

# example-2:
class Employ(Manager):
    def plan(self):
        print("Ideas")
    def work(self):
        print("Dedications")
    def project(self):
        print("Project_1")

e1 = Employ()
e1.plan()
e1.work()
e1.Management()
e1.project()

# example-3:

from inheritance_1 import Animal


class ChildAnimal(Animal):
    def childDog(self):
        print("Child dog is eating milk")
    def dog(self):
        print("Rock")
    def character(self):
        print("Dog is Sleeping")

C=ChildAnimal()
C.dog()
C.childDog()
C.eat()
C.character()

class app1:
    def v1(self):
        print("I am version 1")
    def v2(self):
        print("I am version 2")

class app2(app1):
    def v3(self):
        print("I am version 3")
    def v4(self):
        print("I am version 4")
a=app1()
a.v1()
a.v2()

# Single level Inheritance.

class Dad:  # parent class
    def bike(self):
        print("Hero bike")
class son(Dad): # child class
    def cycle(self):
        print("Hercules cycle")

s=son()
s.bike()
s.cycle()

# Multilevel inheritance

class Grandpa:
    def car(self):
        print("U nova car")
    def home(self):
        print("Light House")

class Dad(Grandpa):
    def bike(self):
        print("Unicorn Bike")
    def garden(self):
        print("Green garden")

class Son(Dad):
    def cycle(self):
        print("Hero cycle")
    def bat(self):
        print("MRF bat")

s=Son()
s.home()
s.car()
s.bike()
s.bat()
s.garden()
s.cycle()


# Hierarchical Inheritance

class Dad: # parent class
    def house(self):
        print("Blue House")

class son1(Dad): # child 1 class
    def garden(self):
        print("Flower garden")

class son2(Dad): # child 2 class
    def factory(self):
        print("milk factory")

son_1 = son1()
son_1.garden()
son_1.house()

son_2 = son2()
son_2.factory()
son_2.house()

# Multiple Inheritance

class Dad:     #Parent class
    def House(self):
        print("red house")
class Mom:
    def shop(self):  # Parent class
        print("Medical Shop")

class daughter(Dad,Mom):  # child class
    def office(self):
        print("post office")

d=daughter()
d.House()
d.office()
d.shop()


# POLYMORPHISM

# * polymorphism is small topic in python .
# * it can use only overriding method .
# * it will not use overloading method.


