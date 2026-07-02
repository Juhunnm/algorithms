# 4881. [S/W 문제해결 기본] 5일차 - 배열 최소 합 D2

T = int(input())

def dfs (row,total):
    global answer

    if total >= answer:
        return
    
    if row == N:
        if answer > total :
            answer = total
        return
    for col in range(N):
        if visited[col] == 0:
            visited[col] = 1
            dfs(row+1, total + arr[row][col])
            visited[col] = 0

# 모든 행, 현재까지의 합
for tase_case in range(1,T+1):
    N = int(input())
    arr = [[] for _ in range(N)]
    
    answer = 9999999
    visited =[0] * N

    for r in range(N):
        arr[r] = list(map(int,input().split()))

    dfs(0,0)
    print(f"#{tase_case} {answer}")