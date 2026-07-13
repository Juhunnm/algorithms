# 4828. [S/W 문제해결 기본] 1일차 - min max D2


from uuid import MAX


T = int(input())

for tase_case in range(1,T+1):
    N = int(input())
    # for i in N:
    #     n = int(input())
    narr = list(map(int,input().split()))

    print(f"#{tase_case} {max(narr) - min(narr)}")