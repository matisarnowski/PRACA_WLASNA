let loremIpsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut viverra magna ac massa dignissim, ut condimentum arcu sodales. Donec nec nisl orci. Phasellus finibus porttitor accumsan. Praesent placerat cursus enim a elementum. Morbi ut tellus est. Vestibulum iaculis sed enim vel suscipit. Pellentesque eu bibendum diam, nec euismod mi. Sed.";

loremIpsum = loremIpsum.toLowerCase();

let myTabWithLetters = ["a", "e", "i", "o", "u"];

for (let i = 0; i < myTabWithLetters.length; i++) {
    console.log(myTabWithLetters[i]);
    loremIpsum = loremIpsum.replaceAll(myTabWithLetters[i], myTabWithLetters.indexOf(myTabWithLetters[i]));
}
console.log(loremIpsum);

