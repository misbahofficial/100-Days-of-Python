# Display a welcome message to the user
print("Welcome to GPA calculator.")

# Prompt the user to enter their letter grades
print('Please enter all your letter grades, one per line: ')

# Provide instructions to the user on how to end the input
print("Enter a blank line to designate the end.")

# Define a dictionary that maps letter grades to their corresponding point values
points = {
    'A+': 4.00,
    'A': 3.75,
    'A-': 3.50,
    'B+': 3.25,
    'B': 3.00,
    'B-': 2.75,
    'C+': 2.50,
    'C': 2.25,
    'D': 2.00,
    'F': 0.00
}

# Initialize variables to keep track of the number of courses and total grade points
number_of_courses = 0
total_points = 0

# Initialize a flag to indicate when the user is done entering grades
done = False

# Start a loop that continues until the user is done entering grades
while not done:
    # Prompt the user to enter a grade
    grade = input()

    # Check if the user entered a blank line to end the input
    if grade == '':
        done = True
    # Check if the entered grade is not in the 'points' dictionary
    elif grade not in points:
        # Display a message indicating that the grade is unknown and ignore it
        print("Unknown grade '{0}' being ignored".format(grade))
    else:
        # Increment the number of courses
        number_of_courses += 1

        # Add the grade points of the entered grade to the total points
        total_points += points[grade]

# Check if the user entered at least one grade
if number_of_courses > 0:
    # Calculate the GPA by dividing the total points by the number of courses, and format it to 3 decimal places
    gpa = total_points / number_of_courses
    formatted_gpa = '{0:.3}'.format(gpa)

    # Print the calculated GPA to the user
    print('Your GPA is', formatted_gpa)
