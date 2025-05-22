let myListWithNames = ["Laura", "Michał", "Ludwik",
    "Katarzyna", "Joanna", "Laura", "Michał", "Laura", "Michał", "Laura",
    "Michał"];

let myListToDisplay = ["Laura", "Michał", "Ludwik",
    "Katarzyna", "Joanna", "Laura", "Michał", "Laura", "Michał", "Laura",
    "Michał"];

let myNewListWithNames = [];
for (let i = 0; i < myListWithNames.length; i++) {
    if (i == myListWithNames.indexOf(myListWithNames[i])) {
        myNewListWithNames.push(myListWithNames[i]);
    };
}

myListToDisplay = myListToDisplay.filter((value, index, array) => { return array.indexOf(value) === index });
console.log(myNewListWithNames);
console.log(myListToDisplay);