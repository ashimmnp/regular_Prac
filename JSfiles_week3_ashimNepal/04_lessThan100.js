let lessThan100 = (a,b) => {
    let c = a + b;
    if (c<100){
        return true;
    }
    return false;
}
let con1 = lessThan100(22,15);
let con2 = lessThan100(83,34);
let con3 = lessThan100(3,77); 
console.log("Condition1: ",con1);
console.log("Condition2: ",con2);
console.log("condition3: ",con3);