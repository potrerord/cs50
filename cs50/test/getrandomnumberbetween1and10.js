// JavaScript style guide: https://github.com/airbnb/javascript

function getrandomnumberbetween1and10() {
    // Generate random float where 0 <= rand_float < 1.
    let rand_float = Math.random();

    // Scale rand_float to 0 <= rand_float < 10, floor it, then add 1.
    let number = Math.floor(rand_float * 10) + 1;

    return number;
}
