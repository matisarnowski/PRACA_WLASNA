class Animal {
    
    constructor(name, weight, pseudonym, age, sound) {
        this.name = name;
        this.weight = weight;
        this.pseudonym = pseudonym;
        this.age = age;
        this.sound = sound;
    };

    giveMeaSound() {
        return `${this.sound} ${this.sound}`;  
    };
};

let martha = new Animal("Tygrysek", 40, "Martusia", 6, "Miau, miau!");
let arthur = new Animal("Dinozaur", 35, "Arturek", 4, "Aghgggg!");

Animal.prototype.presentHere = function () { console.log("Jestem " + this.pseudonym + " moje zwierzątko to: " + this.name + "."); };

console.log(`Waga Marty: ${martha.weight}.`);
martha.presentHere();
console.log(`Artur wydaje takie dźwięki: ${arthur.giveMeaSound()}`);