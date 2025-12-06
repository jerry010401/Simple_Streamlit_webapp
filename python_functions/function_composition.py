#FUNCTION COMPOSITION:-

#Function composition means combining two (or more) functions so that the output of one function becomes the input of another.
#like f(g(x))
# Example:-

def add(x):
    return x+2    #f(x)=add()

def mul(x):
    return x*2    #g(x)=mul()

def composed(x):
    return add(mul(x))  #---> f(g(x)) --> add of (x+2)

print(composed(5))

