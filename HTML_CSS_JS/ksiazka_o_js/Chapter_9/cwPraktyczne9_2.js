let myWindowLocation = 'Protokół: ' + window.location.protocol + ' lokalizacja: ' + window.location.href;

let protocol = document.querySelector(".protocol");
document.getElementById("protocol").innerHTML = myWindowLocation;
console.log(myWindowLocation);