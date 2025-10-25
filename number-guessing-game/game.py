
import random

def guess_the_number():
    """
    This function implements a simple number guessing game.
    """
    number_to_guess = random.randint(1, 100)
    guess = None

    print("I'm thinking of a number between 1 and 100.")

    while guess != number_to_guess:
        try:
            guess = int(input("What's your guess? "))

            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
        except ValueError:
            print("Please enter a valid number.")

    print(f"You got it! The number was {number_to_guess}.")

if __name__ == "__main__":
    guess_the_number()
