// Airbnb JavaScript style guide: https://github.com/airbnb/javascript/

/**
 * Prompts user for an int height and creates a Mario-style pyramid with
 * # characters.
 */

// Import the readline-sync module to interact with user via console.
const readlineSync = require('readline-sync');

// Main function.
const main = function mainFunction () {
  // Get height of half-pyramid.
  let userHeight = getHeight('Height: ');

  // Print pyramid.
  console.log();
  printPyramid(userHeight);
}

// Return user-input positive integer pyramid height.
const getHeight = function getHeightFunction (prompt) {
  let height;

  // Continually reprompt if height is not an integer between 1 and 8.
  while (true) {
    height = Number(readlineSync.question(prompt));
    if (!Number.isInteger(height)) {
      console.log('error: height must be an integer.\n');
      continue;
    } else if (height < 1 || height > 8) {
      console.log('error: height must be between 1 and 8, inclusive.\n');
      continue;
    }

    return height;
  }

}

// Print pyramid with height input.
const printPyramid = function printPyramidFunction (height) {
  // Print input number of rows, starting with row 1 to simplify calc.
  for (let row = 1; row < height + 1; row++) {
    // Initialize printer string.
    let printer = '';

    // Add decreasing spaces.
    printer += ' '.repeat(height - row);

    // Then add increasing # starting with 1.
    printer += '#'.repeat(row);

    // Then add a double space.
    printer += '  ';

    // Then add the same amount of # as before.
    printer += '#'.repeat(row);

    // Print row.
    console.log(printer);
  }
}

main();
