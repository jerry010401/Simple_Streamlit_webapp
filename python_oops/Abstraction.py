
from abc import ABC , abstractmethod

# Define the architect plan:-

class FeaturePlan(ABC):
    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def logout(self):
        pass

class Webapp(FeaturePlan):
    def enter(self):
        print("Enter the details!")
    def checkout(self):

        print("checkout it!")

    def login(self):
        print("Login successfully!")
    def logout(self):
        print("Logout successfully!")


w=Webapp()
w.enter()
w.login()
w.logout()
w.checkout()

