# from datetime import date
# from datetime import datetime

# # Day Stuff
# today = date.today()
# print("Current Date:", today)

# # Time Stuff
# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")
# print("Current Time:", current_time, "\n")

# # Etc
# print("------------------------------\n")

# print("G-day m8.")

# name = input("What's ur name? \n> ")

# print("Hi " + name + "!")

# color = input("What's ur favorite color? \n> ")
# print("Your favorite is " + color + "? That's also my favorite color! :D")

# function header format:
# def function_name():
def greeting():
  # the body of the function is indented
  name = input("What's ur name? \n> ")
  print("Hi " + name + "!")


# to run the function, you have to call it outside
# the function
greeting()