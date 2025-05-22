const button = document.getElementById('myButton');
const paragraph = document.getElementById('exampleParagraph');

paragraph.style.backgroundColor = "#ff0000";

button.addEventListener("click", () => {
    paragraph.classList.toggle("hidden");
})