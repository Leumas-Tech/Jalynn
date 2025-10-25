# Gemini CLI Projects

This repository contains a few simple projects created with the help of the Gemini CLI. Each project is implemented in three different programming languages: Python, JavaScript, and C++.

## 1. Hello World

This is the simplest program you can write! It just prints "Hello World" to your screen.

### Languages

*   **Python:**
    *   **File:** `hello-world-scripts/python/hello-world.py`
    *   **How to run:**
        ```bash
        python hello-world-scripts/python/hello-world.py
        ```

*   **JavaScript (Node.js):**
    *   **File:** `hello-world-scripts/js/hello-world.js`
    *   **How to run:**
        ```bash
        node hello-world-scripts/js/hello-world.js
        ```

*   **C++:**
    *   **File:** `hello-world-scripts/cpp/hello-world.cpp`
    *   **How to run:**
        First, you need to compile the C++ code. This will create an executable file.
        ```bash
        g++ hello-world-scripts/cpp/hello-world.cpp -o hello-world
        ```
        Then, you can run the executable:
        ```bash
        ./hello-world
        ```
        (On Windows, you might run `hello-world.exe`)

## 2. Number Guessing Game

This is a fun little game where the computer thinks of a number between 1 and 100, and you have to guess it!

### Languages

*   **Python:**
    *   **File:** `number-guessing-game/game.py`
    *   **How to run:**
        ```bash
        python number-guessing-game/game.py
        ```

*   **JavaScript (Node.js):**
    *   **File:** `number-guessing-game/game.js`
    *   **How to run:**
        ```bash
        node number-guessing-game/game.js
        ```

*   **C++:**
    *   **File:** `number-guessing-game/game.cpp`
    *   **How to run:**
        First, compile the code:
        ```bash
        g++ number-guessing-game/game.cpp -o number-guesser
        ```
        Then, run the game:
        ```bash
        ./number-guesser
        ```
        (On Windows, you might run `number-guesser.exe`)

## 3. Payroll Calculator

This is a simple tool to calculate your paycheck. It calculates your gross pay, taxes, and net pay.

You can change the tax rates by editing the `payroll-calculator/config.json` file.

### Languages

*   **Python:**
    *   **File:** `payroll-calculator/python/calculator.py`
    *   **How to run:**
        ```bash
        python payroll-calculator/python/calculator.py
        ```

*   **JavaScript (Node.js):**
    *   **File:** `payroll-calculator/js/calculator.js`
    *   **How to run:**
        ```bash
        node payroll-calculator/js/calculator.js
        ```

*   **C++:**
    *   **File:** `payroll-calculator/cpp/calculator.cpp`
    *   **How to run:**
        First, compile the code:
        ```bash
        g++ payroll-calculator/cpp/calculator.cpp -o payroll-calculator
        ```
        Then, run the calculator:
        ```bash
        ./payroll-calculator
        ```
        (On Windows, you might run `payroll-calculator.exe`)
