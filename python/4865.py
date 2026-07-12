# 4865. [S/W 문제해결 기본] 3일차 - 글자수 D2\

T = int(input())

for tase_case in range(1,T+1):
    s1 ={}

    str1 = list(input())
    str2 = list(input())
    for char in str1:
        s1[char]  = 0
    for char in str2:
        if char in s1.keys():
            s1[char] += 1
            
    print(f"#{tase_case} {max(s1.values())}")
