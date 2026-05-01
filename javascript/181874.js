function solution(myString) {
    myString = myString.toLowerCase();
    return [...myString].map((v, i) => v === "a" ? v.toUpperCase() : v).join("");
}
console.log(
    solution("PrOgRaMmErS")

);