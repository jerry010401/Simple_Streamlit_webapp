
#✅ Pure Functions
# Always return the same output for the same input.
# pure = predictable and no side effects.

def add(a,b):
    return a+b
print(add(5,7))

# IMPURE FUNCTIONS
# OUTPUT MAY CHANGE EVEN WITH THE SAME OUTPUT
# impure = unpredictable,has side effects.
total = 0

def add(amount):
    global total     # side effects
    total += amount
    print("I am from add ",total)

def test():

    print("I am the total",total)

add(10)
test()

def greet(name="Jerry"):
    print(f"Hii i am {name}!")
greet()