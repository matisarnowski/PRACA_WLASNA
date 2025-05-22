const elem1 = document.querySelector(".output")
output = "To jest uaktualniony tekst elementu elem1."
elem1.textContent = output;
const tester = document.getElementById("tester")
tester.classList.add("red");
tester.style.background = "#ff0000";
url = window.location.href;
elem1.textContent += " A to jest adres URL elementu: " + url;
