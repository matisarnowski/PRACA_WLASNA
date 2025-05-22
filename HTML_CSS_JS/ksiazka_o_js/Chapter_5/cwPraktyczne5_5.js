let gridOfTable = [];
const cells = 64;
let rows = [];
var columns = 8;
let counter = 0;

while (counter < cells + 1) {
    ++counter;
    rows.push(counter);
    if (counter % 8 === 0) {
        if (rows.length != 0) {
            gridOfTable.push(rows)
        }
        rows = [];
    }    
}
console.table(gridOfTable);