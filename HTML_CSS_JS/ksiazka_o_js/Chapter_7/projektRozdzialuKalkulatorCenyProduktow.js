class Product {
    #price;
    #quantity;
    #order;
    constructor(price, quantity, order = 0.0) {
        this.#price = price;
        this.#quantity = quantity;
        this.#order = order;
    };

    get getPrice() {
        return this.#price;
    };

    set setPrice(price) {
        this.#price = price;
    };

    get getQuantity() {
        return this.#quantity;
    };

    set setQuantity(quantity) {
        this.#quantity = quantity;
    };

    get getOrder() {
        return this.#order;
    };

    set setOrder(order) {
        this.#order = order;
    };

    increaseQuantity(supply) {
        let quantity = this.getQuantity;
        quantity += supply;
        this.setQuantity = quantity;
    };

    decreaseQuantity(reduction) {
        let quantity = this.getQuantity;
        quantity -= reduction;
        if (quantity >= 0) {
            this.setQuantity = quantity;
        } else {
            console.log("Nie masz tyle produktów.");
            console.log("W magazynie masz tylko: " + this.getQuantity);
        };
    };

    getOrderForMoney(quantityOfOrder) {
        if (quantityOfOrder <= this.getQuantity) {
            let order = quantityOfOrder * this.getPrice;
            this.setOrder = order;
            this.decreaseQuantity(quantityOfOrder);
        } else {
            console.log("Nie możesz niestety zrealizować tego zamówienia. Masz za mało towarów. Masz tylko: ", this.getQuantity, " brakuje Ci: ", quantityOfOrder - this.getQuantity);
        };
    };
}

computers = new Product(2345.97, 1000);
consoles = new Product(3487.22, 2500);
fridges = new Product(2501.01, 1500);

myProductsTab = [computers, consoles, fridges];

myOrderTab = [250, 123, 11];

for (let k = 0; k < myOrderTab.length; k++) {
    console.log("Ilość produktu, przed zamówieniem: ", myProductsTab[k].getQuantity);
};

for (let i = 0; i < myProductsTab.length; i++) {
    myProductsTab[i].getOrderForMoney(myOrderTab[i]);
};

for (let j = 0; j < myProductsTab.length; j++) {
    console.log("Aktualnie zamówienie produktu: ", myProductsTab[j].getOrder, " Oraz ilość produktu: ", myProductsTab[j].getQuantity);
}