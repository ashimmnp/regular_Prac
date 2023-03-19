let addUp = (a) =>{
let sum = 0;
for (let i = 0; i<=a; i++){
    sum = sum + i
}
return sum;
}
no1 = addUp(4);
no2 = addUp(13);
no3 = addUp(600);
console.log("Added up number1: ",no1);
console.log("Added up number2: ",no2);
console.log("Added up number3: ",no3);