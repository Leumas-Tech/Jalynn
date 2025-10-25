
#include <iostream>
#include <random>
#include <string>

void guessTheNumber() {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> distrib(1, 100);
    int numberToGuess = distrib(gen);
    int guess = 0;

    std::cout << "I'm thinking of a number between 1 and 100." << std::endl;

    do {
        std::cout << "What's your guess? ";
        std::string input;
        std::cin >> input;

        try {
            guess = std::stoi(input);

            if (guess < numberToGuess) {
                std::cout << "Too low!" << std::endl;
            } else if (guess > numberToGuess) {
                std::cout << "Too high!" << std::endl;
            }
        } catch (const std::invalid_argument& ia) {
            std::cout << "Please enter a valid number." << std::endl;
        }

    } while (guess != numberToGuess);

    std::cout << "You got it! The number was " << numberToGuess << "." << std::endl;
}

int main() {
    guessTheNumber();
    return 0;
}
