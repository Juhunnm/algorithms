
function solution(arr, n) {
    if (arr.length % 2 !== 0) {
        for (let i = 0; i < arr.length; i++) {
            if (i % 2 == 0) {
                arr[i] += n
            }
        }
    }
    if (arr.length % 2 == 0) {
        for (let j = 0; j < arr.length; j++) {
            if (j % 2 !== 0) {
                arr[j] += n
            }
        }
    }

    return arr
}
console.log(solution([49, 12, 100, 276, 33], 27));
