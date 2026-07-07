# 4874. [S/W 문제해결 기본] 5일차 - Forth

T = int(input())

for tase_case in range(1,T+1):
    opcode = input().split()
    stack =[]
    answer = 0
    
    for token in opcode:
        if token.isdigit():
            stack.append(int(token))
        elif token == "+" :
            if len(stack) < 2:
                answer = -1
                break
            stack.append(stack.pop() + stack.pop())
        elif token == "*":
            if len(stack) < 2:
                answer = -1
                break
            stack.append(stack.pop() * stack.pop())
        elif token == "-" :

            if len(stack) < 2:
                answer = -1
                break

            b = stack.pop()
            a = stack.pop()
            stack.append(a - b)
        elif token == "/":

            if len(stack) < 2:
                answer = -1
                break
            
            b = stack.pop()
            a = stack.pop()
            stack.append(a // b)
        elif token == ".":
            if len(stack) != 1:
                answer = -1
                break
            answer = stack.pop()
            break

       
    print(f"#{tase_case} {answer if answer != -1 else 'error'}")


#후위 연산자 피연산자,그리고 연산자 나오면 둘이 계산
#     10 2 + 3 4 + * .
# 10 + 2 = 12
# 3 + 4  = 7
# 12 * 7 = 84

