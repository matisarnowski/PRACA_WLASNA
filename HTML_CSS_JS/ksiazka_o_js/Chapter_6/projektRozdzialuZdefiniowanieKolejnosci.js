let one = () => console.log("jeden");
let two = () => console.log("dwa");
function threeFunction() {
    console.log("trzy");
    one();
    two();
}
function fourFunction() {
    console.log("cztery");
}

setTimeout(fourFunction(), 0);
setTimeout(threeFunction(), 1);
setTimeout(one(), 4);