function addNameOfCandidate(item, index, value) {
    let tr = document.createElement("tr");
    let tdOne = document.createElement("td");
    tdOne.textContent = index + 1;
    tr.append(tdOne);
    let tdTwo = document.createElement("td");
    tdTwo.textContent = item;
    tr.append(tdTwo);
    let tdThree = document.createElement("td");
    tdThree.textContent = value;
    tr.append(tdThree);
    tr.onclick = function () {
        let count = Number(tr.lastChild.textContent);
        count++;
        tr.lastChild.textContent = count;
    };
    tableName.appendChild(tr);
};
let myArray = ["Sebastian", "Adam", "Miłosz", "Czarek", "Joanna", "Paula", "Piotr"];
let message = document.querySelector("#message");
let inputName = document.querySelector("#addFriend");
let buttonName = document.querySelector("#addNew");
let tableName = document.getElementById("output");
myArray.forEach((item, index) => {
    addNameOfCandidate(item, index, 0);
});
buttonName.onclick = function () {
    addNameOfCandidate(inputName.value, myArray.length, 0);
    if (inputName.value !== "") {
        let div = document.createElement("div");
        div.innerHTML = "Dodano kandydata nr: " + (myArray.length + 1);
        message.appendChild(div);
    }
    myArray.push(inputName.value);
}

