function solution(numbers, n) {
    let answer = 0
    for (i of numbers) {
        if (answer > n) return answer
        answer += i
    }
    return answer
}