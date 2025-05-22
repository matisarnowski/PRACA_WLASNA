let tableOfMultiplications = [];
let value = 10;
for (let i = 1; i <= value; i++) {
    let temp = []
    for (let j = 1; j <= value; j++) {
        temp.push(`${i} * ${j} = ${(i * j)}`);
    }
    tableOfMultiplications.push(temp);
}
console.table(tableOfMultiplications);