// Airbnb JavaScript style guide: https://github.com/airbnb/javascript/

// Says hello.

// Main function.
const main = function mainFunction () {
  // Request string input from user.
  const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  readline.question(`What is your name? `, name => {
    console.log(`hello, ${name}`);
    readline.close();
  });
}

main()
