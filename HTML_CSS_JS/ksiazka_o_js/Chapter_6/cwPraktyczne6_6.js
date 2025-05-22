function power(arg) {
    console.log(arg)
    if (arg === 0) return 1;
    else return arg * power(arg - 1); 
}

let myArgument = prompt("Podaj liczbę z zakresu od 0 do nieskończoności naturalną: ");

alert(power(myArgument));