allElements = document.querySelectorAll(".something");
console.log(allElements);
for (let i = 0; i < allElements.length; i++) {
    console.dir(allElements.item(i));
}