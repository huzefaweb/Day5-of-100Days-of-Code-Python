"""
100 days of Python course
DAY 5
"""

# calculate the sum of all the even numbers from 1 to 100,
# including 2 and 100: using the for ... in range loop
# approach using range 2, 101 and stepping by 2
even_sum = 0
for number in range(2, 101, 2):
    even_sum += number
print(even_sum)

# a different approach by defining the range 1, 101
alternative_sum = 0
for number in range(1, 101):
    if number % 2 == 0:
        alternative_sum += number
print(alternative_sum)

# note: even_sum and alternative_sum are constant variables
# once this subject is covered in future class it will make sense!
