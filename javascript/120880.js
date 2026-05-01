function solution(numlist, n) {
    return numlist.sort((a, b) => {
        const distA = Math.abs(a - n)
        const distB = Math.abs(b - n)

        if (distA === distB) {
            return (b - n) - (a - n)
        }
        return distA - distB
    })

}
console.log(solution([1, 2, 3, 4, 5, 6], 4));