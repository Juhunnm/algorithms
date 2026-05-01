function solution(arr) {
    var answer = [];
    arr.reduce((acc, cur) => {
        for (let i = 0; i < cur; i++) {
            acc.push(cur)
        }
        return acc
    }, answer)
    return answer;
}
console.log(solution([5, 1, 4]))