let myTabWithNumbers = [];

for (let i = 0; i < 100; i++) {
    myTabWithNumbers.push(Math.floor(Math.random() * 100));
}

console.table(myTabWithNumbers);

myTabWithNumbers = myTabWithNumbers.map(x => x * 2);

console.table(myTabWithNumbers);