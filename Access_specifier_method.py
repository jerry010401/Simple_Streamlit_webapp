# Access specifier using for method

class Parent:
    def public(self):
        print("Public method!")
    def _protect(self):
        print("Protect method!")
    def __private(self):
        print("Private method!")

    def access_from_sameclass(self):
        print("\nAccess the same class:-")
        self.public()
        self._protect()
        self.__private()

class Child(Parent):

    def access_from_subclass(self):
        print("\nAccess the sub class:-")
        self.public()
        self._protect()
        try:
            self._Parent__private() # This is a name mangling method but is not correct thing.
        except AttributeError:
            print("Cannot access the private method (Attribute error)")

class Stranger:
    def access_from_otherclass(self,obj):
        print("\nAccess the stranger class:-")
        obj.public()
        obj._protect()
        try:
            obj.__private()
        except AttributeError:
            print("Cannot access the private method (Attribute error)")





p=Parent()
p.access_from_sameclass()

c= Child()
c.access_from_subclass()

s=Stranger()
s.access_from_otherclass(p)
