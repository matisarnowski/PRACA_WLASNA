let dateNow = new Date();
let dateToPolishFormat = dateNow;
dateNow = dateNow.toLocaleDateString("pl-PL");
console.log(dateNow);
tableWithMonths = ["Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec", "Lipiec", "Sierpień", "Wrzesień", "Październik", "Listopad", "Grudzień"];
let dayOfMonth = dateToPolishFormat.getDate();
let yearNow = dateToPolishFormat.getFullYear();
let monthOfYear = dateToPolishFormat.getMonth();
let todayToPolish = "Dziś jest: " + dayOfMonth + ", miesiąc: " + tableWithMonths[monthOfYear] + " roku: " + yearNow;
document.getElementById("date").innerHTML = todayToPolish;
function myTimer() {
    let dateNowInLoop = new Date();
    if (dateNowInLoop.getMinutes() < 10) {
        let nowIsTheTime = " " + dateNowInLoop.getHours() + ": 0" + dateNowInLoop.getMinutes() + ": " + dateNowInLoop.getSeconds();
        document.getElementById("time").innerHTML = nowIsTheTime;
    } else if (dateNowInLoop.getMinutes() < 10 && dateNowInLoop.getSeconds() < 10) {
        let nowIsTheTime = " " + dateNowInLoop.getHours() + ": 0" + dateNowInLoop.getMinutes() + ": 0" + dateNowInLoop.getSeconds();
        document.getElementById("time").innerHTML = nowIsTheTime;
    } else if (dateNowInLoop.getSeconds() < 10) {
        let nowIsTheTime = " " + dateNowInLoop.getHours() + ": " + dateNowInLoop.getMinutes() + ": 0" + dateNowInLoop.getSeconds();
        document.getElementById("time").innerHTML = nowIsTheTime;
    } else {
        let nowIsTheTime = " " + dateNowInLoop.getHours() + ": " + dateNowInLoop.getMinutes() + ": " + dateNowInLoop.getSeconds();
        document.getElementById("time").innerHTML = nowIsTheTime;
    }
}
setInterval("myTimer()", 1000);
