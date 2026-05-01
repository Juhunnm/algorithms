const solution = (num_list) => {
    let answer = 0;
    const len = num_list.length
    if (len >= 11) {
        for (let i = 0; i < len; i++) {
            answer += num_list[i]
        }
    } else {
        answer = 1
        for (let i = 0; i < len; i++) {
            answer *= num_list[i]
        }
    }
    return answer;
}
// [3, 4, 5, 2, 5, 4, 6, 7, 3, 7, 2, 2, 1]
// [2, 3, 4, 5]
let result = solution(
    [2, 3, 4, 5])
console.log(result);
