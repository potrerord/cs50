// Airbnb JavaScript style guide: https://github.com/airbnb/javascript/

// Says hello.

// Main function.
const main = function mainFunction () {
  // Initialize instance of readline interface.
  const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  // Ask user for name and print response.
  readline.question(`What is your name? `, name => {
    console.log(`hello, ${name}`);
    readline.close();
  });
}

main()
