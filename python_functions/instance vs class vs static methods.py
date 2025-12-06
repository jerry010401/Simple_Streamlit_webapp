# INSTANCE Vs CLASS Vs STATIC METHODS:-


class myclass:

    def instance_method(self):      # normal or instance method
        print("This is an Instance method!")

    @classmethod
    def class_method(cls):         # class method
        print("This is a class method!")

    @staticmethod
    def static_method():          # static method
        print("This is a static method!")

m = myclass()
m.instance_method()
myclass.class_method()
myclass.static_method()

#------------------------------

# 1. CLASS METHOD

# if have using will not create the object in the class

class Company:
    company_name = "ZOHO"  # class level data

    @classmethod
    def change_name(cls,new_name):
        cls.company_name = new_name

Company.change_name("GOOGLE")
print(Company.company_name)    # output GOOGLE


# STATIC METHOD

# if have using will not create the object in the class

class Math:

    @staticmethod
    def mul(x,y):
        return x*y
    @staticmethod
    def div(a,b):
        return a//b
    @staticmethod
    def add(c,d):
        return c+d
    @staticmethod
    def sub(v,w):
        return v-w



print(Math.mul(5,6))  # 30
print(Math.div(20,4))  # 5
print(Math.add(4,6))   # 10
print(Math.sub(70,30))  # 40

# Difference between class method and static method......

class Company:

    company_name = "GOOGLE"

    @classmethod
    def company_change_name(cls,new_name):
        cls.company_name = new_name

    @staticmethod
    def try_change_name(try_new_name):
        company_name = try_new_name

Company.company_change_name("ZOHO")  # insert function name
Company.try_change_name("META")      # insert function name

print("After classmethod :",Company.company_name)  # insert variable name  # ZOHO
print("After staticmethod :",Company.company_name) # insert variable name  # ZOHO











