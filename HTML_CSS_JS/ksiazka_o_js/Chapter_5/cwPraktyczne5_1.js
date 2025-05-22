const maxValueForUser = 10;
let randomNumber = Math.floor(Math.random() * maxValueForUser) + 1;
console.log(randomNumber);

let answerUserIs = false;
let answerNumber = 0;

while (!answerUserIs) {
    let answer = prompt("Podaj liczbę w zakresie od 1 do 10, całkowitą. ");
    answer = Number(answer);
    
    if (answer === randomNumber) {
        answerNumber++;
        alert(`Podałeś prawidłową odpowiedż, liczba do odgadnięcia, to: ${answer}. Odgadłeś liczbę w próbie: ${answerNumber}.`);
        answerUserIs = true;
    } else if (answer < randomNumber) {
        alert(`Podałeś za małą liczbę, twoja odpowiedź, to: ${answer}`);
        answerNumber++;
    } else if (answer > randomNumber) {
        alert(`Podałeś za dużą liczbę, twoja odpowiedź, to: ${answer}`);
        answerNumber++;
    }
}
alert("Koniec gry!");