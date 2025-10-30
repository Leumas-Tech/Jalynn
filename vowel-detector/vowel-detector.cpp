#include <iostream>
#include <string>
#include <map>

int main() {
    std::string inputString;
    std::cout << "Enter a string: ";
    std::getline(std::cin, inputString);

    std::string vowels = "aeiouAEIOU";
    int totalVowels = 0;
    std::map<char, int> vowelCounts;

    for (char c : inputString) {
        if (vowels.find(c) != std::string::npos) {
            totalVowels++;
            vowelCounts[c]++;
        }
    }

    std::cout << "Original string: " << inputString << std::endl;
    std::cout << "Total number of vowels: " << totalVowels << std::endl;
    std::cout << "Vowel counts (case-sensitive):" << std::endl;
    for (auto const& [vowel, count] : vowelCounts) {
        std::cout << "  " << vowel << ": " << count << std::endl;
    }

    return 0;
}