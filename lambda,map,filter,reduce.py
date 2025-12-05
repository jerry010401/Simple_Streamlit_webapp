#LAMBDA FUNCTIONS - THIS IS A ONE LINE CODE EXPRESSION AND ARGUMENTS.
# A lambda function is a small anonymous (or sometimes assigned) function that you can define in one line.
# lambda arguments : expression
from functools import reduce

add=lambda x,y : x+y  #add expression
print(add(5,8))

square = lambda x:x*x  #square expression
print(square(3))

sub=lambda a,b:a-b
print(sub(20,5))

cube = lambda y:y**y  #cube expression
print(cube(4))

mul = lambda e,f : e*f #mul expression
print(mul(3,7))

# MAP FUNCTION:-
#map(function, iterable) — applies the given function to every element of the iterable and returns a new iterable of results.
animals = ["lion","tiger","fox"]
result = list(map(lambda animal : animal.upper(),animals))
print(result)

fruits=["APPLE","BANANA","MANGO","ORANGE"]
result1 = list(map(lambda fruit : fruit.lower(),fruits))
print(result1)

# FILTER FUNCTION
# filter(function, iterable) — keeps only those elements for which the function returns True.


nums = [1,2,3,4,5,6,7,8,9,10]
even = list(filter(lambda x:x%2==0,nums))    # find the even numbers of the list.
print(even)

nums=[1,2,3,4,5,6,7,8,9,10]
odd = list(filter(lambda x:x%2==1,nums))   # find the odd numbers of the list.
print(odd)

nums1 = [-1,0,2,-5,7,-3,-8,4,1,9,6,-10]
positive_value = list(filter(lambda x:x>=0,nums1))  # find the positive numbers of the list.
print(positive_value)

nums1 = [-1,0,2,-5,7,-3,-8,4,1,9,6,-10]
negative_value = list(filter(lambda x:x<0 , nums1))  # find the negative numbers of the list.
print(negative_value)

# REDUCE FUNCTION:-
#reduce(function, iterable) — applies a function cumulatively on the iterable’s items to reduce them to a single value. This is available via the functools module.
# import the reduce function
num=[1,3,5,7,4]
sum = reduce(lambda a,b : a+b,num)     # reduce function helps to sum of the all number it gives the one number of output.
print(sum)

# 1+3 =4
# 4+5=9
# 9+7=16
# 16+4=20  # output = 20


num1=[22,46,7,34,77,32]
max_value = reduce(lambda a,b : a if a>b else b,num1)
print(max_value)

# 22>46=46
#46>7 = 46
#46>34=46
#46>77=77
#77>32 = 77    # output = 77

# PROBLEM-1
# find the expensive price and add the total amount....

prices=[270,480,1700,1450,1620,940]
expensive = list(filter(lambda x:x>1000,prices))  # filter the expensive price function
print(expensive)

total = reduce(lambda a,b:a+b,expensive)  # reduce to all functions to get total amount...
print(total)



