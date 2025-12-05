# Access specifier for variable:-

class Parent:
    def __init__(self):
        self.public_var = "I am Public"  #Public variable
        self._protected_var = "I am Protected"  #Protect variable
        self.__private_var = "I am Private"  #Private variable

    def access_from_sameclass(self):
        print("Access from same class:-")
        print("Public : ",self.public_var)
        print("Protect : ",self._protected_var)
        print("Private : ",self.__private_var)

class Child(Parent):
    def access_from_subclass(self):
        print("\nAccess from same class:-")
        print("Public : ", self.public_var)
        print("Protect : ", self._protected_var)
        try:
            print("Private : ",self._Parent__private_var) # Name Mangling method the variable can see the output. but is not a proper thing.
        except AttributeError:
            print("Cannot Access from subclass Attribute error")

class Stranger:
    def access_from_otherclass(self,obj):
        print("\nAccess from other class:-")
        print("Public : ",obj.public_var)
        print("Protect : ",obj._protected_var)
        try:
            print("Private :",obj.__private_var)
        except AttributeError:
            print("Cannot Access the class is an AttributeError")







p=Parent() # This is called object.
p.access_from_sameclass()

c=Child()
c.access_from_subclass()

s=Stranger()
s.access_from_otherclass(p)
