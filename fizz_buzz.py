"""
100 days of Python course
DAY 5
"""

# a quick exercise in logic, using if / elif / else for
# the solution to the FizzBuzz challenge
# the use of operators is important and the range ensures
# that we get numbers from 1 up to and including 100 only
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
