import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 문제
# DFS를 구현하면 되는 문제이나 조건을 조심하여 풀어야 한다.

# 조건
# 1. 오름차순으로 인접 정점을 방문해야 한다.
# 2. 정점 i의 "방문 순서" 를 출력하는 문제이다. 전체적 방문 결과 X

# 풀이
# 1. n,m,start를 입력받고 크기의 n+1만큼 그래프 2차원리스트를 만든다. (0은 주어지지 않으므로) 
# 2. u,v 값을 입력받아 각 정점에도 서로 간선의 값을 추가한다.
# 3. 오름차순으로 방문해야 하기에 리스트 값들을 정렬한다.
# 4. 글로벌 변수 count를 통해 방문 순서를 기록하고, 재귀함수를 통해 dfs를 수행한다.

def dfs(start):
    global count 

    answer[start] = count
    for v in graph[start]:
        if answer[v]:
            continue
        count +=1
        dfs(v)
    return


n,m,start = map(int,input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
for lst in graph:
    lst.sort()
count = 1
answer = [0] * (n+1)
a = dfs(start)

for x in answer[1:]:
    print(x)