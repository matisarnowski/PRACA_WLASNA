let myWordsOneThousand = "1000";

(function () {
    let myWordsOneThousand = "jeden tysiąc";
    console.log(myWordsOneThousand);
})();

let result = "1002";
result = (function () {
    let result = "1001";
    return result;
})();
console.log(result);
console.log(result = result);

let resultSecond = "1003";

let myFunctionWithParametr = (function (resultSecond) {
    let myFunctionWithParametr = resultSecond;
    return `Oto część ciągu tekstowego: ${myFunctionWithParametr}`;
})();

console.log(myFunctionWithParametr = resultSecond);