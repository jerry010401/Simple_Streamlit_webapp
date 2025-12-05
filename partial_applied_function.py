#PARTIAL APPLIED FUNCTION:-
# normal function:-
from functools import partial
def calculate_price(base_price,tax_price):
    return base_price*(1+tax_price)
print(calculate_price(1000,0.18)) #1180.0
print(calculate_price(700,0.18))  #826.0

# define the original partial function...
# step-1---> import the partial function
# step-2----> create the function
def calculate_amount(base_amount,tax_amount):
    return base_amount * (1+tax_amount)

# step-2----> create partial applied function fixed with GST...
amount_with_gst = partial(calculate_amount,tax_amount=0.18)
print(amount_with_gst(100))  # 118.0
print(amount_with_gst(500))  #590.0
print(amount_with_gst(1000)) #1180.0

# problem-1 --> create the email with extension

def create_email(username,domain):
    return f"{username}@{domain}"

gmail = partial(create_email,domain= "gmail.com")
kmail = partial(create_email,domain = "kmail.com")

print(gmail("jerry1000"))  #jerry1000@gmail.com
print(kmail("edison123"))  #edison123@kmail.com