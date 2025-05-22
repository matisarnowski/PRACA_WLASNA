loremIpsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut viverra magna ac massa dignissim, ut condimentum arcu sodales. Donec nec nisl orci. Phasellus finibus porttitor accumsan. Praesent placerat cursus enim a elementum. Morbi ut tellus est. Vestibulum iaculis sed enim vel suscipit. Pellentesque eu bibendum diam, nec euismod mi. Sed.";

function myCapitalization(text) {
    text = text.toLowerCase();
    text = text.split(" ");
    text = text.map(value => value.charAt(0).toUpperCase() + value.slice(1));
    text = text.join(" ");
    return text;
}

loremIpsum = myCapitalization(loremIpsum);

console.log(loremIpsum);