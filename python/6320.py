person1 = input()
pserson2 = input()

a = input()
b = input()


def win(a,b) :
    if a=="가위" and b =="바위" :
        print("바위가 이겼습니다!")
    elif a=="가위" and b=="보":      
        print("가위가 이겼습니다!")
    elif a=="바위"and b=="보":  
        print("보가 이겼습니다!")

win(a,b)
