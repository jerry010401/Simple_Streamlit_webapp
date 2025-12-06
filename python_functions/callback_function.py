#CALLBACK FUNCTIONS
# A callback function is a function that you pass as an argument to another function.
# Example-1
def on_button_click(callback):
    print("Button clicked!")
    callback()
def show_message():
    print("Hii Jerry.. Welcome to the page!")
on_button_click(show_message)

#Example-2

def greet(name):
    print(f"Hii! how are you? {name}")
def get_user(callback):
    user="jerry"
    callback(user)
get_user(greet)


