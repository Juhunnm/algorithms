# 4873. [S/W 문제해결 기본] 4일차 - 반복문자 지우기 D2

T = int(input())

for tase_case in range(1,T+1):
    s = list(input())
    stack =[]

    for token in s:
        if len(stack) <= 0: # 처음 값 들어올떄
            stack.append(token)
            continue

        if(stack[-1] == token):
            stack.pop()
            continue

        stack.append(token)
    print(f"#{tase_case} {len(stack)}")
