# 4866. [S/W 문제해결 기본] 4일차 - 괄호검사

T = int(input())

for tase_case in range(1,T+1):
    s = list(input())
    arr =[]
    error = False

    for token in s:
        if token in ["{","("]:
            arr.append(token)

        elif token == "}":
                if arr and arr[-1] == "{":
                    arr.pop()
                else :
                    error = True
                    break
        elif token == ")":
                if arr and arr[-1] == "(":
                    arr.pop()
                else:
                    error = True
                    break
    print(f"#{tase_case} { 0 if error or arr else 1}")
    #(