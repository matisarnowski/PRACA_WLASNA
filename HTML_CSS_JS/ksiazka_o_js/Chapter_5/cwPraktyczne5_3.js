let myWork = [];

for (let i = 0; i < 10; i++) {
    if (i % 2 === 0) {
        myWork.push({name: `Lekcja ${i}`, status: true})
    } else { 
        myWork.push({name: `Lekcja ${i}`, status: false})
    }
};
console.table(myWork);