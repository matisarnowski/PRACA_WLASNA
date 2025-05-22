let myStartedVariable = prompt("Podaj liczbę mniejszą niż 10: ");
myStartedVariable = Number(myStartedVariable);
let mySecondStartedVariable = myStartedVariable;
function myRecursionFunction(myStartedVariable) {
    console.log(myStartedVariable);
    if (myStartedVariable < 10) {
        return myRecursionFunction(++myStartedVariable);
    } else {
        return myStartedVariable;
    };
};
function mySecondRecursionFunction(mySecondStartedVariable) {
    console.log(mySecondStartedVariable);
    if (mySecondStartedVariable > 9) {
        return mySecondStartedVariable;
    } else {
        return mySecondRecursionFunction(++mySecondStartedVariable);
    };
};

myRecursionFunction(myStartedVariable);
mySecondRecursionFunction(mySecondStartedVariable);