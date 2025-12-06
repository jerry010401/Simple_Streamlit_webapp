# HIGHER ORDER FUNCTION (HOF) IS A FUNCTION THAT EITHER:

# 1.TAKE ANOTHER FUNCTION IS AN ARGUMENT,OR -----> (PRE DEFINED LOGIC FUNCTIONS)
# 2. RETURNS A FUNCTION IT'S AN OUTPUT. ----> (THIS IS PREBOUND LOGIC FUNCTIONS)

# use to make a code more flexible,reusable and dynamic.

# 1. NORMAL WAY OF FUNCTION  OR TRADITIONAL FUNCTION WAY

"""
def build_email(username,provider):
    if provider == "gmail":
        return f"{username}@gmail.com"
    if provider == "ymail":
        return f"{username}@ymail.com"
    if provider == "hotmail":
        return f"{username}@hotmail.com"
    else:
        return f"{username}@example.com"

print(build_email("jerry","gmail"))
print(build_email("kalvin","ymail"))
print(build_email("edison","hotmail"))
print(build_email("akash","unknown"))

"""
from numpy.ma.core import inner

# 2.HIGHER ORDER FUNCTION TYPE-1
# PREDEFINED FUNCTION:-
# use to make a code more flexible,reusable and dynamic.
#TAKE ANOTHER FUNCTION IS AN ARGUMENT,OR -----> (PRE DEFINED LOGIC FUNCTIONS)

'''
def gmail_email(username,domain="gmail.com"):
    return f"{username}@{domain}"

def ymail_com(username,domain="ymail.com"):
    return f"{username}@{domain}"

def hotmail_email(username,domain="hotmail.com"):
    return f"{username}@{domain}"

def example_email(username,domain="example.com"):
    return f"{username}@{domain}"

def email(username,domain="rolex.com"):
    return f"{username}@{domain}"


def build_email(username,email_func):
    return email_func(username)

print(build_email("jerry",gmail_email))
print(build_email("kalvin",ymail_com))
print(build_email("edison",hotmail_email))
print(build_email("alice",example_email))
print(build_email("akash",email))
'''


# 3.HIGHER ORDER FUNCTION TYPE-2
# RETURNS A FUNCTION IT'S AN OUTPUT. ----> (THIS IS PREBOUND LOGIC FUNCTIONS)

def email_builder(domain):
    def build_email(username):
        return f"{username}@{domain}"
    return build_email

gmail=email_builder("gmail.com")
ymail=email_builder("ymail.com")
hotmail = email_builder("hotmail.com")
r_mail = email_builder("2006")

print(gmail("jerry"))
print(ymail("kalvin"))
print(hotmail("edison"))
print(r_mail("akash"))

# CLOSER FUNCTION

def outside(msg):
    def inside():
        return f"message is:{msg}"
    return inside()
reply=outside("Hii Hello,welcome to tvl!")
print(reply)




