let prize = prompt("Podaj liczbę: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 lub 10.");
prize = Number(prize);
let message = "Wybrana opcja to: maskotka "; 

switch (prize) {
    case 0:
        message += "miś.";
        break;
    case 1:
        message += "żyrafa.";
        break;
    case 2:
        message += "żółwik.";
        break;
    case 3:
        message += "tygrys.";
        break;
    case 4:
        message += "dinozaur.";
        break;            
    case 5:
        message += "ufoludek.";
        break;
    case 6:
        message += "wąż.";
        break;
    case 7:
        message += "papuga.";
        break;
    case 8:
        message += "hipcio.";
        break;
    case 9:
        message += "słonik.";
        break;
    case 10:
        message += "piesek.";
        break;        
    default:
        message = "Niestety dokonałeś błędnego wyboru.";
        break;
}
alert(message);