function solution(num_list) {
    let num1 = 0
    let num2 = 0;
    num_list.map((e, i) => {
        if (((i + 1) % 2) === 0) {
            num1 += e;
        } else {
            num2 += e
        }
    })

    return Math.max(num1, num2);
}