let start = 10;
let secondStart = start;

function getStartParameter(start){
    console.log(start);
    if (start < 1) {
        return start;
    } else {
       return getStartParameter(--start);
    };
};
function secondGetSecondStartParameter(secondStart){
    console.log(secondStart);
    if (secondStart > 0) {
        return getStartParameter(secondStart--);
    } else { 
        return secondStart;
    };
};

getStartParameter(start);
secondGetSecondStartParameter(secondStart);