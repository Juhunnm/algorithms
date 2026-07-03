# 4880. [S/W 문제해결 기본] 5일차 - 토너먼트 카드게임

T = int(input())

def compare(a,b):  
    ca = cards[a]
    cb = cards[b] 

    if ca == cb:
        return a if a < b else b
        
    elif (ca % 3) + 1 == cb :
        return b
    else :
        return a

def game(i,j):
    if i == j:
        return i
    
    left = game(i,(i+j)//2)
    right = game((i+j)//2 +1 ,j)

    return compare(left,right)
    
for tase_case in (range(1,T+1)):
    N = int(input())
    cards = list(map(int,input().split()))
    
    winer = game(0,N-1)
    
    print(f"#{tase_case} {winer + 1}")


# 3

# 4
# 1 3 2 1

    #1 가위
    #2 바위
    #3 보

    # 1 3 2 1 1 3 2 1