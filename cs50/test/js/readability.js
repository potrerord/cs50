// Airbnb JavaScript style guide: https://github.com/airbnb/javascript/

// Prints the Coleman-Liau index reading grade level for input text.

// Import the readline-sync module to interact with user via console.
const readlineSync = require('readline-sync');

// Main function.
const main = function mainFunction () {
  // Prompt user for text to analyze
  let userString = readlineSync.question("Enter text: ");

  // Initiate counter variables.
  let userLetters = 0;
  let userSentences = 0;

  // Special case: Words will be one more than the amount of spaces.
  let userWords = 1;

  // Scan each character in string to count letters/words/sentences.
  userString.split('').forEach(function(char) {
    if (['.', '!', '?'].includes(char)) {
      // Check if character ends a sentence.
      userSentences += 1
    } else if (char.trim() === '') {
      // Check if character is whitespace.
      userWords += 1
    } else if (/^[A-Za-z]$/.test(char)) {
      // Check if character is alpha.
      userLetters += 1;
    }
  });

  // Store rounded Coleman-Liau index
  let level = Math.round(coleLiau(userLetters, userWords, userSentences))

  // Print Grade X
  if level < 1:
    print("Before Grade 1.")
  elif level > 15:
    print("Grade 16+")
  else:
    for grade in range(1, 16):
      if grade == level:
        print(f"Grade {level}")
}

// Return the Coleman-Liau index given the arguments.
const coleLiau = function coleLiauFunction (letters, words, sentences) {

  let score = (
    (0.0588 * (100 * (letters / words)) - (0.296 * (100 * sentences / words))) - 15.8
  );

  return score;
}

main()
