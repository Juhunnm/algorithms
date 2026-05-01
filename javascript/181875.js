// function solution(strArr) {
//     let answer = [];
//     let len = strArr.length
//     for (let i = 0; i < len; i++) {
//         if (i % 2 !== 0) {
//             strArr[i] = strArr[i].toUpperCase()
//         } else {
//             strArr[i] = strArr[i].toLowerCase()
//         }
//     }
//     return strArr;
// }
function solution(strArr) {
    return strArr.map((v, i) => i % 2 !== 0 ? v.toUpperCase() : v.toLowerCase());
}
console.log(solution(["AAA", "BBB", "CCC", "DDD"]))
console.log(solution(["aBc", "AbC"]));
