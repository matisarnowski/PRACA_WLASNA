const theList = ['Laurence', 'Svekis', true,
    35, null, undefined, { test: 'one', score: 55 }, ['one', 'two']];
theList.pop();
theList.shift();
theList.pop();
theList.pop();
theList.pop();
theList.unshift("PIERWSZY");
theList[3] = "Witaj, świecie!";
theList[2] = "ŚRODKOWY";
theList.push("OSTATNI");
console.log(theList);