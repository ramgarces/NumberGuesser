'''
Ideas:
    -Add menu system (play again?, change range?, etc.)
'''

import random

# Define function to put all game code into
def play_game():
    # Set range for number guesses
    print("Current range: 1 - ___")
    range_max = int(input("Enter range max: ")) 

    # Generate a random number and assign to a variable
    random_number = random.randint(1, range_max)

    # Get user's guess for the first time
    user_guess = int(input(f"Guess a number 1 - {range_max}: "))

    # Keep game going while user's guess is not random number
    while user_guess != random_number:
        if user_guess > random_number:
            print("Too high.")
        if user_guess < random_number:
            print("Too low.")
        print("Guess again.")
        user_guess = int(input(f"Guess a number 1 - {range_max}: "))
    else:
        print("You did it!")
        print("")
        print(f"The number was {random_number}")
        
# Call function to run the game
while True:
    try:
        play_game()
        break
    except:
        print("Something went wrong!")
