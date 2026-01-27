H,M = map(int,input().split())
a = int(input())

tm = M + a

H += tm // 60
M = tm % 60

H %= 24

print(H,M)