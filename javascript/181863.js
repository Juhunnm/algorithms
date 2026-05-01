function solution(rny_string) {
    return [...rny_string].map((v) => v === "m" ? v = "rn" : v).join('')
}
console.log(solution("masterpiece"));
