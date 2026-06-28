T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
      n, a = input().split()
      n = int(n)
      answer = ""

      for i in range(n) :
        num = int(a[i],16) 
        binary = ""

        while num > 0 :
            binary = str(num % 2) + binary
            num //= 2
        while len(binary) < 4 :
            binary = "0" + binary 
        answer += binary

      print(f"#{test_case} {answer}")