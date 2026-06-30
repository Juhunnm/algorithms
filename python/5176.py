# T = int(input())


# def subroot (start,end,node):
#     if start > end:
#         return
     
#     n = end - start + 1
#     root = start + n // 2 
#     tree[node] = root

#     subroot(start,root - 1 ,node * 2)
#     subroot(root + 1,end,node * 2 + 1)


# for tast_case in range(1,T+1):
#     N = int(input())
#     tree = [0] * (N * 2 +1)

#     subroot(1,N,1)
#     print(tree)
#     print(f"#{tast_case} {tree[1]} {tree[int(N//2)]}")

T = int(input())


def inord(node) :
    global cnt
    if node <= N :
        inord(node * 2)
        tree[node] = cnt
        cnt += 1
        inord(node * 2 + 1)


for tast_case in range(1,T+1):
    N = int(input())
    tree = [0] * (N+1)
    cnt = 1
    inord(1)
    print(f"#{tast_case} {tree[1]} {tree[int(N//2)]}")
