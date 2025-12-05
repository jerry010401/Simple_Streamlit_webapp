# EXCEPTION HANDLING TOPICS LIKE,
# TRY,EXCEPT AND FINALLY......

print("Welcome to Zomato!")
try:
    item_input = int(input("How many items:"))

    total_amount = 200 * item_input
    average_item_price = 200 / item_input

    print("total price : ", average_item_price)
except ZeroDivisionError:
    print("you Cannot order 0 items!")
except ValueError:
    print("Invalid Characters")

print("Thankyou for your purchase!")

# if-else checks only knows problems.

number = int(input("Enter :"))

if number==0:
    print("You cannot divide by zero")
else:
    print(200/number)
