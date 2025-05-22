console.log(decodeURIComponent("Jaka%20dzisiaj%20pogoda%3F"));
console.log(encodeURIComponent("Jaka dzisiaj pogoda?"));
let urlAdress = "http://www.google.pl/maps/place/Toruń";
let encodeURLAdress = encodeURI(urlAdress);
console.log(encodeURLAdress);
let secondURLAddress = "http://www.basescripts.com?=Witaj, świecie";
encodeSecondAddress = encodeURIComponent(secondURLAddress);
console.log(encodeSecondAddress);
console.log(decodeURIComponent(encodeSecondAddress));
