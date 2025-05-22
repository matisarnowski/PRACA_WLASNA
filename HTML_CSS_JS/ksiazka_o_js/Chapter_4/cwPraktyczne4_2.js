let ageOfUser = prompt("Podaj swój wiek: ");
ageOfUser = Number(ageOfUser);
let message = "";

if (ageOfUser < 19) {
    message = "Masz za mało lat, żeby wejść do lokalu i nie możesz też kupić alkoholu";
} else if (ageOfUser >= 19 && ageOfUser < 21) {
    message = "Możesz wejść do lokalu, ale nie możesz kupić alkoholu";
} else {
    message = "Możesz bawić się do woli w lokalu i kupować alkohol.";
}

alert(message);