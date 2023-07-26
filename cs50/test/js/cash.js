// Airbnb JavaScript style guide: https://github.com/airbnb/javascript/

/**
 * Prints the minimum US coins (up to quarters) needed to make a given
 * amount of change owed in cents.
 */


// Import the readline-sync module to interact with user via console.
const readlineSync = require('readline-sync');

// Main function.
const main = function mainFunction () {
  console.log();

  // Get change owed.
  let userChange = getChange('Enter change (in dollars): ');

  // Count coins necessary for user's change.
  let coins = countCoins(userChange);

  // Print number of coins (as an integer and a newline).
  console.log(coins);

  console.log();
}

// Return user-input positive int amount of change in dollars.
const getChange = function getChangeFunction (prompt) {
  let change;

  // Continually reprompt if change input is not valid.
  while (true) {
    // Get user input.
    change = readlineSync.question(prompt);

    // Check if input is empty.
    if (change === "") {
      console.log('error: no change entered\n');
      continue;
    }

    // Convert change to a number.
    change = Number(change)

    // Check if input is in dollars.2d format.
    if (!Number.isInteger(change * 100)) {
      console.log('error: invalid dollars and cents\n');
      continue;

    // Check if input is negative.
    } else if (change < 0) {
      console.log('change must be positive');
      continue;
    }

    return change;
  }
}

// Count the minimum number of coins equal to argument amount.
const countCoins = function countCoinsFunction (dollars) {
  // List of coin values from quarters down.
  const coinValues = [25, 10, 5, 1];

  // Convert float into integer coin value for calculations.
  let cents = parseInt(dollars * 100);

  // Initialize counter variable.
  let count = 0;

  // Iterate through list of coins.
  coinValues.forEach(function(coin) {
    while (true) {
      // Switch to smaller coin if necessary.
      if (cents < coin) {
          break;
      }

      // Subtract value of each coin; count the coin.
      cents -= coin;
      count += 1;
    }
  })

  // Return count when done subtracting coins.
  return count;
}

main();
