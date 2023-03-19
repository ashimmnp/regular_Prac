let points = (p2,p3) => {
    let b1 = p2*2;
    let b2 = p3*3;
    let tot = b1 + b2;
    return tot;
}
let t1 = points(1,1);
let t2 = points(7,5);
let t3 = points(38,8);
console.log("Total Points of Team 1:",t1);
console.log("Total Points of Team 2:",t2);
console.log("Total Points of Team 3:",t3);
