T = int(input())

for tase_case in range(1,T+1):
    str1 = input()
    str2 = input()
    s = str2.find(str1)
    
    answer = 0
    
    if s == -1:
        answer = 0
    else :
        answer = 1

    print(f"#{tase_case} {answer}")
