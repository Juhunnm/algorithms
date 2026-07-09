# 4869. [S/W 문제해결 기본] 4일차 - 종이붙이기 D2

T = int(input() )

for tase_case in range(1,T+1):
    N = int(input())                                                                                                                         
    k = N // 10
    dp = [0] * (k+1)

    dp[1] = 1
    dp[2] = 3

    for i in range(3,k + 1):
        dp[i] = dp[i-1] + 2 * dp[i-2]


        
        
    print(f"#{tase_case} {dp[k]}")