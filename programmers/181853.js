function solution(num_list) {
    num_list.sort((a, b) => a - b)

    return num_list.slice(0, 5)
}
console.log(solution([12, 4, 15, 46, 38, 1, 14]));
