# Ideas: Have user select number range for guessing, make sure number is staying the same for all guesses (not changing everytime a user enters a guess)

import random

# Generate a random number and assign to a variable
random_number = random.randint(1, 10)

# Get user's guess for the first time
user_guess = int(input("Guess a number 1 - 10: "))

# Keep game going while user's guess is not random number
while user_guess != random_number:
    print("Guess again.")
    print(f"(TESTING) Random number: {random_number}")
    user_guess = int(input("Guess a number 1 - 10: "))
else:
    print("You did it!")
    print("")
    print(f"The number was {random_number}")
