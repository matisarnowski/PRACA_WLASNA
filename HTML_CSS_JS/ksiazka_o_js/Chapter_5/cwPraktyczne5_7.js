let myObject = { name: "Mateusz", surname: "Sanowski", dateOfBirth: 1988 };

for (let property in myObject) {
    console.log(`${property}: ${myObject[property]}`);
}

let myTable = Object.keys(myObject);

for (let i = 0; i < myTable.length; i++) {
    console.log(`${myTable[i]}: ${myObject[myTable[i]]}`)
};