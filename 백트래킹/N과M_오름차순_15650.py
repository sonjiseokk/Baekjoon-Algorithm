def backtrack(start):
    if len(arr) == m:
        t = arr[:]
        t.reverse()
        if t != arr and arr not in result:
            if t[0] > arr[0]:
                result.append(arr[:])
        return
    for i in range(start,n+1):
        arr.append(i)
        backtrack(start+1)
        arr.pop()
n,m = map(int,input().split())
result = []
arr= []
backtrack(1)
for i in range(len(result)):
    print(" ".join(map(str,result[i])))