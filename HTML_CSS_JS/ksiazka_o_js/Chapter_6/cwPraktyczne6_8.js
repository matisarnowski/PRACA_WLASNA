let myVariableWithFunction = function myFunctionToVariable(argument){console.log(argument)};
function myFunctionToVariable(argument){console.log(argument)};
myVariableWithFunction("To jest napis przekazany funkcji");
myFunctionToVariable("To jest argument przekazany do tej samej funkcji, ale bez przypisywania jej do zmiennej.")