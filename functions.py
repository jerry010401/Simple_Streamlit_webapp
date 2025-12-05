
# create simple functions

def greet(name,age,location):
    print(f"Hii My name is {name.capitalize()} and I'm {age.__float__()} old . I'm from {location.capitalize()}")
greet("jerry",24,"tirunelveli")

# add function

def add(a,b):
    print(a+b)
add(3,5)

# sub function

def sub(c,d):
    print(c-d)
sub(5,2)


# Multiply function
def mul(x,y):
    print(x*y)
mul(7,5)

# div function

def div(e,f):
    print(e/f)
    print(e//f)
div(50,3)

# mod function

def mod(v,s):
    print(v%s)
mod(100,6)







def mul(g,h):
    return g*h
result_1 = mul(9,7)
print(result_1)

# create the function to call another file the functions.

# Use return function only that is why it works.

def add(u,w):
    return u+w

def details(name,age,location):
    return f"My name is {name}.I'm {age} years old and I'm from {location}."


# use *args function to use lots of arguments in one function

def add_1(*args):
    total=0
    for i in args:
        total+=i
    return total
print(add_1(1,2,5,4))


def sub_1(*args):
    total=1000
    for i in args:
        total-=i
    return total
print(sub_1(90,30,100,20))

def mul_1(*args):
    total = 1
    for i in args:
        total *=i
    return total
print(mul_1(2,3,7))

#use the Kwargs function

def create_profile(**kwargs):
    print("User Profile")
    for key,value in kwargs.items():
        print(f"{key}:{value}")
create_profile(name="Akash",age=19,oocupation="Student")

def my_list(name,age,location):
    print(f"Hii my name is {name}. and I'm {age} years old. currently i am living in {location}")
my_list("Jerry",24,"Bangalore")