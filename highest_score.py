"""
100 days of Python course
DAY 5
"""

# use the input for as many scores as user wants and split on the space
student_scores = input("Input a list of student scores separated by spaces").split()

# in range loop to count the scores submitted
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

# set the highest score to zero and use it as a counter
# the for loop compares score to hightest score and it it is
# a bigger number then stores that number as the heighest score
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f"The highest score in the class is: {highest_score}")

# notes: running pylint, advised to use enum function in line 10
# and to make highest_score a constant / global variable in UPPERCASE
