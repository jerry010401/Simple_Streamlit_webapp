#variables

#L--E--G--B

# L= Local variables

def purchase():
    shoes="puma shoes" # Local variable
    print("Your shoes is : ",shoes)
purchase()

# E= Enclosing variables

def order():
    price=700 #Enclosed variable
    def checkout(): #nested function
        print("Your shoes price is :",price)
    checkout()
order()

# G=Global variables

my_page = "Jerry01" #Global variable

def page():
    print("Welcome to the page :",my_page)
def homepage():
    print("Your home page is :",my_page)
page()
homepage()

#B-built in variable

print(__file__)

# over all use case function


delivery_partner = "Zometo"

def hotel():
    item="Pizza"
    def order():
        quantity = 3
        print(f"your order is {quantity} {item} using {delivery_partner}")
    order()
hotel()

def restarunt():
    food="Biriyani"
    def order_1():
        quantity_1=5
        print(f"Your order is {quantity_1} {food} using {delivery_partner}")
    order_1()
restarunt()

#Type casting

x="10"
y="20"

print(type(x))
print(type(y))

a=int(x)
print("10",type(a))
b=int(y)
print("20",type(b))

c="20.56"

print(float(c))

## String usage cases

"""
coder_name = "jerry"

print(coder_name.lower())
print(coder_name.upper())
print(coder_name.capitalize())
"""


mobile_number = "9952109613"

masked=mobile_number[:2] + "******" + mobile_number[-2:]
print(masked)

song="shape OF yoU"
artist="JERRY aJ"

formated = f"{song.title()}-{artist.title()}"
print(formated)


location = "Tirunelveli"

fixed_location = location.replace("Tirunelveli","Tenkasi")
print(fixed_location)

message = "Your Uber id number is confirmed. This is your id : UBI123456."

booking_id_number = message.split(".")[1].split(":")[1].strip()
print(booking_id_number)

offer_msg = "use Swiggy123 to get 100 off you first order"
if "Swiggy123" in offer_msg:
        print("Offer confirmed")



feed_back = "The driver was polite and drive was smooth"
print("Positioned :",feed_back.find("driver"))

name="Jerry Johnson"
initial = "".join([word[0].upper() for word in name.split()])
print(initial)

clear_input = "    Jerry     "
clean = clear_input.strip()
print(clean)



word = "The trip was amazing and the car was clean"

word_count =len(word.split("The"))
print(word_count)
print(word_count.bit_count())

atm_number = "837747828834"
edit_number = atm_number[:8]+"****"
print(len(edit_number))
print(edit_number)

my_name = "Jerry A"
print(my_name.find("A"))
print(my_name[2])
print(my_name.count("r"))

"""
secrat_number=45



for i in range(0,5):
    user_input = int(input("Enter the number :"))
    if user_input<1 or user_input>100:
        print("Invalid numbers")
    elif user_input>secrat_number:
        print("Your number is Higher")
    elif user_input<secrat_number:
        print("Your number is Lesser")

    else:
        print("Your number is correct")
        break
"""
#if ,elif,else conditions
"""
marks = 34


if marks >=90:
    print("Grade A")
elif marks>=80:
    print("Grade B")
elif marks>=70:
    print("Grade C")
elif marks>=60:
    print("Average")
elif marks>=35:
    print("lower")
else:
    print("fail")
"""
# nested if conditions

age = 24
has_license="No"

if age>=18:
    if has_license == "Yes":
        print("You can Drive")
    else:
        print("Go and take License!")
else:
    print("You are too young to drive!")


# nested if conditions
amount=14000
has_card = "Yes"

if amount>=15000:
    if has_card == "Yes":
        print("You can Purchase")
    else:
        print("You cannot Purchase")
else:
    print("You have not enough amount!")

#Two conditons use one if conditons

marks=70
attendance = 87

if marks>=80 or attendance>=70:
    print("You are eligible to write the exam!")
else:
    print("You are not eligible!")



recharge_data = 1.5
recharge_amount = 200

if recharge_data>=1.5 or recharge_amount>=399:
    print("You are eligible!")
else:
    print("You are not eligible!")


order_amount=1400
days="mon"
member_ship="Gold"

if (order_amount>=1500 and days in ["sat","sun"]) or member_ship=="Gold":
    print("20% discount!")
else:
    print("No discount!")


number = [1,4,-5,-3,-7,0,5,9,14,-12]

for i in number:
    if i>=0:
        print(i)


def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "cannot divide by zero!"
print(divide(40,8))


