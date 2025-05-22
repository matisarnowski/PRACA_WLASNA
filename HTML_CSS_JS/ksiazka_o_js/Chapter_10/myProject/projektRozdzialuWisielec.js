let myWords = ["Honor", "Particularly", "Rice", "Lady", "Alone", "Throughout", "Layers", "Atomic", "Port", "Silence", "Notice", "Offer", "Wish", "Dirty", "Which", "Red", "Attached", "Saw", "Orbit"];
const game = { cur: "", solution: "", puzz: [], total: 0 };
let totalScore = 0;
let gameArea = document.querySelector(".gameArea");
let score = document.querySelector(".score");
let puzzle = document.querySelector(".puzzle");
let letters = document.querySelector(".letters");
let btn = document.querySelector("button");
let totalTotalScore = document.createElement("div");
let comment = document.createElement("div");
totalTotalScore.innerHTML = totalScore;
comment.innerHTML = "Twój całkowity wynik, to: ";
gameArea.appendChild(comment);
gameArea.appendChild(totalTotalScore);

btn.addEventListener("click", startGame);;

/**
 * Starts the game.
 */
function startGame() {
    if (myWords.length > 0) {
        btn.style.display = 'none';
        game.puzz = [];
        game.total = 0;
        game.cur = myWords.shift();
        game.solution = game.cur.split("");
        builder();
        let tempA = Number(totalTotalScore.textContent);
        tempA += totalScore;
        totalTotalScore.innerHTML = tempA;
        totalScore = 0;
    } else {
        score.textContent = "To było ostatnie słowo.";
    }
};
/**
 * Creates an element and appends it to the parent element.
 * @param {string} elType - The type of the element to create.
 * @param {HTMLElement} parentEle - The parent element to append the created element to.
 * @param {string} output - The text content of the created element.
 * @param {string} cla - The class name of the created element.
 * @returns {HTMLElement} - The created element.
 */
function createElements(elType, parentEle, output, cla) {
    const temp = document.createElement(elType);
    temp.classList.add("boxE");
    parentEle.append(temp);
    temp.textContent = output;
    return temp;
}
/**
 * Updates the score element.
 */
function updateScore() {
    score.textContent = `Liczba pozostałych liter: ${game.total}`;
    if (game.total <= 0) {
        console.log("Koniec gry");
        score.textContent = "Koniec gry";
        btn.style.display = "block";
    }

}
/**
 * Builds the puzzle and letters elements.
 */
function builder() {
    letters.innerHTML = "";
    puzzle.innerHTML = "";

    game.solution.forEach((lett) => {
        let div = createElements("div", puzzle, "-", "boxE");
        if (lett == " ") {
            div.style.borderColor = "white";
            div.textContent = " ";
        } else {
            game.total++;

        }
        game.puzz.push(div);
        updateScore();
    })
    for (let i = 0; i < 26; i++) {
        let temp = String.fromCharCode(65 + i);
        let div = createElements("div", letters, temp, "box");
        let checker = function (e) {
            div.style.backgroundColor = "#ddd";
            div.classList.remove("box");
            div.classList.add("boxD");
            div.removeEventListener("click", checker);
            checkLetter(temp);
        }
        div.addEventListener("click", checker);
    }

}
/**
 * Checks if the selected letter is in the solution and updates the puzzle and score accordingly.
 * @param {string} letter - The selected letter.
 */
function checkLetter(letter) {
    console.log(letter);
    game.solution.forEach((ele, index) => {
        if (ele.toUpperCase() == letter) {
            game.puzz[index].textContent = letter;
            game.total--;
            updateScore();
            totalScore++;
        };
    });
}
