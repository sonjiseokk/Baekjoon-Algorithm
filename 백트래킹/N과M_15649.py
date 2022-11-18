# 문제
# n과 m을 활용하는 정석적인 백트래킹 문제이다.
# 말 그대로 백트래킹이 무엇인지를 이해하는 문제이다.

# 조건
# 1. 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 
# 2. 중복되는 수열을 여러 번 출력하면 안된다. ex) (2,2)
# 3. 수열은 사전 순으로 증가하는 순서로 출력해야 한다.

# 풀이
# 1. list 하나를 정의하여 백트래킹을 시도한다.
# 2. list 안에 i값, 즉 n보다 작은 숫자가 없다면 추가하고 백트래킹을 다시 시도한다.
# 2-1. not in을 통해 중복되는 수열을 제거하는 것이다.
# 3. 순차적으로 진행된다면 result = [1,2] 가 될 것이고, 만약 m = 2 라고 가정한다면,
# 3-1. result의 길이가 m가 같음에 따라 출력되고, 다음 과정에서 result = [1] 이 된 후, 다음 과정이 진행된다.
# 4. 결국 이런식으로 계속 반복하면 결과가 출력되어 정답 판정을 받는다. 



def backtrack():
    if len(result) == m:
        print(' '.join(map(str,result)))
        return
    for i in range(1,n+1):
        if i not in result:
            result.append(i)
            backtrack()
            result.pop()
n,m = map(int,input().split())
result = []

backtrack()