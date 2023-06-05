# This program is to calculate GPA for Philosophy, Bangla, Sociology etc. department

course_01 = float(input("Course 01 point: "))
course_02 = float(input("Course 02 point: "))
course_03 = float(input("Course 03 point: "))
course_04 = float(input("Course 04 point: "))
course_05 = float(input("Course 05 point: "))
course_06 = float(input("Course 06 point: "))

total_point = (4 * course_01) + (4 * course_02) + (4 * course_03) + (4 * course_04) + (4 * course_05) + (4 * course_06)
total_credit = 24

gpa = round((total_point / total_credit), 2)

print(f'Your GPA is {gpa}')

