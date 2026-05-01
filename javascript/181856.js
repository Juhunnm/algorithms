function sumArr(arr) {
    return arr.reduce((arr, cur) => arr + cur)
}

function solution(arr1, arr2) {
    if (arr1.length === arr2.length) {
        let a = sumArr(arr1)
        let b = sumArr(arr2)
        if (a > b) return 1
        else if (a < b) return -1
        else return 0
    } else if (arr1.length > arr2.length) return 1
    else return -1
}


console.log(solution([49, 13], [70, 11, 2]))
console.log(solution([100, 17, 84, 1], [55, 12, 65, 36]))