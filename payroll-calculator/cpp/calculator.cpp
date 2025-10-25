#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <vector>

// A simple function to trim whitespace from the start and end of a string
std::string trim(const std::string& str) {
    size_t first = str.find_first_not_of(" \t\n\r");
    if (std::string::npos == first) {
        return str;
    }
    size_t last = str.find_last_not_of(" \t\n\r");
    return str.substr(first, (last - first + 1));
}

void calculatePayroll() {
    double fedTaxRate = 0.15;
    double stateTaxRate = 0.05;
    double ssTaxRate = 0.062;

    std::ifstream configFile("../config.json");
    if (configFile.is_open()) {
        std::string line;
        while (std::getline(configFile, line)) {
            size_t colonPos = line.find(':');
            if (colonPos != std::string::npos) {
                std::string key = trim(line.substr(0, colonPos));
                std::string valueStr = trim(line.substr(colonPos + 1));
                // Remove quotes from key
                key.erase(std::remove(key.begin(), key.end(), '"'), key.end());
                // Remove comma from value if it exists
                valueStr.erase(std::remove(valueStr.begin(), valueStr.end(), ','), valueStr.end());

                try {
                    double value = std::stod(valueStr);
                    if (key == "fedTaxRate") fedTaxRate = value;
                    else if (key == "stateTaxRate") stateTaxRate = value;
                    else if (key == "SSTaxRate") ssTaxRate = value;
                } catch (const std::invalid_argument& ia) {
                    // Ignore lines that don't have a valid number
                }
            }
        }
        configFile.close();
    } else {
        std::cout << "config.json not found, using default tax rates." << std::endl;
    }

    double hoursWorked, hourlyRate;

    std::cout << "Enter hours worked: ";
    std::string inputHours;
    std::cin >> inputHours;

    std::cout << "Enter hourly rate: ";
    std::string inputRate;
    std::cin >> inputRate;

    try {
        hoursWorked = std::stod(inputHours);
        hourlyRate = std::stod(inputRate);

        double grossPay = hoursWorked * hourlyRate;
        double fedAmount = grossPay * fedTaxRate;
        double stateAmount = grossPay * stateTaxRate;
        double ssAmount = grossPay * ssTaxRate;
        double netPay = grossPay - fedAmount - stateAmount - ssAmount;

        std::cout << std::fixed << std::setprecision(2);
        std::cout << "\nGross Pay: $" << grossPay << std::endl;
        std::cout << "Federal Tax: $" << fedAmount << std::endl;
        std::cout << "State Tax: $" << stateAmount << std::endl;
        std::cout << "Social Security: $" << ssAmount << std::endl;
        std::cout << "Net Pay: $" << netPay << std::endl;

    } catch (const std::invalid_argument& ia) {
        std::cout << "\nPlease enter valid numbers for hours worked and hourly rate." << std::endl;
    }
}

int main() {
    calculatePayroll();
    return 0;
}