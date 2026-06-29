st = input()

def reverse(str) :
    if str == str[::-1]:
        print(str)
        print("입력하신 단어는 회문(Palindrome)입니다.")
reverse(st)