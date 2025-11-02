import random

def get_computer_choice():
    """Gets a random choice (R, P, or S) for the computer."""
    return random.choice(['R', 'P', 'S'])

def determine_winner(user_choice, computer_choice):
    """Determines the winner of a round."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'R' and computer_choice == 'S') or \
         (user_choice == 'P' and computer_choice == 'R') or \
         (user_choice == 'S' and computer_choice == 'P'):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    """Main function to run the game."""
    user_score = 0
    computer_score = 0

    while True:
        try:
            best_of = int(input("Best of how many rounds? "))
            if best_of <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    for round_num in range(1, best_of + 1):
        print(f"\n--- Round {round_num} ---")
        user_choice = input("Enter your choice (R, P, or S): ").upper()

        while user_choice not in ['R', 'P', 'S']:
            print("Invalid choice. Please enter R, P, or S.")
            user_choice = input("Enter your choice (R, P, or S): ").upper()

        computer_choice = get_computer_choice()

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)
        print(winner)

        if winner == "You win!":
            user_score += 1
        elif winner == "Computer wins!":
            computer_score += 1

        print(f"Score: You {user_score} - {computer_score} Computer")

    print("\n--- Game Over ---")
    if user_score > computer_score:
        print("You won the game!")
    elif computer_score > user_score:
        print("Computer won the game!")
    else:
        print("The game is a tie!")

    print(f"Final Score: You {user_score} - {computer_score} Computer")

if __name__ == "__main__":
    main()