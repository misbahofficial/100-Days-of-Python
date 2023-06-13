# Import the random module
import random

# Define a list of stages, which will be used to display the hangman as the player loses lives
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''']

# Define a list of words to choose from
words = ['apple', 'litchi', 'banana', 'orange', 'juice']

# Choose a random word from the list of words
chosen_word = random.choice(words)

# Create a blank list to store the guessed letters
blank_list = []

# Create a string to display the blank list
display = ""

# Loop through the chosen word and add a '_' to the blank list for each letter
for i in range(len(chosen_word)):
    blank_list.append('_')

# Join the blank list with spaces to create a string
display = " ".join(blank_list)

# Set the end of game flag to False
end_of_game = False

# Set the number of lives to 6
lives = 6

# While the game is not over, do the following:
while not end_of_game:

    # Get the user's guess
    user_guess = input("Guess a letter: ")

    # Loop through the blank list and check if the user's guess is in the chosen word
    for j in range(len(blank_list)):
        if chosen_word[j] == user_guess:

            # If the user's guess is in the chosen word, replace the '_' in the blank list with the user's guess
            blank_list[j] = user_guess

            # Join the blank list with spaces to create a new string
            display = " ".join(blank_list)

    # If the user's guess is in the chosen word, print the following:
    if user_guess in chosen_word:
        print("You guessed a right word.")
        print(display)

    # Otherwise, do the following:
    else:

        # Decrement the number of lives
        lives -= 1

        # Print the corresponding stage of the hangman
        print(stages[lives])

        # If the number of lives is 0, print the following:
        if lives == 0:
            print("You lose.")
            print("Game over. You ran out of lives.")
            break

        # Otherwise, print the following:
        else:
            print(display)
            print('Your guess is wrong. So, you loose a life.')

    # If there are no more '_' in the blank list, print the following and set the end of game flag to True:
    if '_' not in blank_list:
        print("Congratulations! You win.")
        end_of_game = True

