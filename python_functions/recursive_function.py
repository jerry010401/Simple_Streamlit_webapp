# RECURSIVE FUNCTIONS:-

# A RECURSIVE FUNCTION IS A FUNCTION THAT CALL ITSELF IN ORDER TO SOLVE A SMALLER VERSION OF THE SAME PROBLEM.

# example-1. 5!= 5*4*3*2*1 = 120

def factorial(n):   #5
    if n==1:        #5==1
        return 1
    return n*factorial(n-1) # 5*4*3*2*1=120

print(factorial(5))


# factorial(5)
# --> 5*factorial(4)
# --> 5*4*factorial(3)
# --> 5*4*3factorial(2)
# --> 5*4*3*2factorial(1)
# --> 5*4*3*2*1 = 120

#example-2

def countdown(n):
    if n == 0:
        print('BOOM')
        return None
    print(n)
    return countdown(n-1)
print(countdown(5))

#GENERATOR AND YIELD:-

# A generator function is a special type of function that use the yield keyword to return the values one by one,instead of returning everything at once.

def get_numbers(n):
    return [i for i in range(n)]
print(get_numbers(5))

def get_one_by_one(n):
    for i in range(n):
        yield i  # one by one iterable to pause number.

for num in get_one_by_one(10):
    print(num)
