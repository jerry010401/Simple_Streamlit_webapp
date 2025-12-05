# for loop functions.

names = ["edison","kalvin","jerry","akash","alice"]

for i in names:
    print(i.upper())


"""
names=[1,2,9,5,7,3,6,8,10,4]
for i in names:
    if i==3:
        break
    print(i)
"""
# find positive number using for loop anf if condition and continue statement
"""n=[9,3,-2,-6,-4,-8,9,6,3,16,17,15]

for i in n:
    if i<0:
        continue
    print(i)
"""

# find Negative number using for loop anf if condition and continue statement


num=[1,-3,-6,0,9,6,25,-4,-7,10,-8]

for i in num:
    if i>=0:
        continue
    print(i)


# While loop functions

"""
correct_pin = "12345"
entered_pin = ""

while correct_pin != entered_pin:
    entered_pin = input("Enter your correct pin :")
print("Access granted!")
"""

count=5

while count>0:
    print(f"Count down: {count}")
    count-=1
print("Time's Up!")


"""
items=[]

while True:
    add_item = input("Add item to type 'done' to finish")
    if add_item.lower()=="done":
        break
    items.append(add_item)
print("Items in cart :",items)
"""








# import and call the function one file to another file

"""
from functions import add

result = add(3,5)
print(result/4)

from functions import details

result = details("Alice",19,"Tirunelveli")
print(result)

"""
for i in range(0,5):
    print("Numbers : ",i)
    i+=1

i=1
while i<=5:
    print("Number:",i)
    i+=1

count=5

while count>0:
    print(f"count down : {count}")
    count-=1
print("Times Up!")