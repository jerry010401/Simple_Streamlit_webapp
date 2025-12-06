# create,and write the file code

file=open("notes.txt", "a")
file.write("This is file handling file page!\n")
file.write("Welcome to the page!\n")
file.write("Add a new line\n")
file.write("This is a new line!")
file.close()



# read and print the file code.
file=open("notes.txt", "r")
content=file.read()
print("File content:\n",content)
file.close()

"""
fruit_name = input("Enter your fruit :")

with open("data.txt","a") as file:  # "a" means append the file.
    file.write(fruit_name+ "\n")

    print("Your fruit added!")


with open("data.txt","r")as file:  # "r" means read only the file.
   for _ in range(7):   #  "_" This is called throw away variable.
       print(file.readline().strip())


with open("file.txt","w") as file:   # "w" means overwrites or create the file.
    file.write("This is our file Page!\n")
"""

with open("file.txt", "r")as file:
    while True:
        line=file.readline()   # if read to fetch the data you can use readline() function.
        if not line:
            break
        if "INFO" in line:
            print("Found info:",line.strip())

with open("file.txt", "r") as file:
    for _ in range(8):                 #  "_" This is called throw away variable.because we have to get the integer value so this is called pagination.
        print(file.readline().strip())


#CREATE THE CSV FILE AND READ,WRITE THE LINE ONE FILE TO ANOTHER FILE.

with open("input_file.csv", "r") as infile,open("output_file.csv", "w") as outfile:
    for line in infile:
        print(line.strip())
        outfile.write(line)


# import csv module and use to get the particular data in the file.using dict
"""
import csv

with open("input_file.csv","r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["age"])
"""

with open("input_file.csv", "r") as file:
    lines = file.readlines()  # this function use to read the all the columns.
    for line in lines[1:]: # skip header
        columns = line.strip().split(",")
        print(columns[2])
