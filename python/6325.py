arr = [2, 4, 6, 8, 10]

def findnumber(n) :
    if n in arr:
        print(f"{n} => True")
    else :
        print(f"{n} => False")
print(arr)
findnumber(5)
findnumber(10)