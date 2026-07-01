T = int(input())

def dfs (v):
    global cnt
    cnt += 1

    for child in tree[v]:
        dfs(child)

for tase_case in range(1,T+1) :
    E,N = map(int,input().split())
    arr = list(map(int, input().split()))
    tree = [[] for _ in range(E + 2)]

    for i in range(0,len(arr),2): 
        parent = arr[i]
        children = arr[i+1]
        tree[parent].append(children)
    

    cnt = 0
    print(tree)
    dfs(N)
    print(f"#{tase_case} {cnt}")