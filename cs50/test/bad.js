// JavaScript style guide: https://github.com/airbnb/javascript

function getrandomnumberbetween1and10() {
    let number = Math.random();
    if (number <= 0.1) {
        return 1;
    }
    if (number <= 0.2) {
        return 2;
    }
    if (number <= 0.3) {
        return 3;
    }
    if (number <= 0.4) {
        return 4;
    }
    if (number <= 0.5) {
        return 5;
    }
    if (number <= 0.6) {
        return 6;
    }
    if (number <= 0.7) {
        return 7;
    }
    if (number <= 0.8) {
        return 8;
    }
    if (number <= 0.9) {
        return 9;
    }
    if (number <= 1) {
        return 10;
    }
}

let n = 1000000000;
let dictionary = {};
for (let i = 0; i < n; i++) {
    num = getrandomnumberbetween1and10();
    if (!dictionary.hasOwnProperty(num)) {
        dictionary[num] = 0;
    }

    dictionary[num] += 1;
}

console.log(dictionary)