
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function guessTheNumber() {
  const numberToGuess = Math.floor(Math.random() * 100) + 1;
  console.log("I'm thinking of a number between 1 and 100.");

  const askGuess = () => {
    rl.question("What's your guess? ", (guess) => {
      const parsedGuess = parseInt(guess, 10);

      if (isNaN(parsedGuess)) {
        console.log('Please enter a valid number.');
        askGuess();
      } else if (parsedGuess < numberToGuess) {
        console.log('Too low!');
        askGuess();
      } else if (parsedGuess > numberToGuess) {
        console.log('Too high!');
        askGuess();
      } else {
        console.log(`You got it! The number was ${numberToGuess}.`);
        rl.close();
      }
    });
  };

  askGuess();
}

guessTheNumber();
