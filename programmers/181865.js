function solution(binomial) {
    var answer = 0;
    binomial = binomial.split(" ")
    console.log(binomial);

    if (binomial[1] === "+") {
        answer = Number(binomial[0]) + Number(binomial[3])
    } else {

        answer = Number(binomial[0]) - Number(binomial[3])
    }
    return answer
}
console.log(solution("43 + 12"));
