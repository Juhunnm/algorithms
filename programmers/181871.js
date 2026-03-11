function solution(myString, pat) {
    let asnwer = 0
    while (myString.indexOf(pat) !== -1) {
        ++asnwer

        myString = myString.slice(myString.indexOf(pat) + 1);

    }
    return asnwer
}
//pop() pat - 1
console.log(solution("banana", "ana"));
console.log(solution("aaaa", "aa"));

console.log(solution("nanana", "nana"));