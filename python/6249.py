n = input()

arr = [0] * 10

for a in n:
    arr[int(a)] += 1 

for i in range(len(arr)):
    print(i,end=" ")
print()

for i in arr:
    print(i, end=" ")