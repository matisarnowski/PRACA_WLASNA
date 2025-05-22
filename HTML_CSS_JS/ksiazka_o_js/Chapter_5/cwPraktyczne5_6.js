let myTabel = [];

let counter = 0;
let maxRange = 10;

while (counter < maxRange) {
    myTabel[counter] = counter;
    counter++;
};
console.log(myTabel);

for (let i = 0; i < myTabel.length; i++) {
    console.log(myTabel[i]);
};

for (let element of myTabel) {
    console.log(element);
};