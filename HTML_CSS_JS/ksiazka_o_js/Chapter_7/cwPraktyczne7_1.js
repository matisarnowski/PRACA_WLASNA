class Person {
    #firstName;
    #lastName;
    constructor(firstName, lastName) {
        this.#firstName = firstName;
        this.#lastName = lastName;
    };

    set setFirstName(firstName) {
        this.#firstName = firstName;
    };

    get getFirstName() {
        return this.#firstName;
    };

    set setLastName(lastName) {
        this.#lastName = lastName;
    };

    get getLastName() {
        return this.#lastName;
    };
};

let mati = new Person("Mateusz", "Lipecki");
let seba = new Person("Sebastian", "Bach");

console.log(`Siema ${mati.getFirstName} ${mati.getLastName}.`);
console.log(`Siema ${seba.getFirstName} ${seba.getLastName}.`);