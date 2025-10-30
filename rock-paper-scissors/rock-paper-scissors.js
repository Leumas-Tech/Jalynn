const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});

const choices = ['R', 'P', 'S'];
let userScore = 0;
let computerScore = 0;
let roundsToWin = 0;

function getComputerChoice() {
  const randomIndex = Math.floor(Math.random() * choices.length);
  return choices[randomIndex];
}

function determineWinner(userChoice, computerChoice) {
  if (userChoice === computerChoice) {
    return 'It\'s a tie!';
  } else if (
    (userChoice === 'R' && computerChoice === 'S') ||
    (userChoice === 'P' && computerChoice === 'R') ||
    (userChoice === 'S' && computerChoice === 'P')
  ) {
    userScore++;
    return 'You win this round!';
  } else {
    computerScore++;
    return 'Computer wins this round!';
  }
}

function playGame() {
  if (userScore === roundsToWin || computerScore === roundsToWin) {
    console.log('\n--- Game Over ---');
    if (userScore > computerScore) {
      console.log('Congratulations! You won the game!');
    } else if (computerScore > userScore) {
      console.log('Computer won the game!');
    } else {
      console.log('The game is a tie!');
    }
    console.log(`Final Score: You ${userScore} - ${computerScore} Computer`);
    readline.close();
    return;
  }

  readline.question('Enter your choice (R for Rock, P for Paper, S for Scissors): ', (userChoice) => {
    userChoice = userChoice.toUpperCase();

    if (!choices.includes(userChoice)) {
      console.log('Invalid input. Please enter R, P, or S.');
      playGame();
      return;
    }

    const computerChoice = getComputerChoice();
    console.log(`You chose: ${userChoice}`);
    console.log(`Computer chose: ${computerChoice}`);

    const result = determineWinner(userChoice, computerChoice);
    console.log(result);
    console.log(`Score: You ${userScore} - ${computerScore} Computer`);

    playGame();
  });
}

function setupGame() {
  readline.question('Enter the number of rounds to win (an odd integer 3 or greater): ', (rounds) => {
    const numRounds = parseInt(rounds);

    if (isNaN(numRounds) || numRounds < 3 || numRounds % 2 === 0) {
      console.log('Invalid input. Please enter an odd integer 3 or greater.');
      setupGame();
    } else {
      roundsToWin = numRounds;
      console.log(`First to win ${roundsToWin} rounds wins the game!`);
      playGame();
    }
  });
}

setupGame();
