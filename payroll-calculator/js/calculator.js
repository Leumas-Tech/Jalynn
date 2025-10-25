const readline = require('readline');
const fs = require('fs');
const path = require('path');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function calculatePayroll() {
  const defaultConfig = {
    fedTaxRate: 0.15,
    stateTaxRate: 0.05,
    SSTaxRate: 0.062
  };

  const configPath = path.join(__dirname, '..', 'config.json');
  let taxRates = defaultConfig;

  try {
    const configData = fs.readFileSync(configPath, 'utf8');
    taxRates = JSON.parse(configData);
  } catch (error) {
    console.log("config.json not found, using default tax rates.");
  }

  rl.question("Enter hours worked: ", (hoursWorked) => {
    rl.question("Enter hourly rate: ", (hourlyRate) => {
      const parsedHours = parseFloat(hoursWorked);
      const parsedRate = parseFloat(hourlyRate);

      if (isNaN(parsedHours) || isNaN(parsedRate)) {
        console.log("\nPlease enter valid numbers for hours worked and hourly rate.");
        rl.close();
        return;
      }

      const grossPay = parsedHours * parsedRate;
      const fedAmount = grossPay * taxRates.fedTaxRate;
      const stateAmount = grossPay * taxRates.stateTaxRate;
      const ssAmount = grossPay * taxRates.SSTaxRate;
      const netPay = grossPay - fedAmount - stateAmount - ssAmount;

      console.log(`\nGross Pay: $${grossPay.toFixed(2)}`);
      console.log(`Federal Tax: $${fedAmount.toFixed(2)}`);
      console.log(`State Tax: $${stateAmount.toFixed(2)}`);
      console.log(`Social Security: $${ssAmount.toFixed(2)}`);
      console.log(`Net Pay: $${netPay.toFixed(2)}`);

      rl.close();
    });
  });
}

calculatePayroll();