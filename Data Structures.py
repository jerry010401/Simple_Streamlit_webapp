# 1.List Data structure:
from test_code import location

# create the list data of the collections:-

name_list=["Edison","Kalvin","Akash","Alice","Edison"] #family
food_list=["Parotta","Biryani","Chicken rice","Chapati"] #foods
fruits_list = ["Apple","Banana","Orange","Mango"] #fruits
play_list=["Shape of you","Nallai Allai","chinnamma","Stereo Hearts","Waving flag"]

"""
print(name_list)
print(food_list)
print(fruits_list)
"""

# 1.1 list properties.

"""
name_list.append("Sumathi")
print("After append ",name_list)
name_list.insert(2,"Jerry")
print("After insert",name_list)
name_list.remove("Kalvin")
print("After removing ",name_list)
name_list.pop()
print("After pop ",name_list)
name_list.reverse()
print("After reversing ",name_list)

print(name_list.count("Edison"))
print(name_list.index("Edison"))
"""

# Slicing the list collections:-
"""
print("Last 2 foods :",food_list[-2:])
print("First 3 names :",name_list[:3])
print("Get Two and Three fruits :",fruits_list[1:3])
"""

# List iteration

"""
print(play_list)

for name in name_list:
    print("Name:",name)
for play in play_list:
    print(play + " By Jerry")
for i in fruits_list:
    print("Fruit name :",i)
"""


#Check if the element
"""

if "Chapati" in food_list:
    print("Yes")
else:
    print("No")

if "Markku ma" in play_list:
    print("Yes")
else:
    print("No")

# Update the element in list. it means mutable list is a mutable data structure

print(play_list)
play_list[2]="Marakku ma"
print(play_list)

# List is a Heterogeneous data Structure.it means allows the multiple data type in the list.

details = ["Jerry",24,168,60,"Tirunelveli"]

for i in details:
    print(i)


my_list = ["Jerry",37,89,636,"Bangalore"]

for i in my_list:
    print(i)
"""


# How to find the index number using enumerator to elements.
"""
print(play_list)

for i,play in enumerate(play_list):
    print(f"Play list {i} : {play}")

print(fruits_list)

for i,fruit in enumerate(fruits_list):
    print(f"Fruit name {i} : {fruit}")

print(name_list)

for i,name in enumerate(name_list):
    print(f"birth order {i} : {name}")
"""

# Tuples Data Structure.

"""
trip_summary = ("Taxi","Chennai","Airport","Completed")

print(trip_summary)
"""

"""
for trip in trip_summary:
    print(trip)
"""

# print(trip_summary[1])

"""
print(trip_summary.count("Chennai"))
print(trip_summary.index("Airport"))
"""

# set data structure
"""
a={1,2,3,}
print(type(a))

taxi_cities_1 = {"Tirunelveli","Chennai","Bangalore","Mumbai","Tirunelveli"}
taxi_cities_2 ={"Tirunelveli","Madurai","Bangalore","Delhi"}
print(taxi_cities_1.union(taxi_cities_2))
# print(taxi_cities_1.intersection(taxi_cities_2))
# print(taxi_cities_1.difference(taxi_cities_2))
print(taxi_cities_2.difference(taxi_cities_1))

taxi_cities_1.add("Tuty")
print(taxi_cities_1)

taxi_cities_1.remove("Chennai")
print(taxi_cities_1)

my_list = {1,3,5,8}
my_list.add(6)
print(my_list)
my_list.remove(3)
print(my_list)

my_list.discard(6)
print(my_list)
"""

# Dictionary Data Structure
# Use List inside dict of the elements.
"""
my_details =[{
    "Name":"Jerry","Age":24,
    "Education":["M.Sc","B.Sc",12],
    "Status":"Completed",
    "Phone.No":9360835814},{
    "Name":"Kalvin","Age":26,
    "Education":["M.Sc","B.Sc",12],
    "Status":"Completed",
    "occupation":"Data Engineer"},{
    "Name":"Edison","Age":30,
    "Education":["Phd","B.Sc",12],
    "Status":"Completed",
    "occupation": "Priest"
   }
]

print(my_details)
"""

# print(my_details["Name"])
# print(my_details.get("Jerry")) # it gives "None" value....
"""
print(my_details.keys())
print(my_details.values())

for key,value in my_details.items():
    print(key,":",value)
    # print(f"{key} : {value}")

my_details.update({"Bike_model":"Hero"})
print(my_details)

my_details.update({"Bike_model":"R15"})
print(my_details)

my_details.pop("Status")
print(my_details)

for k,v in my_details.items():
    print(k,":",v)

print(my_details["Education"][2])

for i in my_details["Education"]:
    print(i)
"""
# Use dict inside dict value in the elements
brother_details ={
    "Jerry":{
    "Name":"Jerry","Age":24,
    "Education":["M.Sc","B.Sc",12],
    "Status":"Completed",
    "Phone.No":9360835814},
    "Kalvin":{
    "Name":"Kalvin","Age":26,
    "Education":["M.Sc","B.Sc",12],
    "Status":"Completed",
    "occupation":"Data Engineer"},
    "Edison":{
    "Name":"Edison","Age":30,
    "Education":["Phd","B.Sc",12],
    "Status":"Completed",
    "occupation": "Priest"
   }
}

# print(brother_details)

#print("Jerry Education :",brother_details["Jerry"]["Education"])
#print("Edison Education :",brother_details["Edison"]["Education"])


# print("Kalvin Occupation :",brother_details["Kalvin"]["occupation"])

for name,details in brother_details.items():
    print(name)
    print( details["Education"],"-->",details["Status"])



