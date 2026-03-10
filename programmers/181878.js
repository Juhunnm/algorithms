function solution(myString, pat) {
    let answer = 0;

    if (myString.length < pat.length) return 0

    myString = myString.toLowerCase()
    pat = pat.toLowerCase()

    answer = myString.includes(pat);


    return +answer
}

console.log(solution("aaaa", "aa"))
// console.log(solution("AbCdEfG", "aBc"))
// console.log(solution("aaAA", "aaaaa"))