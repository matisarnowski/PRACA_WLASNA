function multiplyByFive(firstNumber) {
    return firstNumber * 5;
};
function multiplySquare(firstNumber) { 
    return firstNumber * firstNumber;
};

function addTwoFunctions(firstNumber) {
    return multiplyByFive(firstNumber) + multiplySquare(firstNumber);
};

let myTabWithScores = [];

for (let i = 0; i < 25; i++) {
    myTabWithScores.push(addTwoFunctions(i));
}

console.table(myTabWithScores);