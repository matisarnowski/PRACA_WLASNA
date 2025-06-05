const tabelOfNames = ["Sebastian", "Cezary", "Miłosz", "Adam", "Joanna", "Marta", "Małgorzata", "Paula", "Piotr", "Kinga", "Pamela", "Jacek"];
function build() {
    /**
      * Builds an HTML table of names, their corresponding indices, and a random number.
      * The table is appended to an element with the id "output" in the document.
      */
    let html = `<h1>tabela moich przyjaciół.</h1><table>`;
    tabelOfNames.forEach((item, index) => {
        dataRandom = Math.floor(Math.random() * 100);
        html += `<tr class="box" data-row="${index + 1}" data-name="${item}" data-random="${dataRandom}" onClick="getData(this)"><td>${item}</td>`;
        html += `<td>${index + 1}</td>`;
        html += `<td>Tutaj jest losowa liczba: ${dataRandom}</td></tr >`;
    });
    html += `</table>`;
    document.getElementById("output").innerHTML = html;
}
function getData(item) {
    elRow = item.getAttribute("data-row");
    elName = item.getAttribute("data-name");
    elRandom = item.getAttribute("data-random");
    console.log(elRow);
    console.log(elName);
    console.log(elRandom);
    document.getElementById("message").innerHTML = `${elName} znajduje się w wierszu ${elRow} i ma losową liczbę ${elRandom}.`;
}
build();