el = document.querySelector(".something");
allElements = document.querySelectorAll(".something");
console.log(el);
for (let i = 0; i < allElements.length; i++) {
    console.dir(allElements[i].innerHTML);
}