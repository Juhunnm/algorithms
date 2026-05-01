function solution(a, b) {
    let answer = 0;
    if ((a % 2) !== 0 && (b % 2) !== 0) {
        return a ** 2 + b ** 2
    } else if ((a % 2) !== 0 || (b % 2) !== 0) {
        return 2 * (a + b)
    } else {
        return Math.abs(a - b)
    }
}
