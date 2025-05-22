let elementInput = document.getElementById("addItem");
let elementButton = document.getElementById("addNew");
let elementList = document.getElementById("sList");
function addOne(elementInput, elementList) {
    /**
     * Adds a new item to a list.
     * 
     * @param {HTMLInputElement} elementInput - The input element containing the item value.
     * @param {HTMLUListElement} elementList - The list element to which the item will be added.
     * @returns {void}
     */
    let li = document.createElement('li');
    let item = elementInput.value;
    li.appendChild(document.createTextNode(item));
    elementList.appendChild(li);
}
elementButton.onclick = function () { addOne(elementInput, elementList) };