let titles = document.querySelectorAll(".title");
let myTexts = document.querySelectorAll(".myText");
let nextElement;
for (let element = 0; element < titles.length; element++) {
    titles[element].onclick = function () {
        nextElement = myTexts[element];
        nextElement.classList.add("active");
        nextElement.onclick = function () { this.classList.remove("active"); }
    };
}