T =int(input())

for tase_case in range(1,T+1):  
    N = int(input())
    heap = [0]
    arr = list(map(int,input().split()))

    for i in arr :
        heap.append(i)
        idx = len(heap) - 1
        while idx > 1:
            parentIdx = idx // 2
            if heap[idx] < heap[parentIdx] : 
                heap[idx],heap[parentIdx] = heap[parentIdx],heap[idx] 
                idx = parentIdx
            else :
                break

    lastIdx = len(heap) -1    
    result = 0    
    while lastIdx > 1:
        lastIdx = lastIdx // 2
        result += heap[lastIdx]

    print(f"#{tase_case} {result}")