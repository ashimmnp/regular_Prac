function binary(deciNum){
    let num = '';
    let q = deciNum;
    while (q !==0){
        num = (q%2) + num;
        q = Math.floor(q/2);
    }
    return num;
}
let deci1 = binary(1);
let deci5 = binary(5);
let deci10 = binary(10);
console.log("In binary of 1 is: ",deci1);
console.log("In binary of 5 is: ",deci5);
console.log("In binary of 10 is: ",deci10);