function solution(arr) {
    let len = arr.length//6
    let a = 1
    while (a < len) {
        a *= 2
    }

    for (let i = len; i < a; i++) {
        arr.push(0)
    }

    return arr
}