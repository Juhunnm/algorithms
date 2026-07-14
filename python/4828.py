# 4828. [S/W 문제해결 기본] 1일차 - min max D2

T = int(input())

for tase_case in range(1,T+1):
    N = int(input())
    # for i in N:
    #     n = int(input())
    narr = list(map(int,input().split()))
    #직접 구하기
    max_value = narr[0]
    min_value = narr[0]

    for n in narr:
        if n > max_value:
            max_value = n
        if n < min_value:
            min_value = n
    
    # print(f"#{tase_case} {max(narr) - min(narr)}")
    print(f"#{tase_case} {max_value - min_value}")
    
    