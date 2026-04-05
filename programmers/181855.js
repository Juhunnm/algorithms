function solution(strArr) {
    var answer = {};
    for (let str of strArr) {
        console.log(str.length)
        answer[str.length] = (answer[str.length] ?? 0) + 1
    }
    return Math.max(...Object.values(answer))
}
console.log(solution(["a", "bc", "d", "efg", "hi"]))