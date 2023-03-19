let oddishOrEvenish = (a) =>{
let s = 0;
while (a >0){
    c = a % 10;
    s += c;
    a = (a - c)/10;
}
if (s%2==0){
    return "Evenish";
}
else {
    return "Oddish";
}
}

no1 = oddishOrEvenish(43);
no2 = oddishOrEvenish(373);
no3 = oddishOrEvenish(4433);
console.log("no1 is: ",no1);
console.log("no2 is: ",no2);
console.log("no3 is: ",no3);