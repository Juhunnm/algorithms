while 1 : 
    try :
        s = str(input())
    except EOFError:
        break
    
    print(f">> {s.upper()}")