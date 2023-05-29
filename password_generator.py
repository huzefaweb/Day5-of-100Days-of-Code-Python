"""
100 days of Python course
DAY 5
"""

# Password Generator Project using the random module
import random

# lists are supplied and meaningfully named - contents as shown
# of most commonly used symbols and letters in upper- and lowercase
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# user can choose the number for each category but cannot skip a category
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Easy Level code below where the password is according to choice of
# category and in that order i.e. not scrambled
# remove comments below to run or paste into a new python file:

# password = ""

# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password += random.choice(numbers)

# print(password)

# Hard Level where the random.shuffle is used to produce
# a harder password for the user

# start with creating a list to work with the input
password_list = []

# 3 for loops address each category in turn: note how
# the in range defines what will be appended
for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

# view the password list which is still in order
print(password_list)

# now shuffle it and view again
random.shuffle(password_list)
print(password_list)

# for loop to produce the password and display it
# note: pylint recommends refactor---
# "consider using string.join(sequence) for concatenating
#     strings from an iterable"
# also recommended to make password a constant variable
# which is not in the scope of this lesson

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")
