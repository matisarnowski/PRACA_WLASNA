let tabItems = ["Kamień", "Papier", "Nożyce"];
let yourScores = 0;
let computerScores = 0;
let message = "Dostajecie następującą ilość punktów: ";
const match = 3;
while ((yourScores < match) && (computerScores < match)) {
    let computerRun = Math.floor((Math.random() * 10)) % 3;
    computerRun = tabItems[computerRun];
    let yourRun = Math.floor((Math.random() * 10)) % 3;
    yourRun = tabItems[yourRun];

    if (yourRun === tabItems[0] && computerRun === tabItems[0]){
        message += "TY: 0, KOMPUTER: 0. Jest remis. Wybraliście oboje: ";
        message += yourRun;
    } else if (yourRun === tabItems[1] && computerRun === tabItems[1]) {
        message += "TY: 0, KOMPUTER: 0. Jest remis. Wybraliście oboje: ";
        message += yourRun;
    } else if (yourRun === tabItems[2] && computerRun === tabItems[2]) {
        message += "TY: 0, KOMPUTER: 0. Jest remis. Wybraliście oboje: ";
        message += yourRun;
    } else if ((yourRun === tabItems[0] && computerRun === tabItems[1]) || (yourRun === tabItems[1] && computerRun === tabItems[2]) || (yourRun === tabItems[2] && computerRun === tabItems[0])) {
        message += "TY: 0, KOMPUTER: 1. Komputer tym razem wygrywa. Ty wybrałeś: ";
        message += yourRun;
        message += ", a komputer wybrał: ";
        message += computerRun;
        computerScores++;
    } else if ((yourRun === tabItems[1] && computerRun === tabItems[0]) || (yourRun === tabItems[2] && computerRun === tabItems[1])|| (yourRun === tabItems[0] && computerRun === tabItems[2])) {
        message += "TY: 1, KOMPUTER: 0. Tym razem to Ty wygrywasz. Wybrałeś: ";
        message += yourRun;
        message += ", a komputer wybrał: ";
        message += computerRun;
        yourScores++;
    } else {
        message = "Coś jest nie tak.";
    }
    console.log(message);    
    message = "Dostajecie następującą ilość punktów: ";
}
if (yourScores > computerScores) {
    alert(`Wygrałeś, potyczkę do: ${computerScores}`);
} else {
    alert(`Wygrał komputer do : ${yourScores}`);
}