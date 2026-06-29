T = int(input())
arr = []

def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n -1)+fibonacci(n-2)

for tase_case in range(1,T+1):
    arr.append(fibonacci(tase_case))

print(arr)
