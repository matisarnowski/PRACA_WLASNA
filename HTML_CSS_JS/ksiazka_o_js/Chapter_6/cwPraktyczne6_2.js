let myTabWithWords = ["Kochany", "Miły", "Uprzejmy", "Ambitny", "Waleczny", "Odważny", "Inteligentny", "Zaradny", "Człowiek z Pasją", "Obdarzony wiedzą", "Obdarzony łaską", "Cichy", "Spokojny", "Małowówny", "Elokwentny", "Mistyk", "Naukowiec", "Żołnierz Chrystusa", "Mnich Buddyjski", "Jogin", "Pustelnik"];

function PromptName () { 
    let name = prompt("Podaj swoje imię: ");
    return name;
};
let caseOfCharacterNumber = Math.floor((Math.random() * 100) % myTabWithWords.length);
console.log(caseOfCharacterNumber)
let myFunctionPromptName = PromptName();

console.log(`Masz na imię: ${myFunctionPromptName}, cecha, która dobrze Cię opisuje, to: ${myTabWithWords[caseOfCharacterNumber]}.`);
alert(`Masz na imię: ${myFunctionPromptName}, cecha, która dobrze Cię opisuje, to: ${myTabWithWords[caseOfCharacterNumber]}.`);