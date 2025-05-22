let myWord = "";
let numberIsNot = 5;

for (let i = 0; i < 100; i++) {
    if (!(i % numberIsNot)) {
        continue;
    };
    myWord += i;
};
console.log(myWord);