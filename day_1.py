# Day 1 - Python Print Function
# The function is declared like this:
# print('what to print')

# task-1
print("""Day 1 - Python Print Function
The function is declared like this:
print('what to print')""")

# task-2
# Fix the code below
print("Day 1 - String Manipulation")
print("String Concatenation is done with the \"+\" sign.")
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

# task-3
# input function
userName = input("What is your name? ")
print(len(userName))

# task-4
# variables

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
# Write your code below this line 👇
c = a
a = b
b = c

# Write your code above this line 👆
####################################

# Don't change the code below 👇
print("a: " + a)
print("b: " + b)

# day-1 project band name generator
print("Welcome to the Band Name generator.")
city_name = input("What's name of the city you grew up in?\n")
print(city_name)
pet_name = input("What's your pet name?\n")
print(pet_name)
print("Your band could be " + city_name + " " + pet_name)
