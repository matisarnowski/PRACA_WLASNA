function addTwoNumbers(firstNumber, secondNumber) {
    return firstNumber + secondNumber;
};
function oddTwoNumbers(firstNumber, secondNumber) { 
    return firstNumber - secondNumber;
};

function promptNumbersAndSign() {
    let firstNumber = prompt("Podaj pierwszą liczbę: ");
    firstNumber = Number(firstNumber);
    let sign = prompt("Podaj znak działania + lub -. ");
    let secondNumber = prompt("Podaj drugą liczbę do działania: ");
    secondNumber = Number(secondNumber);

    if (sign === "+") {
        return addTwoNumbers(firstNumber, secondNumber);
    } else if (sign === "-") {
        return oddTwoNumbers(firstNumber, secondNumber);
    } else {
        return "Podałeś błędne działanie, nie ma go w zakresie kalkulatora. ";
    }
};

let passMyFunctionToOddOrAdd = promptNumbersAndSign();

console.log(passMyFunctionToOddOrAdd);