# 문제
# 15650과 똑같으나 if문을 제거하면 해결되는 문제라 생략하겠다.

def backtrack(start):
    if len(arr) == m:
        print(' '.join(map(str,arr)))
        return
    for i in range(start,n+1):
        arr.append(i)
        backtrack(i)
        arr.pop()
n,m = map(int,input().split())

arr= []
backtrack(1)