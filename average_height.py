"""
100 days of Python course
DAY 5
"""

# code provided, incorporating .split function
# the in range and converting to integer also provided
# pylint advised to use enumerate (which will be learned in future lesson)
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# set the total height to zero: it is a counter that will be added to
# in the for loop using the height input
total_height = 0
for height in student_heights:
    total_height += height
print(f"total height = {total_height}")

# set the number of students to zero: also a counter that
# gets incremented in the for loop
number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(f"number of students = {number_of_students}")

# final calculation and output
average_height = round(total_height / number_of_students)
print(average_height)

# footnotes: constant variables were identified and should be in
# uppercase - not addressed at this learning level
# total_height and number_of_students need to be in CAPS
