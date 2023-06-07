import random  # Import the random module for generating random numbers

choices = ["Rock", "Paper", "Scissors"]  # List of available choices in the game

def get_user_choice():
    while True:
        try:
            choice = int(input("Enter your choice (0 for Rock, 1 for Paper, 2 for Scissors): "))  # Prompt the user to enter their choice
            if choice in [0, 1, 2]:  # Check if the choice is valid
                return choice  # Return the valid choice
            else:
                print("Invalid input. Please enter a number between 0 and 2.")  # Display an error message for invalid input
        except ValueError:
            print("Invalid input. Please enter a number.")  # Display an error message for non-numeric input

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a draw!"  # If the user and computer choices are the same, it's a draw
    elif (
            (user_choice == 0 and computer_choice == 2)  # Check the winning conditions for the user
            or (user_choice == 1 and computer_choice == 0)
            or (user_choice == 2 and computer_choice == 1)
    ):
        return "You win!"  # If the user wins, return the corresponding message
    else:
        return "Computer wins!"  # If the computer wins, return the corresponding message

def play_game():
    print("Welcome to Rock, Paper, Scissors!")  # Display a welcome message
    while True:
        user_choice = get_user_choice()  # Get the user's choice
        computer_choice = random.randint(0, 2)  # Generate a random choice for the computer

        print(f"You chose: {choices[user_choice]}")  # Display the user's choice
        print(f"Computer chose: {choices[computer_choice]}")  # Display the computer's choice

        winner = determine_winner(user_choice, computer_choice)  # Determine the winner
        print(winner)  # Display the result

        play_again = input("Do you want to play again? (y/n): ")  # Ask the user if they want to play again
        if play_again.lower() != "y":
            break  # Exit the loop if the user doesn't want to play again

    print("Thanks for playing!")  # Display a goodbye message

play_game()  # Start the game
