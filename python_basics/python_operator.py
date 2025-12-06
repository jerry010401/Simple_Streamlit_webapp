a=20
b=4

# Arithmetic operator
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b) #20*20*20*20

#Comparison operator

x=10
y=5
print(x==y)
print(x!=y)
print(x>y)
print(x<y)

#Logical operator

d=True
e=False

print(d and e)
print(d or e)
print(not d)

#Problems -1

amount= 1600
tax= amount * 0.18
total = amount + tax
print(total)

if total > 1500 :
    discount = total * 0.10
    total -= discount
print(total)

# problem -2

age = 24

student = "No"
unemployed= "Yes"

if age<25 and student == "No":
    print("Go to search for work")
elif age<25 and student == "Yes":
    print("Go to study")
else:
    print("Get a Job!")

