from collections import deque
import sys
input = sys.stdin.readline

# 문제
# BFS를 구현하면 되는 문제이나 조건을 조심하여 풀어야 한다.
# 처음부터 작성한 코드라 조금 공간 복잡도가 있다. 개선사항으로는 visited를 result로 활용했다면 좋았을 것 같다.

# 조건
# 1. 오름차순으로 인접 정점을 방문해야 한다.
# 2. 정점 i의 "방문 순서" 를 출력하는 문제이다. 전체적 방문 결과 X

# 풀이
# 1. DFS와는 다르게 while문으로 접근했다.
# 2. 그외에는 유사하나 첫줄에 "꼭"
# import sys
# input = sys.stdin.readline
# 3. 이걸 넣어줘야한다. 이거 넣지않아서 오류잡느라 하루종일 걸렸다.. ㅠㅠ 

def bfs(graph,start):
    global count

    visited[start] = True 
    queue = deque([start])
    
    while queue:
        n = queue.popleft()
        result[n] = count
        count +=1
        for i in graph[n]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n,m,start = map(int,input().split())

visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]

for i in range(1,m+1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(len(graph)):
    graph[i].sort()

count = 1
result = [0 for _ in range(n+1)]

bfs(graph,start)

print(*result[1:],sep="\n")
