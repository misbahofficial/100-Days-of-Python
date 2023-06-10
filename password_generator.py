import random

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']  # List of uppercase letters
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # List of numbers
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', "'", '"', '<',
           '>', ',', '.', '/', '?']  # List of symbols

number_of_letters = int(input("How many letters do you want? "))  # User input for the number of letters
number_of_numbers = int(input("How many numbers do you want? "))  # User input for the number of numbers
numbers_of_symbols = int(input("How many symbols do you want? "))  # User input for the number of symbols

generated_password = ""  # Initialize an empty string to store the generated password

# Generate the letters for the password
for i in range(number_of_letters):
    random.shuffle(letters)  # Shuffle the list of letters
    generated_password += str(letters[i])  # Append a letter from the shuffled list to the generated password

# Generate the numbers for the password
for j in range(number_of_numbers):
    random.shuffle(numbers)  # Shuffle the list of numbers
    generated_password += str(numbers[j])  # Append a number from the shuffled list to the generated password

# Generate the symbols for the password
for k in range(numbers_of_symbols):
    random.shuffle(symbols)  # Shuffle the list of symbols
    generated_password += str(symbols[k])  # Append a symbol from the shuffled list to the generated password

converted_pass = list(generated_password)  # Convert the generated password string into a list
random.shuffle(converted_pass)  # Shuffle the list of characters in the password
final_password = ''.join(converted_pass)  # Join the shuffled characters to form the final password string

print(final_password)  # Print the final password
