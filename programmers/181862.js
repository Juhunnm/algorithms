function solution(myStr) {
    myStr = ['a', 'b', 'c'].reduce((acc, cur) =>
        acc.replaceAll(cur, " "), myStr).split(" ").filter(v => v != "")
    return myStr.length === 0 ? ["EMPTY"] : myStr
}
console.log(solution("cabab"));
