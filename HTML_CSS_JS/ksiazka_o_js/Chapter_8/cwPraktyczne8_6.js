let numberPI = Math.PI;
console.log("Liczba PI: ", numberPI);
console.log("Zaokrąglenie liczby 5,7, w dół: ", Math.floor(5.7));
console.log("Zaokrąglenie liczby 5,7, w górę: ", Math.ceil(5.7));
let randomNumber = Math.floor(Math.random() * 100);
console.log("Losowo wybrana liczba: ", randomNumber);
let randomNumberFrom0to100 = Math.floor(Math.random() * 100);
let randomNumberFrom1To100 = Math.ceil(Math.random() * 99);
let randomNumberFrom1To10 = Math.ceil(Math.random() * 9);

function myFunctionToRandomNumber() {
    let myTabelWithRandomNumbers = {};
    for (let i = 0; i < 10; i++) {
        let myFirstTabelWithRandomNumbers = [];
        for (let j = 0; j < 10; j++) {
            myFirstTabelWithRandomNumbers.push(Math.floor(Math.random() * 100));
        }
        let myTabelAssisted = myFirstTabelWithRandomNumbers.map(Number);
        myTabelAssisted.sort();
        minValue = myTabelAssisted[0];
        maxValue = myTabelAssisted[myTabelAssisted.length - 1];
        console.log(myTabelAssisted);
        myTabelWithRandomNumbers["min:" + i] = minValue;
        myTabelWithRandomNumbers["max:" + i] = maxValue;
    }
    return myTabelWithRandomNumbers;
}
console.table(myFunctionToRandomNumber());