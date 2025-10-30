import random

def get_computer_choice():
    return random.choice(['R', 'P', 'S'])

def determine_winner(user_choice, computer_choice):
    global user_score, computer_score
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'R' and computer_choice == 'S') or \
         (user_choice == 'P' and computer_choice == 'R') or \
         (user_choice == 'S' and computer_choice == 'P'):
        user_score += 1
        return "You win this round!"
    else:
        computer_score += 1
        return "Computer wins this round!"

user_score = 0
computer_score = 0
rounds_to_win = 0

while True:
    try:
        rounds_input = input("Enter the number of rounds to win (an odd integer 3 or greater): ")
        rounds_to_win = int(rounds_input)
        if rounds_to_win >= 3 and rounds_to_win % 2 != 0:
            break
        else:
            print("Invalid input. Please enter an odd integer 3 or greater.")
    except ValueError:
        print("Invalid input. Please enter a number.")

print(f"First to win {rounds_to_win} rounds wins the game!")

while user_score < rounds_to_win and computer_score < rounds_to_win:
    user_choice = input("Enter your choice (R for Rock, P for Paper, S for Scissors): ").upper()

    if user_choice not in ['R', 'P', 'S']:
        print("Invalid input. Please enter R, P, or S.")
        continue

    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)
    print(f"Score: You {user_score} - {computer_score} Computer")

print("\n--- Game Over ---")
if user_score > computer_score:
    print("Congratulations! You won the game!")
elif computer_score > user_score:
    print("Computer won the game!")
else:
    print("The game is a tie!")
print(f"Final Score: You {user_score} - {computer_score} Computer")
