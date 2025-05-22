function addTwoNumers() {
    let firstNumber = prompt("Podaj pierwszą liczbę, którą mam dodać. ");
    firstNumber = Number(firstNumber);
    let secondNumber = prompt("Podaj drugą liczbę, którą mam dodać. ");
    secondNumber = Number(secondNumber);
    let sum = firstNumber + secondNumber;
    alert(`Suma tych dwóch liczb, to: ${sum}.`)
    return sum
};

let firstPassOfFunction = addTwoNumers();
let secondPassOfFunction = addTwoNumers();

console.log(firstPassOfFunction);
console.log(secondPassOfFunction);