class Employee {
    #firstName;
    #lastName;
    #seniority;
    constructor(firstName, lastName, seniority) {
        this.#firstName = firstName;
        this.#lastName = lastName;
        this.#seniority = seniority;
    };

    get getFirstName() {
        return this.#firstName;
    }

    set setFirstName(firstName) {
        this.#firstName = firstName;
    };
    
    get getLastName() {
        return this.#lastName;
    }

    set setFirstName(lastName) {
        this.#lastName = lastName;
    };

    get getSeniority() {
        return this.#seniority;
    };

    set setSeniority(seniority) {
        this.#seniority = seniority;
    };
}


mati = new Employee("Mateusz", "Sarnowski", 0);
seba = new Employee("Sebastian", "Bach", 1);

myTabWithEmployees = [mati, seba];

Employee.prototype.returnInformationAboutEmployee = function () { return "Imię pracownika " + this.getFirstName + " nazwisko pracownika: " + this.getLastName + " staż pracy pracownika: " + this.getSeniority; };
Employee.prototype.setInformationForEmployee = function (name) { this.setFirstName = name; };
Employee.prototype.increaseSeniorityOfEmployee = function () {
    let seniority = this.getSeniority;
    seniority++;
    this.setSeniority = seniority;
}

newNames = ["Alicja", "Małgorzata"];

for (let i = 0; i < myTabWithEmployees.length; i++) {
    console.log(myTabWithEmployees[i].returnInformationAboutEmployee());
    myTabWithEmployees[i].setInformationForEmployee(newNames[i]);
    myTabWithEmployees[i].increaseSeniorityOfEmployee();
    console.log(myTabWithEmployees[i].returnInformationAboutEmployee());
}