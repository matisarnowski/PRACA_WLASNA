const output = document.querySelector(".output");
const mainList = document.querySelector("ul");
mainList.id = "mainList";
console.log(mainList);
//const el = document.querySelectorAll("div");
const eles = document.querySelectorAll("div");
//for (let i = 0; i < el.length; i++) {
//    console.log(el[i].tagName);
//    el[i].id = "id" + (i + 1);
//}
for (let x = 0; x < eles.length; x++) {
    console.log(eles[x].tagName);
    eles[x].id = "id" + (x + 1);
    if (x % 2) {
        eles[x].style.color = "red";
    } else {
        eles[x].style.color = "blue";
    }
}