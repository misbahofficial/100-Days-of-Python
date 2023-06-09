# This program is to calculate GPA for only math department 3rd year

course_01 = float(input("Course 01 point: "))
course_02 = float(input("Course 02 point: "))
course_03 = float(input("Course 03 point: "))
course_04 = float(input("Course 04 point: "))
course_05 = float(input("Course 05 point: "))
course_06 = float(input("Course 06 point: "))
course_07 = float(input("Course 07 point: "))
course_08 = float(input("Course 08 point: "))

total_point = (4 * course_01) + (4 * course_02) + (4 * course_03) + (4 * course_04) + (4 * course_05) + (4 * course_06) + (4 * course_07) + (4 * course_08)
total_credit = 32

gpa = round((total_point / total_credit), 2)

print(f'Your GPA is {gpa}')

