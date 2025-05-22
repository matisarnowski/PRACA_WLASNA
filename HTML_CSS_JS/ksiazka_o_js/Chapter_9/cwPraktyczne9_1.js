//let myWindow = window;
//let myWindowText = JSON.stringify(myWindow);
let myDocumentOfWindow = window.document;
let myDocumentOfWindowText = JSON.stringify(myDocumentOfWindow);
let myWidthText = 'To jest szerokość tekstu: ' + window.innerWidth + '';
let myHeightText = 'To jest wysokość tekstu: ' + window.innerHeight + '';

let documentList = "<ul>";
for (let el in myDocumentOfWindow) { documentList += "<li>" + el + "</li>"; };
documentList += "</ul>";
//console.log(myWindowText);
console.log(myDocumentOfWindowText);
console.log(myWidthText);
console.log(myHeightText);
document.getElementById("przykładowe-ID-1").innerHTML = documentList;
document.getElementById("przykładowe-ID-2").innerHTML = myDocumentOfWindowText;
document.getElementById("przykładowe-ID-3").innerHTML = myWidthText;
document.getElementById("przykładowe-ID-4").innerHTML = myHeightText;