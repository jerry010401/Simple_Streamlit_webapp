
"""
a = int(input("Enter the value a :"))
b = int(input("Enter the value b :"))

print(a + b)
"""

# test condition for email id creation

import sys

full_name = "".join(sys.argv[1:])

#format the email


email = full_name.lower() +"@company.com"

#output

print("\n ----My Profile----")
print("Fullname : ",full_name)
print("email : ",email)
