# 4865. [S/W 문제해결 기본] 3일차 - 글자수 D2

T = int(input())

for tase_case in range(1,T+1):
    s1 ={}
    s2 ={}

    str1 = list(input())
    str2 = list(input())
    for char in str1:
        s1[char] = s1.get(char,0) + 1

    for char in str2:
        s2[char] = s2.get(char,0) + 1

    print(s1,s2)

    print(f"#{tase_case} {max(max(s1.values()),max(s2.values()))}")

    