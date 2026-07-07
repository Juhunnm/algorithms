# 4871. [S/W 문제해결 기본] 4일차 - 그래프 경로 D2

def findeNode(start,end) :

    if visited[start] == 1:
        return 0
    
    visited[start] == 1
    
    if start == end:
        return 1

    for i in graph[start]:
        result = findeNode(i,end)

        if result == 1:
            return 1
    return 0



T = int(input())


for tase_case in range(1,T+1):
    V,E = map(int,input().split())
    graph = [[] for _ in range(V + 1)] #이해하기 쉽게 인덱스 1부터

    for i in range(E) :
        node1,node2 = map(int,input().split())
        graph[node1].append(node2)
        print(graph)

    visited = [0] * (V + 1)

    S,G = map(int,(input().split()))
    
    answer = findeNode(S,G)
    # [[], [4, 3], [3, 5], [], [6], [], []]

    print(f"#{tase_case} {answer}")

# 3
# 6 5 V,E

# info
# 1 4
# 1 3
# 2 3
# 2 5
# 4 6

# 1 6 S,G