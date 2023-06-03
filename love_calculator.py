# Get the names of the two individuals and convert them to lowercase
your_name = input("Enter your name: ").lower()
her_name = input("Enter his/her name: ").lower()

# Count the occurrences of specific letters ('t', 'r', 'u', 'e') in both names
number_of_T = your_name.count('t') + her_name.count('t')
number_of_R = your_name.count('r') + her_name.count('r')
number_of_U = your_name.count('u') + her_name.count('u')
number_of_E = your_name.count('e') + her_name.count('e')

# Calculate the total true score by summing the counts of specific letters
total_true_score = number_of_T + number_of_R + number_of_U + number_of_E

# Count the occurrences of other letters ('l', 'o', 'v', 'e') in both names
number_of_L = your_name.count('l') + her_name.count('l')
number_of_O = your_name.count('o') + her_name.count('o')
number_of_V = your_name.count('v') + her_name.count('v')
number_of_E = your_name.count('e') + her_name.count('e')

# Calculate the total love score by summing the counts of other letters
total_love_score = number_of_L + number_of_O + number_of_V + number_of_E

# Concatenate the total true score and total love score into a single string
# Convert the string to an integer and assign it to the variable total_score
total_score = int(str(total_true_score) + str(total_love_score))

# Check the total score and provide different messages based on its range
if total_score < 10 or total_score > 90:
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif 40 <= total_score <= 50:
    # Check if the total score is between 40 and 50 (inclusive)
    print(f'Your score is {total_score}, you are alright together.')
else:
    print(f'Your score is {total_score}')
