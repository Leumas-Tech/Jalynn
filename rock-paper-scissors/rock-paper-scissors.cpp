#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <random>
#include <limits> // Required for numeric_limits

char getComputerChoice() {
    std::vector<char> choices = {'R', 'P', 'S'};
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> distrib(0, choices.size() - 1);
    return choices[distrib(gen)];
}

std::string determineWinner(char userChoice, char computerChoice, int& userScore, int& computerScore) {
    if (userChoice == computerChoice) {
        return "It's a tie!";
    } else if (
        (userChoice == 'R' && computerChoice == 'S') ||
        (userChoice == 'P' && computerChoice == 'R') ||
        (userChoice == 'S' && computerChoice == 'P')
    ) {
        userScore++;
        return "You win this round!";
    } else {
        computerScore++;
        return "Computer wins this round!";
    }
}

int main() {
    int userScore = 0;
    int computerScore = 0;
    int roundsToWin = 0;

    while (true) {
        std::cout << "Enter the number of rounds to win (an odd integer 3 or greater): ";
        std::cin >> roundsToWin;

        if (std::cin.fail() || roundsToWin < 3 || roundsToWin % 2 == 0) {
            std::cout << "Invalid input. Please enter an odd integer 3 or greater." << std::endl;
            std::cin.clear(); // Clear error flags
            // Ignore rest of the invalid input line
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        } else {
            // Ignore the rest of the line after valid integer input
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            break;
        }
    }

    std::cout << "First to win " << roundsToWin << " rounds wins the game!" << std::endl;

    while (userScore < roundsToWin && computerScore < roundsToWin) {
        std::string userInput;
        char userChoice;

        while (true) {
            std::cout << "Enter your choice (R for Rock, P for Paper, S for Scissors): ";
            std::getline(std::cin, userInput);

            if (userInput.length() == 1 && (userInput[0] == 'R' || userInput[0] == 'P' || userInput[0] == 'S')) {
                userChoice = userInput[0];
                break;
            } else {
                std::cout << "Invalid input. Please enter R, P, or S." << std::endl;
            }
        }

        char computerChoice = getComputerChoice();
        std::cout << "You chose: " << userChoice << std::endl;
        std::cout << "Computer chose: " << computerChoice << std::endl;

        std::string result = determineWinner(userChoice, computerChoice, userScore, computerScore);
        std::cout << result << std::endl;
        std::cout << "Score: You " << userScore << " - " << computerScore << " Computer" << std::endl;
    }

    std::cout << "\n--- Game Over ---" << std::endl;
    if (userScore > computerScore) {
        std::cout << "Congratulations! You won the game!" << std::endl;
    } else if (computerScore > userScore) {
        std::cout << "Computer won the game!" << std::endl;
    } else {
        std::cout << "The game is a tie!" << std::endl;
    }
    std::cout << "Final Score: You " << userScore << " - " << computerScore << " Computer" << std::endl;

    return 0;
}
