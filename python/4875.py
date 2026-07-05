# 4875. [S/W 문제해결 기본] 5일차 - 미로 

T = int(input())


topbottom =[-1,0,+1,0]
leftright = [0,-1,0,+1]


def findWay(sr,sc):
    if sr < 0 or sr >= size or sc < 0 or sc >= size: #미로 벗어난 경우
        return
    elif miro[sr][sc] == 1: # 벽인 경우
        return 
    elif visited[sr][sc] == 1: # 방문했던 경우
        return
    if miro[sr][sc] == 3 : # 도착인 경우
        return 1
    
    visited[sr][sc] = 1
    
    for d in range(4):
        nr = sr + topbottom[d]
        nc = sc + leftright[d]
        result = findWay(nr,nc)
        if result == 1:
            return 1    

    return 0

for tase_case in range(1,T+1):
    size = int(input())
    miro =[list(map(int,input())) for _ in range(size)]

    visited = [[0]*size for _ in range(size)]

    answer = 0

    startrow = 0
    startcol = 0
    # 출발지점 찾기
    for r in range(size):
        for c in range(size):
            if miro[r][c] == 2:
                startrow = r
                startcol = c
                break

    answer = findWay(startrow,startcol)
    print(f"#{tase_case} {answer}")

# [[1 3 1 0 1],
#  [1 0 1 0 1],
#  [1 0 1 0 1],
#  [1 0 1 0 1],
#  [1 0 0 2 1]]

# 1 3 1 0 1
# 1 0 1 0 1
# 1 0 1 0 1
# 1 0 1 0 1
# 1 0 0 2 1
# [
# [0, 0, 0, 1, 0], 
# [0, 1, 0, 1, 0], 
# [0, 1, 0, 1, 0], 
# [0, 1, 0, 1, 0], 
# [0, 1, 1, 1, 0]]