arr = list(range(1,11))


evennumnber = list(filter(lambda x : x % 2 == 0,arr))

result = list(map(lambda x : x**2,evennumnber))

print(result)