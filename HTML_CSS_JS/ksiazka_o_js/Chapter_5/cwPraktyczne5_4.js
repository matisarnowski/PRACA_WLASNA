let myTable = [];
const numbersOfRows = 10;
const numbersOfColumns = 10;
let counter = 0;

for (let i = 0; i < numbersOfRows; i++) {
    let tempTable = [];
    for (let j = 0; j < numbersOfColumns; j++) {
        tempTable.push(i * 10 + j + 1);
    }
    myTable.push(tempTable);
}
console.table(myTable);