function solution(my_string) {
    return my_string.split(" ").filter((v, i) => v !== "")
}
console.log(solution("    programmers  "));

// console.log(solution("i love you"));
// [ '', '', '', '', 'programmers', '', '' ]
