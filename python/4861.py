# 4861. [S/W 문제해결 기본] 3일차 - 회문

T = int(input())

for tase_case in range(1,T+1):

    N,M = map(int,input().split())
    maxtrix = [list(input()) for _ in range(N)]
    answer = []
    #가로
    for r in range(N):
        for c in range(N - M + 1):#시작 column
            for k in range(M // 2):#횟수 
                if maxtrix[r][c+k] != maxtrix[r][c+M-1-k]:
                    break
            else:
                answer = maxtrix[r][c:c+M]

    #세로

    for c in range(N):
        for r in range(N-M+1):
            for k in range(M //2):
                if maxtrix[r+k][c] != maxtrix[r+M-1-k][c]:
                    break
            else :
                for i in range(M):
                    answer.append(maxtrix[r+i][c])

        
    print(f"#{tase_case} {answer}")



# [가로]다 같으면 같은것 
# [4][1] [4][-1]
# [4][2] [4][-2]
# [4][3] [4][-3]
# [4][4] [4][-4]
# #[세로]
# [0][1] - [-1][1]
# [2][1] - [-2][1]
# [3][1] - [-3][1]
# [4][1] - [-4][1]