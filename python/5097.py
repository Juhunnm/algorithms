from collections import deque


T =int(input())

for tase_case in range(1,T+1):
    N,M = map(int,input().split())
    queue = deque(map(int,input().split()))

    for i in range(M % N):
        queue.append(queue.popleft())

    
    print(f"#{tase_case} {queue[0]}")