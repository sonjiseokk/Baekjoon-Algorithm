# 문제
# n과 m을 활용하는 정석적인 백트래킹 문제3 이다.
# 이전 문제에서 중복을 허용하는 방식인데 매우 동일하므로 설명과 조건은 생략하겠다.

def backtrack():
    if len(result) == m:
        print(' '.join(map(str,result)))
        return
    for i in range(1,n+1):
        result.append(i)
        backtrack()
        result.pop()
n,m = map(int,input().split())
result = []

backtrack()