let myVariableWithString = "Mateusz Sarnowski";

function myFunction(myVariableWithString) {

    let i = myVariableWithString.length;
    let encryptedWord = "";
    while (i > 0) {
        i--;
        let myEncryptedIndexOfLetter = Math.floor(Math.random() * myVariableWithString.length)
        let myEncryptedLetter = myVariableWithString[myEncryptedIndexOfLetter];
        encryptedWord += myEncryptedLetter;
        console.log(encryptedWord);

        myVariableWithString = myVariableWithString.slice(0, myEncryptedIndexOfLetter) + myVariableWithString.slice(myEncryptedIndexOfLetter + 1);

        console.log(myVariableWithString);

    }
}

myFunction(myVariableWithString);