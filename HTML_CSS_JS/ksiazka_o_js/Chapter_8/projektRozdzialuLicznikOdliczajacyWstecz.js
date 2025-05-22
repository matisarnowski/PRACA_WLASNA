let endDateCounting;
endDateCounting = new Date("2024", "0", "1", "0", "0", "0");

function endDate(endDateCounting, nowIs) {
    return Date.parse(endDateCounting) - Date.parse(nowIs);
}

function countdown() {
    let nowIs = new Date();
    let todayIsDay = Math.floor(endDate(endDateCounting, nowIs) / (1000 * 60 * 60 * 24));
    let todayIsHours = Math.floor(endDate(endDateCounting, nowIs) / (1000 * 60 * 60)) - todayIsDay * 24;
    let todayIsMinutes = Math.floor(endDate(endDateCounting, nowIs) / (1000 * 60)) - todayIsHours * 60 - todayIsDay * 60 * 24;
    //let todayIsSeconds = endDate(endDateCounting, nowIs) / 1000 - todayIsMinutes * 60 - todayIsHours * 60 * 60 - todayIsDay * 60 * 60 * 24;
    let myDateToday = new MyDateToday(todayIsDay, todayIsHours, todayIsMinutes, endDate(endDateCounting, nowIs) / 1000 - todayIsMinutes * 60 - todayIsHours * 60 * 60 - todayIsDay * 60 * 60 * 24);
    console.log(myDateToday.getDay);
    let myDateToString = "Pozostało dni: " + myDateToday.getDay + ", godzin: " + myDateToday.getHours + ", minut: " + myDateToday.getMinutes + ", sekund: " + myDateToday.getSeconds + ".";
    document.getElementById("countdown").innerHTML = myDateToString;
}
class MyDateToday {
    #day;
    #hours;
    #minutes;
    #seconds;

    constructor(day, hours, minutes, seconds) {
        this.#day = day;
        this.#hours = hours;
        this.#minutes = minutes;
        this.#seconds = seconds;
    }

    set setDay(day) { this.#day = day; }
    get getDay() { return this.#day; }

    set setHours(hours) { this.#hours = hours; }

    get getHours() { return this.#hours; }

    set setMinutes(minutes) { this.#minutes = minutes; }

    get getMinutes() { return this.#minutes; }

    set setSeconds(seconds) { this.#seconds = seconds; }

    get getSeconds() { return this.#seconds; }

}

setInterval("countdown()", 1000);

