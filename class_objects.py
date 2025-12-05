
# 00PS CONCEPTS:-

# 1. create the class and objects

# use the constructor
class Student:
    def __init__(self,s_name,age,place,dept): #inside the paradise is called constructor.
        self.name = s_name
        self.age=age
        self.place = place
        self.dept = dept

    def display(self):
        print(f"Student name :{self.name},age : {self.age},dept : {self.dept} and place: {self.place}")

s1=Student("Jerry",24,"Tvl","PHY")
s2=Student("Kalvin",26,"Bang","DSC")
s3=Student("Edison",30,"Italy","PHI")

s1.display()
s2.display()
s3.display()


class Employ:
    def __init__(self,name,aadhaar): # This is constructor
        self.name = name
        self.aadhaar = aadhaar

    def enter_office(self):
        print(f" please entering your name {self.name}  and type your aadhaar number {self.aadhaar}.")

    def open_bank_account(self):
        print(f"Bank account is open for {self.name} with aadhaar number{self.aadhaar}")

e1=Employ("Jerry","3454-6756-8976")
e1.enter_office()
e1.open_bank_account()

# without constructor

class Mathtools:
    def square(self,n):
        return n*n
    def cube(self,n):
        return n*n*n
tool = Mathtools
print(tool.square(0,5))
print(tool.cube(0,3))

