# Number Guessing Game Objectives:
# Include an ASCII art logo.
import art
import random

# Display the game logo.
print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Ask the user to choose the game difficulty.
player_mode_select = str(input("Choose a difficulty. Type 'easy' or 'hard': ")).lower()

# Mode selected
attempts_left = 0

# Set the number of attempts based on the selected difficulty.
if player_mode_select == "easy":
    attempts_left = 10
elif player_mode_select == "hard":
    attempts_left = 5
else:
    print("Unexpected error")
    exit()

# Generate a random number for the user to guess.
computer_guess = random.randint(1, 101)
is_game_over = False

# Main game loop
while not is_game_over:
    player_guess = int(input("Make a guess: "))

    # Display the number of attempts remaining.
    print(f"You have {attempts_left} attempts remaining to guess the number.")

    if attempts_left == 0:
        # End the game if no attempts left.
        is_game_over = True
        print("Game Over.")
        exit()
    elif player_guess == computer_guess:
        # End the game if the user guessed correctly.
        is_game_over = True
        print("You win!")
    elif player_guess > computer_guess:
        # Provide feedback for a too high guess.
        attempts_left -= 1
        print("Too high.\nGuess again.")
    elif player_guess < computer_guess:
        # Provide feedback for a too low guess.
        attempts_left -= 1
        print("Too low.\nGuess again.")
