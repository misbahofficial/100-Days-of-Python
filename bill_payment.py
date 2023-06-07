import random

names = []

# Get the names from the user
Inputted_names = input("Enter names separated by comma: ")

# Split the inputted names into a list
inputted_names_new = Inputted_names.split(', ')

# Iterate over the inputted names and add them to the 'names' list
for i in range(len(inputted_names_new)):
    names.append(inputted_names_new[i])

# Randomly select a person from the 'names' list to pay the bill
person_to_pay = names[random.randint(0, len(names)-1)]

# Print the result with a friendly message
print(f'{person_to_pay} is going to pay the bill!')

