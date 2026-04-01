function solution(arr, flag) {
    var answer = [];
    flag.map((v, i) => {
        if (v === true) {
            for (let j = 0; j < (arr[i] * 2); j++) {
                answer.push(arr[i])
            }
        } else {
            for (let j = 0; j < arr[i]; j++) {
                answer.pop()
            }
        }
    })
    return answer;
}

console.log(solution([3, 2, 4, 1, 3], [true, false, true, false, false]));