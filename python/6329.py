def countdown(cnt):
    if cnt <= 0:
        print("카운트다운을 하려면 0보다 큰 입력이 필요합니다.")
        return
    
    print(cnt)
    if cnt == 1:
        return
    countdown(cnt - 1)

countdown(0)
countdown(10)