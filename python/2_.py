# 정수형 변수(int)에 숫자 하나를 입력 받아 주세요.
# 입력한 숫자 만큼 위의 배열을 출력 해 주세요.
# 5를 입력하셨다면
# B T K A
# B T K A
# B T K A
# B T K A
# B T K A
# 가 나와야 합니다.

a = int(input())
arr =['B','T','K','A']
for _ in range(a) :
    print(' '.join(arr))  