# 6칸으로 이뤄진 arr배열을 만들어 주세요.
# arr[0]에서 arr[2]에는 세 수를 입력 받아 주세요.
# 이후 정수 1개를 한번 더 입력 받고, 
# arr[3]에서 arr[5]에 입력받은 값으로 부터 1씩 증가한 값으로 채워주세요.
# 만약 아래와 같이 입력이 주어진다면
# 아래 그림처럼 배열에 값이 채워집니다.
# [입력]
# 3 2 5
# 4
arr = [0] * 6

a = list(map(int, input().split()))
for i in range(3):
    arr[i] = a[i]

b = int(input())
for i in range(3, 6):
    b += 1
    arr[i] = b

print(arr)
