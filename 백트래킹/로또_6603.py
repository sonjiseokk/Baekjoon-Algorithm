def backtrack(start):
    if len(arr) == 6:
        res.append(arr[:])
        return
    
    for i in range(start,n):
        arr.append(num[i])
        backtrack(i+1)
        arr.pop()

while True:
    num = list(map(int,input().split()))
    if len(num) <= 1 and num[0] == 0:
        break
    n = num[0]
    num = num[1:]

    res = []
    arr =[]

    backtrack(0)
    for x in res:
        print(*x)
    print()