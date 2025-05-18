# Ideas: Have user select number range for guessing, make sure number is staying the same for all guesses (not changing everytime a user enters a guess)

import random

# Generate a random number and assign to a variable
random_number = random.randint(1, 10)

# Get user's guess
user_guess = int(input("Guess a number 1 - 10: "))

# Does the user's guess match the random number?
if user_guess == random_number:
    print("You did it!")
else:
    print("Guess again.")

print(f"Random number is: {random_number}")
print(f"User number is: {user_guess}")
