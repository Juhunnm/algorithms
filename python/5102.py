from collections import deque


T = int(input())

for tase_case in range(1,T+1):
    V,E = map(int,input().split())

    graph = [[] for _ in range(V+1)]

    for i in range(E):
        node1,node2 = map(int,input().split())

        graph[node1].append(node2)
        graph[node2].append(node1)

    S,G = map(int,input().split())

    queue = deque()
    queue.append(S)
    visited = [0] * (V + 1)
    visited[S] = 1

    while queue:
        node = queue.popleft()

        if node == G:
            break

        for i in graph[node]:
            if visited[i] == 0:
                visited[i] = visited[node] + 1
                queue.append(i)
    
    print(f"#{tase_case} {visited[G] - 1 if visited[G] !=0 else 0}")
    # [[], [4, 3], [3, 5], [1, 2], [1, 6], [2], [4]]
    # 1[4,3] 6 [4]
    # 1[4,3] 5[2]
# 1

# 6 5

# 1 4
# 1 3
# 2 3
# 2 5
# 4 6

# 1 6
