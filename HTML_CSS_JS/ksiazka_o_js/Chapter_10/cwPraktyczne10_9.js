buttonFirst = document.body.childNodes[1].childNodes[1].innerHTML;
buttonSecond = document.body.childNodes[1].childNodes[1].nextElementSibling.innerHTML;
buttonThird = document.body.childNodes[1].childNodes[1].nextElementSibling.nextElementSibling.innerHTML;
console.log(buttonFirst, buttonSecond, buttonThird);
buttons = document.querySelectorAll("button");
function output(item) {
    /**
     * Outputs the text content of an item to the console.
     * 
     * @param {HTMLElement} item - The item to output the text content of.
     * @returns {void}
     */
    console.log(item.textContent);
}
for (let i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener("click", function () {
        console.log(this.textContent);
    });
    output(buttons[i]);
}
