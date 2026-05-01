function solution(binomial) {
    const cal = {
        '+': (a, b) => a + b,
        '-': (a, b) => a - b,
        '*': (a, b) => a * b,
    }

    const [a, op, b] = binomial.split(" ")
    return cal[op](+a, +b)
}
console.log(solution("43 + 12"));
